import os
import time
from lib.data.config import COLORS
from lib.func.utils import show_banner, inc

def buy_code(session_id):
    while True:
        os.system('clear')
        show_banner()
        print()
        inc("   BUY TOOL SOURCE CODES - PKR 1000", 'G')
        inc("   Get Premium WA-BAN Tool Source Code", 'Y')
        inc("   Edit As You Want, Change Links & Reports Do Whatever You Want And Make Tool According To Your Ideas ", 'W')
        print()
        inc("   [1] BUY TOOL SC CODES", 'C')
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
        inc("   [1] DM ON INSTAGRAM", 'M')
        inc("   [2] DM ON TELEGRAM", 'C')
        inc("   [0] BACK TO MAIN MENU", 'R')
        print()
        inc(" SELECT OPTION (0-2):", 'W')
        choice = input(" --> ").strip()
        
        if choice == "0":
            return
        elif choice == "1":
            open_instagram()
        elif choice == "2":
            open_telegram()
        else:
            print(f"{COLORS['R']}❌ Invalid selection!")
            time.sleep(2)

def open_instagram():
    os.system('clear')
    show_banner()
    print()
    inc("   📸 OPENING INSTAGRAM DM...", 'M')
    time.sleep(1)
    
    # Open Instagram DM directly
    os.system('am start -a android.intent.action.VIEW -d "https://instagram.com/_u/awsiskvlehv"')
    
    print(f"{COLORS['G']}✅ Instagram DM opened!")
    time.sleep(2)

def open_telegram():
    os.system('clear')
    show_banner()
    print()
    inc("   💬 OPENING TELEGRAM DM...", 'C')
    time.sleep(1)
    
    # Open Telegram DM directly
    os.system('am start -a android.intent.action.VIEW -d "https://t.me/awsiskvlehv"')
    
    print(f"{COLORS['G']}✅ Telegram DM opened!")
    time.sleep(2)