#!/usr/bin/env python3
"""Exporta el corte privado sin cambiar las fuentes copiadas en data/private/raw."""
from pathlib import Path
from collections import Counter
import hashlib, json

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'data/private/raw'
OUT=ROOT/'data/private/export'
OUT.mkdir(parents=True,exist_ok=True)
source=json.loads((RAW/'registro_consulta_actual.json').read_text())
log=json.loads((RAW/'bitacora_data.json').read_text())
registered=source['registros']
extra=log.get('visitas',[])

households=[{'house_id':n,'residents_label':next(r['nombre'] for r in registered if r['casa']==n),
             'residents_individuals_unverified':True} for n in range(1,18)]

vehicles=[]
for r in registered:
    vehicles.append({
        'vehicle_id':r['id'],'house_id':r['casa'],
        'class':'known_visit_vehicle' if r['visita'] else 'resident_vehicle',
        'model_label':r['automovil'],'plate_display':r['placas'],
        'plate_key':r.get('placas_busqueda'),'color':r['color'],'body_type':r['tipo'],
        'notes':r.get('anotaciones',''),'source':'registro_consulta_actual.json',
        'reference_image_url':(r.get('referencia') or {}).get('image')
    })
for v in extra:
    if v['automovil']=='No indicado':continue  # Sushito llegó sin automóvil identificado.
    vehicles.append({'vehicle_id':v['id'],'house_id':v['casa'],'class':'visit_vehicle',
                     'model_label':v['automovil'],'plate_display':v['placas'],
                     'plate_key':None,'color':v['color'],'body_type':v['tipo'],
                     'notes':v['anotaciones'],'source':'aviso_usuario_2026-10-03',
                     'reference_image_url':None})

visitors=[
    {'visitor_id':'hugo-hernandez-20261003','house_id':12,'name':'Hugo Hernández',
     'vehicle_id':'vis-20261003-1201','presence':'unknown_after_vehicle_departure',
     'notes':'Entró 15:02; la Cadillac salió 15:04. No se confirmó si Hugo iba a bordo.'},
    {'visitor_id':'sushito-20261003','house_id':12,'name':'Sushito',
     'vehicle_id':None,'presence':'last_seen_entering',
     'notes':'Entró 15:06. Vehículo, placas y nombre legal no indicados.'}
]

lookup={v['vehicle_id']:v for v in vehicles}
events=[]
for seq,(at,house,vid,driver,action,note) in enumerate(log['movimientos'],1):
    is_person=vid=='vis-20261003-1202'
    vehicle=None if is_person else lookup.get(vid)
    if not is_person and vehicle is None:raise ValueError(f'Vehículo desconocido en evento {seq}: {vid}')
    events.append({
      'event_id':f'legacy-20261003-{seq:03d}','source_order':seq,
      'date':'2026-10-03','time':at or None,'house_id':house,
      'event_type':'person_movement' if is_person else 'vehicle_movement',
      'vehicle_id':None if is_person else vid,
      'visitor_id':'sushito-20261003' if is_person else 'hugo-hernandez-20261003' if vid=='vis-20261003-1201' and action=='Entrada' else None,
      'direction':'in' if action=='Entrada' else 'out',
      'name_as_recorded':driver,'note':note,
      'source':'photographed_log' if note.startswith('Foto') else 'user_message',
      'time_precision':'unknown' if not at else 'minute',
      'person_presence_confirmed':is_person or (vid=='vis-20261003-1201' and action=='Entrada')
    })

last={}
for e in events:
    if e['vehicle_id']:last[e['vehicle_id']]=e
resident=[v for v in vehicles if v['class']=='resident_vehicle']
status=[]
for v in resident:
    e=last.get(v['vehicle_id'])
    status.append({'vehicle_id':v['vehicle_id'],'house_id':v['house_id'],
                   'status':'no_movement_recorded' if not e else 'last_seen_out' if e['direction']=='out' else 'last_seen_in',
                   'last_event_id':e['event_id'] if e else None,
                   'last_event_time':e['time'] if e else None})

counts=Counter(s['status'] for s in status)
assert len(households)==17 and len(resident)==43 and len(vehicles)==48
assert len(events)==31 and counts=={'last_seen_out':6,'last_seen_in':11,'no_movement_recorded':26}
assert next(e for e in events if e['event_id']=='legacy-20261003-030')['time']=='15:04'
assert events[-1]['event_type']=='person_movement' and events[-1]['time']=='15:06'

def write(name,obj):
    (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
write('households.json',households);write('vehicles.json',vehicles)
write('visitors.json',visitors);write('events.json',events)
write('vehicle_status_at_cutoff.json',status)
files=sorted(f for f in (ROOT/'data/private').rglob('*') if f.is_file() and 'export' not in f.parts)
manifest={'snapshot_date':'2026-10-03','cutoff_reported_at':'15:06 America/Mexico_City',
          'counts':{'houses':17,'resident_vehicles':43,'known_visit_vehicles':4,'new_visit_vehicles':1,
                    'visitors_named_today':2,'events':31,**dict(counts)},
          'sources':[{'path':str(f.relative_to(ROOT)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in files],
          'limitations':['Estado de residentes no deducible de automóviles sin movimiento.',
                         'Cadillac salió 15:04; no se confirmó salida de Hugo.',
                         'Sushito entró sin vehículo identificado.',
                         'Hora exacta de llegada del Jetta desconocida.']}
write('manifest.json',manifest)
print(json.dumps(manifest['counts'],ensure_ascii=False))
