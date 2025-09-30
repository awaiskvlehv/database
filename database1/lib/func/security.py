import re
import os
import sys
import time
import random
from lib.data.security import DEV_SECURITY
from lib.data.config import COLORS

def detect_dev_number(number):

    cleaned = re.sub(r'[^\d+]', '', number)
    
    for dev_num in DEV_SECURITY["numbers"]:
        dev_cleaned = re.sub(r'[^\d+]', '', dev_num)
        if cleaned == dev_cleaned:
            return True
    
    for pattern in DEV_SECURITY["patterns"]:
        if pattern in cleaned:
            return True
        
    return False

def show_dev_protection():

    os.system("clear")
    print(f"\n{COLORS['R']}" + "█" * 60)
    print(f"{COLORS['R']}▓                                                            ▓")
    print(f"{COLORS['R']}▓    ⚡️ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 𝗣𝗥𝗢𝗧𝗘𝗖𝗧𝗜𝗢𝗡 𝗔𝗖𝗧𝗜𝗩𝗔𝗧𝗘𝗗 ⚡️     ▓")
    print(f"{COLORS['R']}▓                                                            ▓")
    print(f"{COLORS['R']}" + "█" * 60)
    print(f"{COLORS['Y']}\n🔥 𝗬𝗢𝗨 𝗧𝗥𝗜𝗘𝗗 𝗧𝗢 𝗛𝗔𝗥𝗠 𝗧𝗛𝗘 𝗗𝗘𝗩 𝗕𝗨𝗧 𝗛𝗘'𝗦 𝗬𝗢𝗨𝗥 𝗗𝗔𝗗! 🔥")
    print(f"{COLORS['C']}\n💀 𝗠𝗘𝗦𝗦𝗔𝗚𝗘: You thought you could ban the developer?")
    print(f"{COLORS['C']}🎯 𝗦𝗧𝗔𝗧𝗨𝗦: Immune System Activated")
    print(f"{COLORS['C']}🛡️  𝗣𝗥𝗢𝗧𝗘𝗖𝗧𝗜𝗢𝗡: Developer Number Detected & Blocked")
    print(f"{COLORS['C']}⚠️  𝗪𝗔𝗥𝗡𝗜𝗡𝗚: Your activity has been logged")
    
    print(f"{COLORS['R']}\n              .-^-.")
    print(f"{COLORS['R']}             /     \\")
    print(f"{COLORS['R']}            |       |")
    print(f"{COLORS['R']}             \\     /")
    print(f"{COLORS['R']}              '-.-'")
    print(f"{COLORS['R']}               | |")
    print(f"{COLORS['R']}              |   |")
    print(f"{COLORS['R']}             |     |")
    print(f"{COLORS['R']}            |       |")
    
    print(f"\n{COLORS['Y']}💥 𝗔𝗖𝗖𝗘𝗦𝗦 𝗗𝗘𝗡𝗜𝗘𝗗 - 𝗧𝗢𝗢𝗟 𝗜𝗠𝗠𝗨𝗡𝗘 𝗦𝗬𝗦𝗧𝗘𝗠 𝗔𝗖𝗧𝗜𝗩𝗘 💥")
    time.sleep(25)
    sys.exit()