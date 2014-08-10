import os
from pyqode.qt import QT_API
from pyqode.qt import PYQT5_API
from pyqode.qt import PYQT4_API


if os.environ[QT_API] == PYQT5_API:
    from PyQt5.QtDesigner import *
elif os.environ[QT_API] == PYQT4_API:
    from PyQt4.QtDesigner import *
