from pathlib import Path
import json,logging,os,sys,tempfile
from data_model import *

logger=logging.getLogger(__name__)

def _documents_folder():
    # Windows CSIDL_PERSONAL resolves the user's actual (including redirected/OneDrive) Documents folder.
    if sys.platform.startswith('win'):
        try:
            import ctypes
            buf=ctypes.create_unicode_buffer(32768)
            # CSIDL_PERSONAL = 5, SHGFP_TYPE_CURRENT = 0
            hr=ctypes.windll.shell32.SHGetFolderPathW(None,5,None,0,buf)
            if hr==0 and buf.value:return Path(buf.value)
        except Exception as e:
            logger.warning('Windows Documents lookup failed: %s',e)
    return Path.home()/'Documents'

DOCUMENTS=_documents_folder()
ROOT=DOCUMENTS/'IK Multimedia'/'UNO Synth Pro Editor'
PRESETS=ROOT
SONGS=ROOT/'songs'
SETTINGS=ROOT/'settings.json'
DEFAULT={'midi_in':'UNO Synth Pro','midi_out':'UNO Synth Pro','midi_controller':'Off','midi_in_channel':1,'midi_out_channel':1,'midi_clock':'Off','sync':'Internal','soft_thru':True,'pr_change':True,'midi_interface':'Auto','knob_behavior':'Relative','pitch_bend_range':2,'master_tuning':0,'keyboard_visible':False,'preview':False,'live_delay':0,'live_slots':[None]*64}
_preset_cache=None
_preset_cache_sig=None

def ensure_dirs():
    ROOT.mkdir(parents=True,exist_ok=True);SONGS.mkdir(parents=True,exist_ok=True)

def load_settings():
    d=dict(DEFAULT);d['live_slots']=list(DEFAULT['live_slots'])
    try:
        if SETTINGS.exists():d.update(json.loads(SETTINGS.read_text(encoding='utf-8')))
    except (OSError,json.JSONDecodeError,TypeError,ValueError) as e:logger.warning('Failed to load settings %s: %s',SETTINGS,e)
    slots=d.get('live_slots')
    d['live_slots']=(list(slots[:64])+[None]*64)[:64] if isinstance(slots,list) else [None]*64
    return d

def save_settings(d):
    ensure_dirs()
    text=json.dumps(d,ensure_ascii=False,indent=2)
    fd,tmp=tempfile.mkstemp(prefix='settings.',suffix='.tmp',dir=str(ROOT))
    try:
        with os.fdopen(fd,'w',encoding='utf-8') as f:f.write(text);f.flush();os.fsync(f.fileno())
        os.replace(tmp,SETTINGS)
    finally:
        try:
            if os.path.exists(tmp):os.unlink(tmp)
        except OSError:pass

def _safe(s):return ''.join(c for c in s if c not in '<>:"/\\|?*').strip() or 'Untitled'

def invalidate_preset_cache():
    global _preset_cache,_preset_cache_sig
    _preset_cache=None;_preset_cache_sig=None

def _scan_signature():
    if not PRESETS.exists():return ()
    try:
        return tuple(sorted((str(p),p.stat().st_mtime_ns,p.stat().st_size) for p in PRESETS.rglob('*.unosyp') if SONGS not in p.parents))
    except OSError:return ()

def _all_presets():
    global _preset_cache,_preset_cache_sig
    sig=_scan_signature()
    if _preset_cache is not None and sig==_preset_cache_sig:return _preset_cache
    out=[]
    for p,_,_ in sig:
        p=Path(p)
        try:
            d=json.loads(p.read_text(encoding='utf-8'));n=d.get('name',p.stem);c=d.get('category','My Presets');t=d.get('tags',[])
        except (OSError,UnicodeDecodeError,json.JSONDecodeError,TypeError,ValueError):
            n=p.stem;c='My Presets';t=[]
        out.append((n,c,t,p))
    _preset_cache=sorted(out,key=lambda x:x[0].lower());_preset_cache_sig=sig
    return _preset_cache

def list_presets(category='All',query=''):
    q=query.lower().strip();out=[]
    for n,c,t,p in _all_presets():
        if (category=='All' or c==category) and (not q or q in (' '.join([n,c,*t]).lower())):out.append((n,c,t,p))
    return out

def categories():return ['All']+sorted({x[1] for x in _all_presets() if x[1]!='All'}|{'My Presets'})

def save_preset(preset,category=None):
    ensure_dirs()
    if category:preset.category=category
    p=PRESETS/(_safe(preset.name)+'.unosyp');i=2
    while p.exists():p=PRESETS/f'{_safe(preset.name)} {i}.unosyp';i+=1
    preset.save(p);invalidate_preset_cache();return p

def load_preset(path):
    d=json.loads(Path(path).read_text(encoding='utf-8'));sd=d.get('sequence',{});seq=Sequence(length=int(sd.get('length',16)),direction=sd.get('direction','Forward'),transpose=int(sd.get('transpose',0)))
    ss=sd.get('steps',[]);seq.steps=[Step(**x) for x in ss[:64]]+[Step() for _ in range(max(0,64-len(ss)))];seq.automation=sd.get('automation',seq.automation)
    return Preset(d.get('name','INIT'),d.get('number'),d.get('params',{}),seq,d.get('tags',[]),d.get('category','My Presets'),d.get('source','local'))


def child_folders(folder):
    """Direct child directories for the LOCAL library browser."""
    try:
        folder=Path(folder)
        if not folder.exists():
            return []
        out=[]
        songs_resolved=None
        try:
            songs_resolved=SONGS.resolve()
        except OSError:
            pass
        for p in folder.iterdir():
            if not p.is_dir():
                continue
            if songs_resolved is not None:
                try:
                    if p.resolve()==songs_resolved:
                        continue
                except OSError:
                    pass
            out.append(p)
        return sorted(out,key=lambda p:p.name.lower())
    except OSError as e:
        logger.warning('Failed to list child folders %s: %s',folder,e)
        return []

def local_folders():
    """Top-level LOCAL preset folders for the main preset selector tree."""
    return child_folders(PRESETS)

def list_songs():
    if not SONGS.exists():return []
    return sorted(SONGS.glob('*.unosong'),key=lambda p:p.stem.lower())

def save_song(song):
    ensure_dirs();p=SONGS/(_safe(song.name)+'.unosong');song.save(p);return p
