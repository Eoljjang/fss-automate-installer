from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto.controls.win32_controls import ButtonWrapper
import time

# Here's a path: "C:\Users\nathan_pulsemedica\Downloads\FSS-Setup-v1.2.0.386.exe"
# Here's another path: "C:\Users\nathan_pulsemedica\Downloads\FSS-Setup-v1.2.0.383.exe"
# Notes:
# - Installing to the same path will automatically delete the old version.
# - You must have VSCode / terminal open in admin mode.

# Paths:
installer_path = input("Enter the path to the installer: ")
installer_path = installer_path.strip('""')
install_path = "C:\FSS_Tested"

# Open the installer
app = Application(backend="win32").start(installer_path)
main_window = app.window()
time.sleep(5) # Make sure the main window is ready first.

# Enter path to install at.
main_window.set_focus()
send_keys(install_path)

# Click the "install" button
main_window.next_button.click();

# Check the "Run Auto Configuration" toggle. Wait for install to finish.
time.sleep(12)
checkbox = ButtonWrapper(main_window.TCheckBox.wrapper_object())
checkbox.click()

# Click the "finish" button.
time.sleep(2)
main_window.finish_button.click()
