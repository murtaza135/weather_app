from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
import traceback
import sys


class WorkerSignals(QtCore.QObject):
    '''
    Defines the signals available from a running worker thread:
    
    error
        `tuple` (exctype, value, traceback.format_exc() )
    
    result
        `object` data returned from processing, anything

    '''
    started = QtCore.Signal()
    finished = QtCore.Signal()
    error = QtCore.Signal(tuple)
    result = QtCore.Signal(object)


class Worker(QtCore.QRunnable):

    def __init__(self, function, *args, **kwargs):
        super().__init__()

        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()    

    @QtCore.Slot()
    def run(self):
        try:
            self.signals.started.emit()
            result = self.function(*self.args, **self.kwargs)
        except:
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()