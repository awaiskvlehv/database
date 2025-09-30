import time
import sys
import os
import re
from lib.data.config import COLORS, USER_SESSIONS, MAX_EMAILS_PER_USER
from lib.func.utils import show_banner, inc, format_phone_number, format_name
from lib.func.email_sender import send_report
from lib.func.data import open_whatsapp, owner_whatsapp, open_youtube, initialize_whatsapp

# Global variables for user data
user_number = ""
user_name = ""

def validate_phone_number(number):
    """Validate if input is a real phone number"""
    # Remove all non-digit characters except +
    cleaned = re.sub(r'[^\d+]', '', number)
    
    # Check if it's empty
    if not cleaned:
        return False
    
    # Check if it contains only digits and optional +
    if not re.match(r'^[\d+]+$', cleaned):
        return False
    
    # Check minimum length (at least 9 digits for international numbers)
    digits_only = re.sub(r'[^\d]', '', cleaned)
    if len(digits_only) < 9:
        return False
    
    # Check if it's a valid Pakistani number format or international
    if cleaned.startswith('+92') or cleaned.startswith('92') or cleaned.startswith('0'):
        # Pakistani number validation
        digits_only = re.sub(r'[^\d]', '', cleaned)
        if digits_only.startswith('92'):
            digits_only = digits_only[2:]  # Remove country code for length check
        
        # Pakistani numbers should be 10 digits after country code
        if len(digits_only) == 10:
            return True
    
    # International number validation (basic)
    digits_only = re.sub(r'[^\d]', '', cleaned)
    if 9 <= len(digits_only) <= 15:
        return True
    
    return False

def get_number_name(session_id):
    global user_number, user_name
    show_banner()
    print()
    
    while True:
        print(f"{COLORS['W']}📱 TARGET NUMBER : ", end='')
        raw_number = input().strip()
        
        # Check if input is empty
        if not raw_number:
            print(f"{COLORS['R']}❌ Empty input! Please enter a valid phone number.")
            continue
        
        # Check if input contains only numbers and valid characters
        if not re.match(r'^[\d+\-\s\(\)]+$', raw_number):
            print(f"{COLORS['R']}❌ Invalid characters! Only numbers, +, -, (, ) and spaces allowed.")
            continue
        
        # Validate phone number format
        if not validate_phone_number(raw_number):
            print(f"{COLORS['R']}❌ Invalid phone number format! Please enter a real phone number.")
            print(f"{COLORS['Y']}💡 Examples: +923001234567, 03001234567, 923001234567")
            continue
        
        try:
            user_number = format_phone_number(raw_number)
            print(f"{COLORS['G']}   ✅ Valid Number | Formatted: {user_number}")
            break
        except Exception as e:
            print(f"{COLORS['R']}❌ Error processing number: {e}")
            continue
    
    print()
    
    while True:
        print(f"{COLORS['W']}👤 TARGET NAME : ", end='')
        raw_name = input().strip()
        
        # Validate name
        if not raw_name:
            print(f"{COLORS['R']}❌ Name cannot be empty!")
            continue
        
        # Check if name contains only letters and spaces
        if not re.match(r'^[a-zA-Z\s]+$', raw_name):
            print(f"{COLORS['R']}❌ Invalid name! Only letters and spaces allowed.")
            continue
        
        # Check minimum name length
        if len(raw_name.strip()) < 2:
            print(f"{COLORS['R']}❌ Name too short! Minimum 2 characters required.")
            continue
        
        user_name = format_name(raw_name)
        print(f"{COLORS['G']}   ✅ Valid Name | Formatted: {user_name}")
        break
    
    if user_number and user_name:
        print(f"\n{COLORS['G']}✅ Data saved successfully! | Daily limit: {MAX_EMAILS_PER_USER} emails")
        time.sleep(2)
        ban_menu(session_id)
    else:
        print(f"{COLORS['R']}❌ Number and Name required!")
        time.sleep(2)
        get_number_name(session_id)

def ban_menu(session_id):
    global user_number, user_name
    show_banner()
    print()
    
    remaining_emails = MAX_EMAILS_PER_USER - USER_SESSIONS[session_id]['email_count']
    print(f"{COLORS['Y']}📊 Emails remaining today: {remaining_emails}")
    print(f"{COLORS['C']}📱 Target Number: {user_number}")
    print(f"{COLORS['C']}👤 Target Name: {user_name}")
    print()
    
    inc("   [1]  BAN BASE " , 'Y')
    inc("   [2]  BAN HIGH " , 'Y')
    inc("   [3]  BAN GROK " , 'Y')
    inc("   [4]  BAN HARD " , 'Y')
    inc("   [5]  BAN NOVA " , 'Y')
    inc("   [6]  BAN WAVE " , 'Y')
    inc("   [7]  BAN PREM " , 'Y')
    inc("   [8]  BAN VOID " , 'Y')
    inc("   [9]  BAN VVIP " , 'Y')
    inc("   [0]  MAIN MENU" , 'R')
    print()
    inc(" SELECT REPORT TYPE (0-9):" , 'W')
    choice = input(" --> ").strip()
    
    if choice == "0":
        main_menu(session_id)
    elif choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        if remaining_emails >= 5:
            print(f"\n{COLORS['Y']}🚀 Sending report type {choice}...")
            send_report(choice, session_id, user_number, user_name)
        else:
            print(f"{COLORS['R']}❌ Not enough email quota! Need 5, have {remaining_emails}")
        print(f"{COLORS['C']}\nPress Enter to continue...")
        input()
        ban_menu(session_id)
    else:
        print(f"{COLORS['R']}❌ Invalid selection!")
        time.sleep(2)
        ban_menu(session_id)

def developer_channels(session_id):
    show_banner()
    print()
    inc("   [1]  DEV - WHATSAPP" , 'C')
    inc("   [2]  OWNER YOUTUBE" , 'R')
    inc("   [3]  OWNER WHATSAPP" , 'G')
    inc("   [4]  BACK TO MAIN MENU" , 'M')
    print()
    inc(" SELECT OPTION (1-4):" , 'W')
    choice = input(" --> ").strip()

    if choice == "1":
        open_whatsapp()
        print(f"{COLORS['G']}📱 Opening Developer WhatsApp Channel...")
        time.sleep(2)
        developer_channels(session_id)
    elif choice == "2":
        open_youtube()
        print(f"{COLORS['G']}📢 Opening YouTube...")
        time.sleep(2)
        developer_channels(session_id)
    elif choice == "3":
        owner_whatsapp()
        print(f"{COLORS['G']}🎥 Opening Owner Whatsapp Channel...")
        time.sleep(2)
        developer_channels(session_id)
    elif choice == "4":
        main_menu(session_id)
    else:
        print(f"{COLORS['R']}❌ Invalid selection!")
        time.sleep(2)
        developer_channels(session_id)

def update_tool():
    print(f"{COLORS['Y']}🔄 Checking for updates...")
    os.system("git pull")
    print(f"{COLORS['G']}✅ Tool updated!")
    time.sleep(2)

def main_menu(session_id):
    initialize_whatsapp()  # This will run only once
    show_banner()
    print()
    
    # Show user stats
    session_data = USER_SESSIONS.get(session_id, {})
    email_count = session_data.get('email_count', 0)
    remaining = MAX_EMAILS_PER_USER - email_count
    
    print(f"{COLORS['G']}👤 User ID: {session_id} | 📧 Today: {email_count}/{MAX_EMAILS_PER_USER}")
    print(f"{COLORS['Y']}⏰ Reset in: {24 - int((time.time() - session_data.get('start_time', time.time())) / 3600)} hours")
    print()
    
    inc("   [1]  JOIN CHANNEL" , 'C')
    inc("   [2]  BANING MENU" , 'M')
    inc("   [3]  UPDATE TOOL" , 'G')
    inc("   [4]  EXIT TOOL" , 'R')
    print()
    inc(" SELECT OPTION (1-4):" , 'W')
    choice = input(" --> ").strip()
    
    if choice == "1":
        developer_channels(session_id)
    elif choice == "2":
        get_number_name(session_id)
    elif choice == "3":
        update_tool()
        main_menu(session_id)
    elif choice == "4":
        print(f"\n{COLORS['Y']}🙏 Thanks for using! Goodbye!")
        sys.exit()
    else:
        print(f"{COLORS['R']}❌ Invalid selection!")
        time.sleep(2)
        main_menu(session_id)
