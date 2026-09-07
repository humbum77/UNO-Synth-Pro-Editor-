import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import App
import storage
app=App()
# prevent real MIDI I/O during GUI smoke test
app.midi.send_cc=lambda *a,**k: None
app.midi.sysex=lambda *a,**k: None
app.midi.bank_program=lambda *a,**k: None
app.midi.note_on=lambda *a,**k: None
app.midi.note_off=lambda *a,**k: None
app.midi.pitch_bend=lambda *a,**k: None
app.midi.read_state=lambda *a,**k: None
app.update_idletasks(); app.redraw()
assert app._design_height()==1000
for page in ('SYNTH','ARP + SEQUENCER','SONG','LIBRARY'):
    app.page=page; app.keyboard_visible=True; app.redraw(); app.update_idletasks()
    assert app._design_height()==1000
app.page='LIBRARY'; app.redraw(); app.update_idletasks(); assert app._lib_search_entry is not None
app.randomize_synth(); assert app.preset.name=='RANDOM'
app.seq_randomize(); assert any(st.notes for st in app.preset.sequence.steps[:app.preset.sequence.length])
app.init_patch(); assert app.preset.name=='INIT'
assert storage.PRESETS.name=='UNO Synth Pro'
assert storage.SONGS.name=='song'
app._closing=True; app.destroy()
print('v1.46 smoke OK')
