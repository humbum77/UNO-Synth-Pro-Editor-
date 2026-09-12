*English | [Русский](README.ru.md)*

# UNO Pro Advanced

Unofficial advanced editor / librarian / sequencer workspace for the **IK Multimedia UNO Synth Pro** family.

Current development version: **v0.9.0-beta**  
Legacy transition baseline: **v1.64 FIX2**

> The project has entered beta testing. Historical v1.x development archives are kept with their original names; new versions use pre-1.0 beta numbering. See `Docs/VERSIONING.md`.

## Current scope

- Real-time synth editing over MIDI.
- Preset library with local files and hardware preset navigation.
- ARP + 64-step sequencer / piano roll editor.
- SONG and LIVE workflows.
- On-screen keyboard with pitch bend, modulation and octave control.
- Read-only hardware sequencer retrieval through the confirmed `0x29` preset-page protocol.
- MIDI Clock master support over MIDI/USB transport.
- Extensive protocol and hardware-research documentation under `Docs/`.

## Hardware / protocol status

Confirmed work includes preset selection/name handling, current-state reads, preset/page reads through `0x29`, and MIDI transport / clock behaviour validated on real hardware.

Important current limitations:

- Hardware **SEQ ON/OFF** control is not yet decoded. MIDI Clock plus PLAY/STOP works when the UNO is synchronized over USB, but switching the hardware sequencer itself still requires a separate confirmed command.
- Permanent STORE / preset write remains locked. The project does not enable unconfirmed destructive SysEx behaviour.
- Some sequencer/UI workflow items are still being refined during beta testing.

## Requirements

- Windows for direct WinMM MIDI operation.
- Python 3.10+
- Pillow >= 10.0

## Run

```bash
pip install -r Docs/requirements.txt
python main.py
```

On Windows you can also use `install_dependencies.bat` and `run_editor.bat`.

## Project layout

| Path | Purpose |
| --- | --- |
| `main.py` | Application entry point |
| `app.py` | Main Tkinter UI and application logic |
| `midi_interface.py` | Low-level Windows MIDI / SysEx layer |
| `midi_engine.py` | Higher-level MIDI transport, clock, CC and note operations |
| `protocol_map.py` | Confirmed protocol mappings and request builders |
| `hardware_seq_0x29.py` | Read-only hardware sequence page decoder |
| `data_model.py` | Sequence, preset and song data models |
| `storage.py` | Preset/song/settings persistence |
| `unosyp_state_decoder.py` | `.unosyp` state decoding helpers |
| `unosyp_seq_decoder.py` | `.unosyp` sequence decoding helpers |
| `Docs/` | Project state, protocol research, validation and build history |

## Versioning

The former fast-moving internal numbering ended at **v1.64 FIX2**. New beta builds use:

- `v0.9.x-beta` for incremental fixes;
- `v0.10.0-beta`, `v0.11.0-beta`, etc. for larger functional milestones;
- `v1.0.0` for the first validated stable release.

Historical files are not renumbered.

## Safety rule

The protocol map is evidence-driven. Unconfirmed MIDI/SysEx mappings must not be invented or enabled as destructive write operations. STORE remains locked until the write path is sufficiently decoded and validated.

## Legal

Unofficial project. UNO Synth Pro and IK Multimedia are trademarks of their respective owners. This project is not affiliated with or endorsed by IK Multimedia.
