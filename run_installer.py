from pywinauto.application import Application
import os

# Note: You must open the terminal window in administrator mode in order for this script to be able to run the installer.
installer_path = input("Enter the path to the installer: ")
installer_path = installer_path.strip('""')
current_user = os.getlogin()
install_path = f"C:/Users/{current_user}/Desktop/FSS_Tested"

app = Application(backend="win32").start(installer_path)
install_dialog = app.InstallDialog
install_dialog.wait('ready', timeout=30)  # Wait for the dialog to be ready (doesn't seem to be working)

# The script is finishing before we can enter keys...
install_dialog.type_keys(install_path)
