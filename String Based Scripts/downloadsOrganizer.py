from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

currentUser = "dreamdevourer"
mainDirectory = f"/Users/{currentUser}/Downloads"

jobDestinationPath = f"/Users/{currentUser}/Documents/Remotish"
personalDestinationPath = f"/Users/{currentUser}/Documents/Personal"
tmpPath = f"/Users/{currentUser}/Downloads/tmp"


class MyHandler(FileSystemEventHandler):
    print("DEBUG: You are inside the MyHandler.")

    def on_modified(self, event):
        print("DEBUG: You are inside on_modified function.")
        for fileName in os.listdir(mainDirectory):
            # if the filename starts with "job_" then move it to jobDestinationPath
            if fileName.startswith("job_") or fileName.startswith("rem_"):
                print(f"{fileName} is work asset!")
                # move files from mainDirectory to jobDestinationPath
                os.rename(f"{mainDirectory}/{fileName}",
                          f"{jobDestinationPath}/{fileName}")
                print(f"{fileName} moved to {jobDestinationPath}")

            elif fileName.startswith("per_"):
                print(f"{fileName} is a personal file!")
                # move files from mainDirectory to personalDestinationPath
                os.rename(f"{mainDirectory}/{fileName}",
                          f"{personalDestinationPath}/{fileName}")
                print(f"{fileName} moved to {personalDestinationPath}")

            elif fileName.startswith("_") or fileName.startswith("tmp_") or fileName.startswith("temp_"):
                print(f"{fileName} is a temporary file!")
                # move files from mainDirectory to tmpPath
                os.rename(f"{mainDirectory}/{fileName}",
                          f"{tmpPath}/{fileName}")
                print(f"{fileName} moved to {tmpPath}")


eventHandler = MyHandler()
observer = Observer()
observer.schedule(eventHandler, mainDirectory, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
