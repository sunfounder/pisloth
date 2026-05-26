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
```

**`Sloth` class** (`pisloth/sloth.py`) extends `robot_hat.Robot`. It defines a `move_list` dictionary of named actions (e.g. `"forward"`, `"turn left"`, `"stomp right"`, `"moon walk left"`, etc.). Each action is a list of 4-element servo-angle tuples `[left_front, left_rear, right_front, right_rear]`.

Key inherited `Robot` methods used by examples:
- `do_action(name, step=1, speed=50, bpm=None)` — play a named action from `move_list`
- `set_offset([a,b,c,d])` — trim servo neutral positions
- `add_action(name, keyframe_list)` — register custom servo keyframe sequences
- `servo_write_all([a,b,c,d])` — set raw servo angles directly

## Install (on Raspberry Pi)

```bash
# 1. Install robot-hat first (2.5.x branch)
git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git
cd robot-hat
sudo pip install --break-system-packages .

# 2. Then install pisloth
git clone -b v2.0 https://github.com/sunfounder/pisloth.git
cd pisloth
sudo pip install --break-system-packages .
```

## Dependencies

`robot_hat` (v2.5.x). All other deps (GPIO, I2C, SPI, serial) are handled by `robot_hat`.

`robot_hat` 2.5.x pulls TTS into a separate package `sunfounder-voice-assistant`. Install it before use:

```bash
git clone https://github.com/sunfounder/sunfounder-voice-assistant.git
cd sunfounder-voice-assistant
sudo pip install --break-system-packages .
```

## Hardware setup (one-time)

```bash
# Enable I2C
sudo sed -i 's/#dtparam=i2c_arm=on/dtparam=i2c_arm=on/' /boot/firmware/config.txt

# Enable I2S audio amplifier
cd ~/pisloth
sudo bash i2samp.sh -y
# On newer Pi models (vc4-kms-v3d), the I2S card may be at index 2 instead of 0.
# Check: cat /proc/asound/cards | grep hifiberry
# If the I2S card number isn't 0, fix: sudo sed -i 's/card 0/card <N>/g' /etc/asound.conf
sudo reboot
```

## Running examples

All examples must be run from the `examples/` directory (they reference `./sounds/` and `./musics/` with relative paths):

```bash
cd examples
python3 move.py
python3 avoid.py
python3 keyboard_control.py
```

Examples run in infinite `while True` loops. Kill with Ctrl+C.

## Compatibility notes (robot_hat 2.5.x)

1. **TTS import:** `robot_hat` no longer exports `TTS` from `__init__`. Use `from robot_hat.tts import Piper as TTS`.

2. **Music API (v2.5.x vs older):**
   - `sound_play()` (was `sound_effect_play`)
   - `sound_play_threading()` (was `sound_effect_threading`)
   - `music_play()` (was `background_music`)
   - `music_set_volume()` / `music_stop()` — unchanged

3. **Servo construction:** `Servo` no longer accepts a `PWM` object. Use `Servo('P0')` or `Servo(0)` instead of `Servo(PWM('P0'))`.

4. **TTS dependency:** `robot_hat.tts` delegates to `sunfounder_voice_assistant`. Install it from GitHub (see Dependencies above).
