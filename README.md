*English | [Русский](README.ru.md)*

# UNO Synth Pro Editor

An advanced editor for the **IK Multimedia UNO Synth Pro** synthesizer — a full-screen desktop application that gives you every synthesis parameter on one screen, in real time over MIDI, without scrolling through menus on the hardware.

Current version: **v1.47**

---

## How it differs from the official IK Multimedia editor

Core sound editing (oscillators, filters, envelopes, LFOs, modulation matrix, effects) works the same way as in the official editor — listed below is only what it does not have, or what is done differently here.

- **Everything on one SYNTH page.** Synthesis parameters, the 16-slot modulation matrix and the whole effects section are visible and editable at the same time, without switching tabs or pages.
- **A preset library that is not limited to 256 slots.** It uses the standard `*.unosyp` preset files, but adds its own categories, tags and search across nested folders — your collection is no longer bound to the synth's memory slots. You can store as many copies of the same patch as you like, each with a different sequence — handy when assembling a song later.
- **Auditioning presets without writing them into the synth's memory.** Any preset from the library can be heard on the hardware immediately, without occupying or overwriting one of the 256 slots — something the official editor cannot do.
- **A genuinely usable SONG mode.** The whole song is visible at once on a 64-position grid: presets are placed with the mouse, and length, tempo and copying sections take a couple of clicks. Editing a song on the synth itself is painful; here it is ordinary on-screen work.
- **A brand-new LIVE mode.** Instant access to saved song files on stage: the song list on the left, a 4×16 grid for switching on the fly. Nothing with this logic exists in the synth or in the official editor — it turns the UNO Synth Pro into an instrument for live performance.
- **FILL 64 in the sequencer.** One click repeats the pattern you have written across all 64 steps.
- **Musical randomisation.** RANDOM generates a complete patch using algorithms tuned to produce usable sounds rather than noise, and the sequencer has its own randomiser: a scale-constrained random walk with note density, humanised velocity and gate, and smooth CC automation.

---

## Features

### Arpeggiator and sequencer (ARP + SEQUENCER page)

- ARP: 10 modes (UP, DOWN, U/D, UD+, D/U, DU+, RND, PLY, X2U, X2D), 1–4 octave range, Gate 0–10, Swing 50–80 %, Hold, and 16 trigger steps in a 2×8 layout.
- Sequencer with up to 64 steps and a piano roll: up to 3 notes per step; a tie is drawn as a continuation of the note block.
- Playback direction: Forward / Backward / Back'n'Forth, Transpose ±12 semitones.
- Per-step editor: Gate, Accent, Velocity, Length, Probability, and four CC automation slots MOD1–MOD4.
- FILL 64 — repeats the current pattern up to 64 steps; CLEAR, COPY, PASTE and RANDOM sit next to it.
- RANDOM generates a melodic sequence together with its CC automation.
- Software playback: the editor sends Note On/Off itself, honouring Gate, Tie, Velocity, Transpose, step probability and per-step CC automation.

### Preset library (LIBRARY page)

- A local library with no 256-slot limit: categories, tags and search handled by the editor.
- Standard `*.unosyp` preset format; search also covers nested category folders.
- ADD imports existing preset files, SAVE stores the current sound.
- A separate Hardware Presets list (1–256, names only) — no invented categories the hardware does not have.
- PREVIEW is a separate checkbox, so nothing is ever sent to the synth by accident.
- Two-way preset number changes between editor and UNO via Bank Select / Program Change, with no echo of incoming changes.

### Song and Live (SONG page)

- SONG: a 64-position grid (4 columns × 16 rows), Tempo, Length 1–64, Play/Stop, Copy/Paste/Clear, Save/Load.
- Songs are stored as `*.unosong` files.
- LIVE: the same 4×16 grid with the list of saved songs on the left for fast switching on stage.

### MIDI settings (SETTINGS page)

- MIDI IN / OUT port selection plus a separate MIDI controller port.
- MIDI IN Channel (OMNI / 1–16) and MIDI OUT Channel (1–16).
- MIDI Clock Send: Off / MIDI / CV Sync; Sync Receive: Internal / External / USB / CV Sync.
- Soft Thru, Program Change, MIDI Interface, Knob Behavior, Pitch Bend Range 1–12, Master Tuning ±50 cents.
- The MIDI port list is cached rather than re-scanned on every redraw; the port is opened on APPLY.

### Interface

- Fully scalable interface with a fixed aspect ratio; the initial window size is chosen to fit the screen.
- On-screen keyboard (toggled from the top-right corner) with PITCH, MOD and octave selection.
- Quick actions in the top bar: RANDOM, INIT, SAVE, STORE, SETTINGS, READ.

---

## Development status

Temporary limitation: bulk preset write (SysEx command `0x28`) is not sent yet — its format is not fully confirmed. The STORE / SEND / DEPLOY TO UNO buttons exist in the interface but stay disabled until protocol reverse-engineering is finished.

The protocol map contains only those CC numbers and SysEx fields that are confirmed by the official MIDI documentation or observed in real traffic with the device.

---

## Requirements

- Windows — MIDI runs directly through the system `winmm.dll`; on other platforms the app starts in offline mode without MIDI.
- Python 3.10+
- Pillow >= 10.0

## Install and run

```bash
pip install -r Docs/requirements.txt
python main.py
```

On Windows you can use the bundled `install_dependencies.bat` and `run_editor.bat`.

## Project layout

| File | Purpose |
| --- | --- |
| `main.py` | Entry point, logging setup |
| `app.py` | Tkinter interface: SYNTH / ARP + SEQUENCER / LIBRARY / SONG / SETTINGS pages |
| `midi_interface.py` | Low-level WinMM MIDI wrapper (ctypes), including SysEx |
| `midi_engine.py` | High-level MIDI layer: CC, Program Change, notes, transport |
| `protocol_map.py` | CC map, SysEx commands, filter and effect enum values |
| `data_model.py` | Data models: `Step`, `Sequence`, `Preset`, `SongSlot`, `Song` |
| `storage.py` | Reading and writing presets, songs and settings |
| `Docs/` | Changelogs, validation reports, interface mock-ups |
| `Assets/` | Interface reference images |

## User data

```
~/Documents/IK Multimedia/UNO Synth Pro/
├── *.unosyp          presets
├── songs/*.unosong   songs
└── settings.json     settings
```

## Contributing

Changes go through branches and pull requests:

```bash
git checkout -b feature/short-description
git add <files>
git commit -m "Short description"
git push -u origin feature/short-description
```

Versions are published as tags (`v1.47`, `v1.48`, ...) instead of archives.

## Legal

An unofficial project. UNO Synth Pro and IK Multimedia are trademarks of their respective owners; this project is not affiliated with or endorsed by them.
