import time
from pathlib import Path

class Utilities:
    def __init__(self, app_name="BUWDA", app_full_name="Bucci Unified Weather Database Application"):
        self.app_name = app_name
        self.app_full_name = app_full_name

    def wait(self, x):
        time.sleep(x)

    def iterate(self, bdel: int, tdel: float, *str: any):
        self.wait(bdel)
        for char in str:
            print(char, end='', flush=True)
            self.wait(tdel)
        print()
    
    def check_icons(self, folder: Path):
        icons = ['sun', 'cloudy', 'rain', 'thunderstorm', 'snow', 'foggy', 'windy', 'light_cloudy', 'hail']
        existing_icons = [icon.stem for icon in folder.glob("*.png")]
        missing_icons = [icon for icon in icons if icon not in existing_icons]

        if missing_icons:
            return