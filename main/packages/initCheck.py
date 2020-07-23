import tkinter
import sys

dependencyCheckPass = True


def check():
    print("Dependency check starting...")
    global dependencyCheckPass
    if not tkinter.TkVersion == 8.6:
        global dependencyCheckPass
        print("Incompatible version of tkinter version detected")
        print("You are using version:", tkinter.TkVersion)
        print("Please update your version to 8.6")
        dependencyCheckPass = False

    def tryPackage(x, y):
        try:
            module_obj = __import__(x)
            globals()[x] = module_obj
            print("Pass", y, "module checking")
        except ImportError:
            failPass()
            print("You have not download the \"" + y + "\" package.")
            print("Please type the command \"pip install " + y + "\"")

    def failPass():
        global dependencyCheckPass
        dependencyCheckPass = False

    tryPackage("PIL", "Pillow")
    tryPackage("yaml", "PyYAML")
    tryPackage("bcrypt", "bcrypt")

    if sys.platform == 'darwin':
        tryPackage("Foundation", "pyobjc")

    if dependencyCheckPass:
        from data.initConfig import init as initConfig
        if initConfig():
            print("Dependency checking passed, starting gui...")
            from packages.gui import startGUI
            startGUI()
    else:
        return False
