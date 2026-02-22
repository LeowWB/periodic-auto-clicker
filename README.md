# periodic-auto-clicker

Script to automate periodic clicking, at a specified location on the screen, in a specified application window.

## Usage

Open `main.py` and set the variables. Open the target application as a window and **keep it open**. Then `python main.py`.

Variables:
* `WINDOW_TITLE` - target application where the clicks will be performed. Set to the name of the open window of the target application.
* `CLICK_INTERVAL` - seconds to wait between successive clicks.
* `SWITCH_DELAY` - after switching to target application, time to wait before clicking. Allows the target application to buffer up after being in the background.
* `CLICK_COORDS` - location to click, in screen coordinates (same coordinate set as your screen resolution; not window coordinates).
* `CHECK_INTERVAL` - how frequently to check the time, in seconds. Lower values will conserve CPU usage but may result in slightly inaccurate timekeeping.

## Tips
* If using Windows cmd, consider disabling QuickEdit mode as it can cause the script to pause. 