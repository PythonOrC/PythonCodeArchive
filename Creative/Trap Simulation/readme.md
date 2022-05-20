# Trap Simulation

_**This document is not at all updated cuz me** ~~lazy~~ **busy**_

This is project is created for practicing International Trap when the user is dry firing at home. <br>
Below is the specification for the varaibles in the configuration file.<br>
This is in early development stage where bugs and inconveniences exist and might cause crashes. <br>
You are welcome to edit the code according to your preference.

## Things to note:

- Moving windows is currently very buggy. After dragging, the user need to release a target in order for the adjustment to take place.
- This goes the same for the maximize window and close window option.

---

## config.json:

- `SOUND_THRESHOLD` should be adjusted for consistency in releasing targets
- `SCREENSIZE` should be adjusted to fit the computer's screen resolution (DOES NOT WORK CURRENTLY)
- `BACKGROUND_HEIGHT` should be adjusted to better simulate the bunker
- `TARGET_SPEED` should be adjusted to better simulate the flight speed of the targets
- `ADVANCE_INFO` gives the user the option to view hidden information that would be useful for calibration
  - `"True"` to show the information
  - `"False"` to hide the information
- `REMINDER` gives the user the option to view a reminder than they can check back to [readme.md](readme.md) for all the information they need.
  - `"True"` to show the reminder
  - `"False"` to hide the reminder
