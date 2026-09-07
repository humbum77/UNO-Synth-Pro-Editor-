from pathlib import Path
import json,logging
from data_model import *
ROOT=Path.home()/'Documents'/'IK Multimedia'/'UNO Synth Pro'; PRESETS=ROOT; SONGS=ROOT/'songs'; SETTINGS=ROOT/'settings.json'
logger=logging.getLogger(__name__)
for p in (ROOT,PRESETS,SONGS):p.mkdir(parents=True,exist_ok=True)
DEFAULT={'midi_in':'UNO_RETURN','midi_out':'UNO_TAP','midi_controller':'Off','midi_in_channel':1,'midi_out_channel':1,'midi_clock':'Off','sync':'Internal','soft_thru':True,'pr_change':True,'midi_interface':'Auto','knob_behavior':'Relative','pitch_bend_range':2,'master_tuning':0,'keyboard_visible':False,'preview':False,'live_delay':0}
def load_settings():
 d=dict(DEFAULT)
 try:
  if SETTINGS.exists():d.update(json.loads(SETTINGS.read_text(encoding='utf-8')))
 except (OSError,json.JSONDecodeError,TypeError,ValueError) as e:logger.warning('Failed to load settings %s: %s',SETTINGS,e)
 return d
def save_settings(d):SETTINGS.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
def _safe(s):return ''.join(c for c in s if c not in '<>:"/\\|?*').strip() or 'Untitled'
def list_presets(category='All',query=''):
 out=[];q=query.lower().strip()
 for p in PRESETS.rglob('*.unosyp'):
  if SONGS in p.parents: continue
  try:
   d=json.loads(p.read_text(encoding='utf-8')); n=d.get('name',p.stem); c=d.get('category','My Presets');t=d.get('tags',[])
  except (OSError,UnicodeDecodeError,json.JSONDecodeError,TypeError,ValueError):
   # Official *.unosyp may be opaque/binary; still show and manage it as a preset file.
   n=p.stem;c='My Presets';t=[]
  if (category=='All' or c==category) and (not q or q in (' '.join([n,c,*t]).lower())):out.append((n,c,t,p))
 return sorted(out,key=lambda x:x[0].lower())
def categories():return ['All']+sorted({x[1] for x in list_presets() if x[1]!='All'}|{'My Presets'})
def save_preset(preset,category=None):
 if category:preset.category=category
 p=PRESETS/(_safe(preset.name)+'.unosyp');i=2
 while p.exists():p=PRESETS/f'{_safe(preset.name)} {i}.unosyp';i+=1
 preset.save(p);return p
def load_preset(path):
 d=json.loads(Path(path).read_text(encoding='utf-8'));sd=d.get('sequence',{});seq=Sequence(length=int(sd.get('length',16)),direction=sd.get('direction','Forward'),transpose=int(sd.get('transpose',0)))
 ss=sd.get('steps',[]);seq.steps=[Step(**x) for x in ss[:64]]+[Step() for _ in range(max(0,64-len(ss)))];seq.automation=sd.get('automation',seq.automation)
 return Preset(d.get('name','INIT'),d.get('number'),d.get('params',{}),seq,d.get('tags',[]),d.get('category','My Presets'),d.get('source','local'))
def list_songs():return sorted(SONGS.glob('*.unosong'),key=lambda p:p.stem.lower())
def save_song(song):
 p=SONGS/(_safe(song.name)+'.unosong');song.save(p);return p
