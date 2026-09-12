# UNO Pro Advanced — beta state

Current development line: **v0.9.0-beta**  
Legacy transition baseline: **v1.64 FIX2**

## Confirmed hardware status

- Normal-mode hardware preset/page read through SysEx `0x29` is integrated.
- Hardware sequences are decoded from pages 0..4; all tested presets currently work except preset #2, which remains a separate unresolved case.
- MIDI Clock over USB is heard by the UNO when the synth is configured for USB synchronization.
- PLAY / STOP work over the current MIDI transport path.
- Hardware **SEQ ON/OFF** remains unresolved and must be decoded as a separate hardware command; it is not treated as a Clock problem.
- Permanent STORE / bulk write remains locked.

## Current beta UI/workflow items

Planned for the next beta implementation pass:

- Remove custom UI scale presets and the scale control; keep the current window resizing behaviour instead.
- Fix vertical-fader label geometry through a shared vertical-fader layout rather than per-block offsets.
- Restore drag visualization in LIVE mode.
- Sequencer: move MANUAL into QUICK, reduce FILL, and add Save / Save As controls.
- Sequencer project workflow: one song/project = one folder; sequence variants are separate files in that folder, without automatically generated Verse/Chorus subfolders.
- Save As keeps the project folder as the default destination and makes the new file the current working file.
- Add current-octave display next to the octave up/down controls.
- Replace the bright piano-roll playback indicator with a subtle vertical playhead line.
- After sequence load, auto-position the piano roll to the most useful/dense note range; indicate notes above/below the visible range.

## Versioning

See `VERSIONING.md`. Historical v1.x build names remain unchanged; new builds no longer use `FIX` / `FIX2` suffixes.
