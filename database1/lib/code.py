import os
import time
from lib.data.config import COLORS
from lib.func.utils import show_banner, inc

def buy_code(session_id):
    while True:
        os.system('clear')
        show_banner()
        print()
        inc("   GET TOOL SOURCE CODES - FREE OF COURSE", 'G')
        inc("   GET PREMIUM WA-BAN TOOL SOURCE CODE", 'Y')
        inc("   Edit As You Want, Change Links & Reports Do Whatever You Want And Make Tool According To Your Ideas ", 'W')
        print()
        inc("   [1] GET TOOL SC CODES", 'C')
        inc("   [0] BACK TO MAIN MENU", 'R')
        print()
        inc(" SELECT OPTION (0-1):", 'W')
        choice = input(" --> ").strip()
        
        if choice == "0":
            return
        elif choice == "1":
            contact_methods(session_id)
        else:
            print(f"{COLORS['R']}❌ Invalid selection!")
            time.sleep(2)

def contact_methods(session_id):
    while True:
        os.system('clear')
        show_banner()
        print()
        inc("   CONTACT TO BUY SOURCE CODE", 'G')
        inc("   Price: PKR 1000 Only", 'Y')
        print()
        inc("   [1] GET VIA WHATSAPP", 'M')
        inc("   [2] GET VIA TELEGRAM", 'C')
        inc("   [0] BACK TO MAIN MENU", 'R')
        print()
        inc(" SELECT OPTION (0-2):", 'W')
        choice = input(" --> ").strip()
        
        if choice == "0":
            return
        elif choice == "1":
            open_wa()
        elif choice == "2":
            open_tg()
        else:
            print(f"{COLORS['R']}❌ Invalid selection!")
            time.sleep(2)

def open_wa():
    os.system('clear')
    show_banner()
    print()
    inc("   📸 OPENING WHATSAPP...", 'M')
    time.sleep(1)
    
    # Open Instagram DM directly
    os.system('am start -a android.intent.action.VIEW -d "https://chat.whatsapp.com/BytdsR5UKui7AjTm7nu4jI"')
    
    print(f"{COLORS['G']}✅ Whatsapp Opened!")
    time.sleep(2)

def open_tg():
    os.system('clear')
    show_banner()
    print()
    inc("   💬 OPENING TELEGRAM...", 'C')
    time.sleep(1)
    
    # Open Telegram DM directly
    os.system('am start -a android.intent.action.VIEW -d "https://t.me/legendmoods"')
    
    print(f"{COLORS['G']}✅ TELEGRAM OPENED!")
    time.sleep(2)
