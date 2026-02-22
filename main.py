from pywinauto import Application
from pywinauto import mouse
import datetime
import time

TITLE="Camera"
ACTION_INTERVAL = 897
CHECK_INTERVAL = 15

last_run = datetime.datetime.now()

try:
    while True:
        now = datetime.datetime.now()
        elapsed = (now - last_run).total_seconds()
        print(f"{now.strftime('%H:%M:%S')}\t{elapsed:.1f}/{ACTION_INTERVAL}s elapsed")

        if elapsed >= ACTION_INTERVAL:
            app = Application().connect(title=TITLE)
            dlg = app.window(title=TITLE)
            dlg.set_focus()

            time.sleep(3)
            mouse.click(coords=(1850, 550))
            print(f"{now.strftime('%H:%M:%S')}\tTRIGGERED")
            
            last_run = now
        
        time.sleep(CHECK_INTERVAL)
except KeyboardInterrupt:
    print("\nScript stopped.")
