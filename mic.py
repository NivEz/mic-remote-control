import win32api
import win32gui

class Mic:
    def __init__(self, is_muted):
        self.is_muted = is_muted
    
    def toggle(self):
        WM_APPCOMMAND = 0x319
        APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000
        hwnd_active = win32gui.GetForegroundWindow()
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)        
        self.is_muted = not self.is_muted
