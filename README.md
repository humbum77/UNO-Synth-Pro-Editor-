# UNO Synth Pro Editor

Редактор для синтезатора IK Multimedia UNO Synth Pro: управление параметрами звука, библиотека пресетов, секвенсор и режимы Song/Live.

Текущая версия: **v1.47**

## Требования

- Windows (MIDI работает через системную `winmm.dll`; на других ОС приложение запускается в offline-режиме без MIDI)
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
| `app.py` | Интерфейс Tkinter, страницы SYNTH/SEQ/LIBRARY/SONG, обработка ввода |
| `midi_interface.py` | Низкоуровневая обёртка WinMM MIDI (ctypes), в том числе SysEx |
| `midi_engine.py` | Высокоуровневый MIDI-слой: CC, Program Change, ноты, транспорт |
| `protocol_map.py` | Карта CC, SysEx-команды, enum-значения фильтров и эффектов |
| `data_model.py` | Модели данных: `Step`, `Sequence`, `Preset`, `SongSlot`, `Song` |
| `storage.py` | Чтение и запись пресетов, песен и настроек |
| `Docs/` | Changelog'и, отчёты валидации, макеты интерфейса |
| `Assets/` | Референсные изображения интерфейса |

## Данные пользователя

Пресеты и песни сохраняются в домашнем каталоге:

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
