import wx
from threading import *

from remoteIR import remote #read data from IR receiver


# Define notification event for thread completion
EVT_RESULT_ID = wx.NewIdRef()

def evt_result(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, EVT_RESULT_ID, func)

class ResultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_RESULT_ID)
        self.data = data

# Thread class that executes processing
class WorkerThread(Thread):
    
    
    
    """Worker Thread Class."""
    def __init__(self, notify_window):
        """Init Worker Thread Class."""
        Thread.__init__(self, daemon = True)
        self._notify_window = notify_window
        self._want_abort = False
        self.receiverIR=remote()
        # This starts the thread running on creation, but you could
        # also make the GUI thread responsible for calling this
        self.start()

    def run(self):
        print("Thread running!")
        """Run Worker Thread."""
        # This is the code executing in the new thread.  You will
        # need to structure your processing so that you periodically
        # peek at the abort variable
        while self._want_abort==False:
            codigo = self.receiverIR.Getcode()
            print("IR code: "+str(codigo))
            
            if self._want_abort:
                # Use a result of None to acknowledge the abort (of
                # course you can use whatever you'd like or even
                # a separate event type)
                wx.PostEvent(self._notify_window, ResultEvent(None))
                return
            # Here's where the result would be returned (this is an
            # example fixed result of the number 10, but it could be
            # any Python object)
            wx.PostEvent(self._notify_window, ResultEvent(codigo))

    def abort(self):
        print("Thread aborted!")
        """abort worker thread."""
        # Method for use by main thread to signal an abort
        self._want_abort = 1
