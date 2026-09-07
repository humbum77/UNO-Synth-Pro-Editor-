UNO Synth Pro Editor v1.12 — SETTINGS DROPDOWNS
===================================

ЗАПУСК
1. Запустите run_editor.bat.
2. По умолчанию редактор пытается использовать:
   MIDI IN  = UNO_RETURN
   MIDI OUT = UNO_TAP
   Это соответствует исследовательской схеме через MIDI Monitor / Proxy.
3. Для прямого подключения откройте SETTINGS и выберите физические MIDI-порты UNO Synth Pro.
4. Интерфейс масштабируется целиком под размер окна. На старте размер выбирается по экрану так, чтобы элементы не обрезались.

ГЛОБАЛЬНАЯ КЛАВИАТУРА
Кнопка с клавишами в правом верхнем углу показывает/скрывает клавиатуру на рабочих страницах.
Слева на клавиатуре — PITCH, MOD и RANGE / C2.

SYNTH
Рабочие интерактивные экраны и линии: OSC waveform, FILTER response, FILTER ENV, AMP ENV.
Подтвержденные CC отправляются в UNO в реальном времени.
Все непрерывные параметры оформлены тонкими линиями; увеличенная невидимая зона мыши сохраняет удобство редактирования.
MOD MATRIX: 16 строк, Source / Amount / Destination / Fade In в одной колонке маршрутов.
Полные списки Source/Destination взяты из руководства UNO Synth Pro.

ARP + SEQUENCER
ARP: 10 режимов, диапазон 1–4 октавы, Gate 0–10, Swing 50–80%, Hold, 16 trigger steps 2x8.
Sequencer: 64 шага; piano-roll позволяет до 3 нот на шаг; Direction Forward/Backward/Back'n'Forth; Transpose ±12 semitones.
Нижний редактор: GATE / ACC / VELOCITY / LENGTH. MOD1–MOD4 выбираются отдельно.
FILL 64 повторяет текущий паттерн до 64 шагов.
Tie отображается как продолжение note block.

SONG / LIVE
SONG: сетка 64 позиций в утвержденной геометрии — 4 колонки x 16 строк, горизонтальные ячейки.
TEMPO, LENGTH 1–64, Play/Stop, Copy/Paste/Clear, Save/Load Song.
TRANSPOSE в SONG отсутствует — проверено на устройстве.
Песни хранятся по умолчанию:
Documents\IK Multimedia\UNO Synth Pro Editor\Song
LIVE использует ту же сетку 4x16. Слева — список сохраненных песен, ячейки — быстрый доступ к песням.

LIBRARY
Локальная библиотека не ограничена 256 пресетами и поддерживает категории/теги/поиск на стороне редактора.
Hardware Presets справа — только 1–256 и имя: категории/теги в UNO не выдумываются.
PREVIEW — отдельный чекбокс. Без безопасной ссылки на аппаратный preset локальный JSON не отправляется в UNO автоматически.

SETTINGS
MIDI IN / OUT; MIDI CONTROLLER; MIDI IN CHANNEL OMNI/1–16; MIDI OUT CHANNEL 1–16;
MIDI CLOCK SEND Off/MIDI/CV Sync; SYNC RECEIVE Internal/External/USB/CV Sync;
SOFT THRU; PR CHANGE; MIDI INTERFACE; KNOB BEHAVIOR; PITCH BEND RANGE 1–12 (default 2); MASTER TUNING ±50 cents.
Все параметры SETTINGS выбираются через выпадающие списки. Выбор MIDI CONTROLLER только меняет настройку; порт открывается после APPLY. MIDI-порты кэшируются и не опрашиваются при каждой перерисовке.

ПРОТОКОЛ / БЕЗОПАСНОСТЬ
Подтвержденный READ request:
F0 00 21 1A 02 03 37 00 00 F7
0x37 response наблюдался длиной 309 bytes.
Подтвержденные Sequencer поля: Direction offset 219 mask 0x30; Tie offset 220 mask 0x10; Gate offsets 220/221; Accent offset 223.
Подтвержденный ARP SysEx: command 0x3C subcommands Direction/Octaves.
CC map включен только для известных CC из наших тестов/мануала.

ВАЖНО: permanent bulk preset write через command 0x28 НЕ отправляется.
STORE / SEND / DEPLOY TO UNO оставлены в интерфейсе, но безопасно заблокированы до полной проверки формата 0x28.
Это сделано специально, чтобы не стереть/испортить секвенцию или preset data.


Current build: v1.17 — Filter MIDI confirmed mappings + modulation/time animation + numeric direct entry.
