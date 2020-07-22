import tkinter


def check():
    if not tkinter.TkVersion == 8.6:
        print("Incompatible version of tkinter version detected")
        print("You are using version:", tkinter.TkVersion)
        print("Please update your version to 8.6")
        return False

    try:
        import PIL
    except ImportError as e:
        print("You have not imported \"Pillow\" package.")
        print("Please type the command \"pip install Pillow\"")
        return False

    print("Pass dependency checking, starting gui...")
    return True
