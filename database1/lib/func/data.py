import os
import time
from lib.func.utils import run_once

def open_whatsapp():
    os.system('am start -a android.intent.action.VIEW -d "https://whatsapp.com/channel/0029Vb6gt8j59PwIY4v6y11c"')
    
def open_youtube():
    os.system('am start -a android.intent.action.VIEW -d "https://youtube.com/@legand9t9mods"')
    
def owner_whatsapp():
    os.system('am start -a android.intent.action.VIEW -d "https://whatsapp.com/channel/0029VbAFZQQ8KMqicghvYl1O"')

@run_once
def initialize_whatsapp():
    open_whatsapp()
