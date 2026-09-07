"""Headless state-machine smoke test for v1.40 LIVE delayed PLAY/STOP."""
from app import App

class MidiStub:
    def __init__(self):
        self.started = 0
        self.stopped = 0
    def start(self): self.started += 1
    def stop(self): self.stopped += 1
    def inputs(self): return []
    def outputs(self): return []
    def close(self): pass

app = App()
try:
    app.midi = MidiStub()
    app.live_delay = 5
    app.toggle_live_play()
    assert app.live_countdown_remaining == 5 and not app.live_playing
    for _ in range(5):
        if app._live_countdown_job is not None:
            try: app.after_cancel(app._live_countdown_job)
            except Exception: pass
            app._live_countdown_job = None
        app._live_countdown_tick()
    assert app.live_playing and app.midi.started == 1
    app.toggle_live_play()
    assert not app.live_playing and app.midi.stopped == 1
    print('PASS')
finally:
    try: app.destroy()
    except Exception: pass
