import os
import time
import random
import re
from lib.data.config import COLORS, USER_SESSIONS, MAX_EMAILS_PER_USER
from lib.func.security import detect_dev_number, show_dev_protection


def get_user_session():

    session_id = str(random.randint(1000, 9999))
    if session_id not in USER_SESSIONS:
        USER_SESSIONS[session_id] = {
            'email_count': 0,
            'start_time': time.time(),
            'last_activity': time.time()
        }
    return session_id


def check_rate_limit(session_id):

    session = USER_SESSIONS.get(session_id)
    if not session:
        return True
    
    if time.time() - session['start_time'] > 86400:
        session['email_count'] = 0
        session['start_time'] = time.time()
    
    if session['email_count'] >= MAX_EMAILS_PER_USER:
        print(f"{COLORS['R']}🚫 Daily limit reached! Try again after 24 hours.")
        return False
    
    return True


def update_email_count(session_id, count):

    if session_id in USER_SESSIONS:
        USER_SESSIONS[session_id]['email_count'] += count
        USER_SESSIONS[session_id]['last_activity'] = time.time()


def format_phone_number(number):

    if detect_dev_number(number):
        show_dev_protection()
    
    cleaned = re.sub(r'[^\d+]', '', number)
    if cleaned.startswith('0'):
        cleaned = cleaned[1:]
    if not cleaned.startswith('92'):
        if cleaned.startswith('+92'):
            cleaned = cleaned[1:]
        elif len(cleaned) == 9:
            cleaned = '92' + cleaned
        else:
            cleaned = '92' + cleaned
    return '+' + cleaned


def format_name(name):

    return ' '.join(word.capitalize() for word in name.split())


def inc(text, color='W', delay=0.02):

    for char in text:
        print(COLORS[color] + char, end='', flush=True)
        time.sleep(delay)
    print()


def show_banner():
    os.system("clear")
    print(f"{COLORS['C']}="*50)
    inc(" 🔥 MA LEGEND 9T9 BANING TOOL 🔥 ", 'R')
    inc(" ⚡ MULTI-USER SECURE SYSTEM ⚡ ", 'G')
    inc(" 🛡️  DEVELOPER PROTECTION ACTIVE 🛡️ ", 'Y')
    print(f"{COLORS['C']}="*50)


def run_once(func):
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'has_run'):
            func(*args, **kwargs)
            wrapper.has_run = True
    return wrapper
