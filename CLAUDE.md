# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

SunFounder PiSloth v2.0 — a biped robot kit for Raspberry Pi with 4 servo joints and an ultrasonic sensor. This repo contains the `pisloth` Python package and example scripts.

The robot hardware uses a **Robot HAT** board. The `pisloth` library depends on `robot_hat`, which must be installed first.

## Architecture

```
pisloth/
  __init__.py    # Exports Sloth class
  sloth.py       # Sloth(Robot) — all movement actions defined here
examples/        # Runnable demo scripts
  sounds/        # WAV sound effects
  musics/        # MP3 background music
i2samp.sh        # I2S audio amplifier setup script (Adafruit-based)
show             # License display script (Python 2, needs fixing)
```

**`Sloth` class** (`pisloth/sloth.py`) extends `robot_hat.Robot`. It defines a `move_list` dictionary of named actions (e.g. `"forward"`, `"turn left"`, `"stomp right"`, `"moon walk left"`, etc.). Each action is a list of 4-element servo-angle tuples `[left_front, left_rear, right_front, right_rear]`.

Key inherited `Robot` methods used by examples:
- `do_action(name, step=1, speed=50, bpm=None)` — play a named action from `move_list`
- `set_offset([a,b,c,d])` — trim servo neutral positions
- `add_action(name, keyframe_list)` — register custom servo keyframe sequences
- `servo_write_all([a,b,c,d])` — set raw servo angles directly

## Install (on Raspberry Pi)

```bash
# 1. Install robot-hat first
git clone https://github.com/sunfounder/robot-hat.git
cd robot-hat
sudo python3 setup.py install

# 2. Then install pisloth
git clone -b v2.0 https://github.com/sunfounder/pisloth.git
cd pisloth
sudo python3 setup.py install
```

Dependencies declared in `setup.py`: `RPi.GPIO`, `smbus`, `spidev`, `pyserial`.

## Running examples

All examples must be run from the `examples/` directory (they reference `./sounds/` and `./musics/` with relative paths):

```bash
cd examples
python3 move.py
python3 avoid.py
python3 keyboard_control.py
```

Examples run in infinite `while True` loops. Kill with Ctrl+C.

## Known issues with current robot_hat (v2.5+)

1. **`from robot_hat import TTS` is broken.** The `robot_hat.tts` module exists but is not re-exported in `robot_hat.__init__`. Use `from robot_hat.tts import Piper as TTS` instead.

2. **Music method names changed.** `robot_hat.Music` no longer has `sound_effect_play` / `sound_effect_threading` / `background_music`. The current API is:
   - `sound_play(file, volume)` (was `sound_effect_play`)
   - `sound_play_threading(file, volume)` (was `sound_effect_threading`)
   - `music_play(file)` (was `background_music`)
   - `music_set_volume(vol)` — unchanged
   - `music_stop()` — unchanged

3. **`show` script is Python 2** — uses `print` statements without parentheses. Fails on Python 3 with `SyntaxError`.

4. **`i2samp.sh` is self-duplicated** — the script content appears concatenated twice (around line 521). The second copy references outdated `/boot/config.txt` paths instead of `/boot/firmware/config.txt`.
