# Import dependencies
from packages.gui import *
from packages.initCheck import check

if __name__ == '__main__':
    if check():
        startGUI()
