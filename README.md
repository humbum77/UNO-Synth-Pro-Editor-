# UNO Synth Pro Editor

Расширенный редактор для синтезатора **IK Multimedia UNO Synth Pro** — полноэкранное десктопное приложение, которое даёт доступ ко всем параметрам синтеза с компьютера, в реальном времени по MIDI, без листания меню на самом устройстве.

Текущая версия: **v1.47**

---

## Возможности

### Редактирование звука (страница SYNTH)

- Три осциллятора: форма волны, тюнинг (±24 полутона), уровень, а также уровень шума.
- Модуляция осцилляторов: Sync 2/3, Ring Mod, FM 1→2 и 1→3.
- Два фильтра с независимыми Cutoff, Resonance, Env Amount и Key Tracking:
  - Filter 1: LP 0°, LP 180°, HP 0°, HP 180°, Bypass;
  - Filter 2: 2P/4P Series, 2P/4P Parallel, Bypass Series/Parallel;
  - Filter Spacing и Filter Link (Off / Cutoff / Cut+Res).
- Две огибающие ADSR — фильтровая (с Loop и Retrigger) и амплитудная (с Loop).
- Два LFO: форма волны (8 типов), Rate, Fade In, Sync.
- Glide, VCA, Swing, Pitch Bend Range, Master Tuning.
- Интерактивные графические экраны: форма волны осциллятора, кривая фильтра, огибающие фильтра и усилителя — редактируются мышью, все непрерывные параметры допускают и прямой числовой ввод.
- Значения отправляются в UNO Synth Pro мгновенно, по подтверждённым CC.

### Матрица модуляции

- 16 маршрутов: Source / Amount / Destination / Fade In в одной колонке.
- Полные списки источников и приёмников по официальному руководству UNO Synth Pro.
- Amount каждого слота передаётся отдельным CC (66–81).

### Эффекты

- Modulation: Chorus / Phaser / Flanger — Amount, Intensity, Rate, Chorus Mode.
- Delay: Mono / Stereo / Doubler / Ping Pong / LCR — Amount, Sync, Time, Time R, Feedback, LPF.
- Reverb: Hall / Plate / Reverse / Spring — Amount, Pre-delay, Time, Low, High, Size, Filter.
- Drive.
- Типы эффектов передаются аппаратно подтверждёнными enum-значениями, а не «сырыми» числами.

### Арпеджиатор и секвенсор (страница ARP + SEQUENCER)

- ARP: 10 режимов (UP, DOWN, U/D, UD+, D/U, DU+, RND, PLY, X2U, X2D), диапазон 1–4 октавы, Gate 0–10, Swing 50–80 %, Hold, 16 trigger-шагов в раскладке 2×8.
- Секвенсор до 64 шагов с piano-roll: до 3 нот на шаг, Tie отображается как продолжение блока ноты.
- Направление воспроизведения: Forward / Backward / Back'n'Forth, Transpose ±12 полутонов.
- Пошаговый редактор: Gate, Accent, Velocity, Length, Probability и четыре слота автоматизации MOD1–MOD4.
- FILL 64 — размножение текущего паттерна до 64 шагов.
- Программное воспроизведение: редактор сам шлёт Note On/Off с учётом Gate, Tie, Velocity, Transpose, вероятности и step-автоматизации CC.

### Библиотека пресетов (страница LIBRARY)

- Локальная библиотека без ограничения в 256 ячеек: категории, теги и поиск на стороне редактора.
- Формат пресета — `*.unosyp`, поиск идёт и по вложенным папкам-категориям.
- Импорт существующих файлов пресетов кнопкой ADD, сохранение текущего звука кнопкой SAVE.
- Отдельный список Hardware Presets 1–256 с именами — без выдуманных категорий, которых в устройстве нет.
- PREVIEW включается отдельным чекбоксом, чтобы ничего не отправлялось в синтезатор случайно.
- Двусторонняя смена номера пресета Editor ↔ UNO через Bank Select / Program Change, без эхо-отправки входящих изменений.

### Song и Live (страница SONG)

- SONG: сетка 64 позиций (4 колонки × 16 строк), Tempo, Length 1–64, Play/Stop, Copy/Paste/Clear, Save/Load.
- Песни хранятся в формате `*.unosong`.
- LIVE: та же сетка 4×16 со списком сохранённых песен слева для быстрого переключения на сцене.

### Настройки MIDI (страница SETTINGS)

- Выбор портов MIDI IN / OUT и отдельного MIDI-контроллера.
- MIDI IN Channel (OMNI / 1–16) и MIDI OUT Channel (1–16).
- MIDI Clock Send: Off / MIDI / CV Sync; Sync Receive: Internal / External / USB / CV Sync.
- Soft Thru, Program Change, MIDI Interface, Knob Behavior, Pitch Bend Range 1–12, Master Tuning ±50 центов.
- Список MIDI-портов кэшируется и не опрашивается при каждой перерисовке; порт открывается по APPLY.

### Интерфейс

- Полностью масштабируемый интерфейс с фиксированной пропорцией: стартовый размер окна подбирается по разрешению экрана.
- Экранная клавиатура (показ/скрытие кнопкой в правом верхнем углу) с PITCH, MOD и выбором октавы.
- Быстрые действия в верхней панели: RANDOM, INIT, SAVE, STORE, SETTINGS, READ.

---

## Безопасность работы с устройством

Редактор сознательно не выполняет bulk-запись пресетов (SysEx-команда `0x28`), пока её формат не подтверждён полностью, — чтобы исключить повреждение пресетов или секвенций в памяти синтезатора. Кнопки STORE / SEND / DEPLOY TO UNO присутствуют в интерфейсе, но безопасно заблокированы.

В карту протокола включены только те CC и SysEx-поля, которые подтверждены официальной MIDI-документацией или наблюдением реального обмена с устройством.

---

## Требования

- Windows — MIDI работает напрямую через системную `winmm.dll`; на других ОС приложение запускается в offline-режиме без MIDI.
- Python 3.10+
- Pillow >= 10.0

## Установка и запуск

```bash
pip install -r Docs/requirements.txt
python main.py
```

В Windows можно использовать готовые скрипты `install_dependencies.bat` и `run_editor.bat`.

## Структура проекта

| Файл | Назначение |
| --- | --- |
| `main.py` | Точка входа, настройка логирования |
| `app.py` | Интерфейс Tkinter, страницы SYNTH / ARP + SEQUENCER / LIBRARY / SONG / SETTINGS |
| `midi_interface.py` | Низкоуровневая обёртка WinMM MIDI (ctypes), в том числе SysEx |
| `midi_engine.py` | Высокоуровневый MIDI-слой: CC, Program Change, ноты, транспорт |
| `protocol_map.py` | Карта CC, SysEx-команды, enum-значения фильтров и эффектов |
| `data_model.py` | Модели данных: `Step`, `Sequence`, `Preset`, `SongSlot`, `Song` |
| `storage.py` | Чтение и запись пресетов, песен и настроек |
| `Docs/` | Changelog'и, отчёты валидации, макеты интерфейса |
| `Assets/` | Референсные изображения интерфейса |

## Данные пользователя

```
~/Documents/IK Multimedia/UNO Synth Pro/
├── *.unosyp          пресеты
├── songs/*.unosong   песни
└── settings.json     настройки
```

## Разработка

Изменения вносятся через ветки и Pull Request'ы:

```bash
git checkout -b feature/short-description
git add <файлы>
git commit -m "Short description"
git push -u origin feature/short-description
```

Релизы версий оформляются тегами (`v1.47`, `v1.48`, ...) вместо архивов.

## Правовая информация

Неофициальный проект. UNO Synth Pro и IK Multimedia — товарные знаки соответствующих правообладателей; проект с ними не связан и ими не поддерживается.
