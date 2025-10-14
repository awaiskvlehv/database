import os
import sys
import time
import json
import re
import random
import smtplib
import requests
import subprocess
import importlib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    BLACK = '\033[90m'
    END = '\033[0m'
    BOLD = '\033[1m'

class Animations:
    @staticmethod
    def loading_animation(text, duration=3):
        chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        start_time = time.time()
        i = 0
        while time.time() - start_time < duration:
            print(f"\r{Colors.YELLOW}{Colors.BOLD}{chars[i % len(chars)]} {text}...{Colors.END}", end="", flush=True)
            time.sleep(0.1)
            i += 1
        print(f"\r{Colors.GREEN}{Colors.BOLD}✅ {text} Complete!{Colors.END}")

    @staticmethod
    def dots_animation(text, duration=2):
        dots = ""
        start_time = time.time()
        while time.time() - start_time < duration:
            for i in range(4):
                dots = "." * i
                print(f"\r{Colors.CYAN}{Colors.BOLD}{text}{dots}   {Colors.END}", end="", flush=True)
                time.sleep(0.3)
        print(f"\r{Colors.GREEN}{Colors.BOLD}✅ {text} 𝐃𝐎𝐍𝐄!{Colors.END}")

def install_package(package_name):
    """Install a Python package with loading animation"""
    try:
        Animations.loading_animation(f"𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐈𝐍𝐆 {package_name.upper()}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name], 
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        print(f"{Colors.RED}{Colors.BOLD}❌ 𝐅𝐀𝐈𝐋𝐄𝐃 𝐓𝐎 𝐈𝐍𝐒𝐓𝐀𝐋𝐋 {package_name.upper()}{Colors.END}")
        return False

def check_and_install_dependencies():
    """Check and install required dependencies"""
    required_packages = ['colorama', 'requests']
    
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"{Colors.GREEN}{Colors.BOLD}✅ {package.upper()} 𝐀𝐋𝐑𝐄𝐀𝐃𝐘 𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐄𝐃{Colors.END}")
        except ImportError:
            print(f"{Colors.YELLOW}{Colors.BOLD}📦 {package.upper()} 𝐍𝐎𝐓 𝐅𝐎𝐔𝐍𝐃, 𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐈𝐍𝐆...{Colors.END}")
            if not install_package(package):
                return False
    return True

# Check dependencies before importing colorama
if check_and_install_dependencies():
    try:
        from colorama import Fore, Style, init
        init(autoreset=True)
        
        colors = {
            'R': Fore.RED + Style.BRIGHT,
            'G': Fore.GREEN + Style.BRIGHT,
            'Y': Fore.YELLOW + Style.BRIGHT,
            'C': Fore.CYAN + Style.BRIGHT,
            'W': Fore.WHITE + Style.BRIGHT,
            'M': Fore.MAGENTA + Style.BRIGHT,
            'B': Fore.BLUE + Style.BRIGHT,
        }
    except ImportError:
        colors = {
            'R': Colors.RED + Colors.BOLD,
            'G': Colors.GREEN + Colors.BOLD,
            'Y': Colors.YELLOW + Colors.BOLD,
            'C': Colors.CYAN + Colors.BOLD,
            'W': Colors.WHITE + Colors.BOLD,
            'M': Colors.MAGENTA + Colors.BOLD,
            'B': Colors.BLUE + Colors.BOLD,
        }
else:
    print(f"{Colors.RED}{Colors.BOLD}❌ 𝐃𝐄𝐏𝐄𝐍𝐃𝐄𝐍𝐂𝐈𝐄𝐒 𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐀𝐓𝐈𝐎𝐍 𝐅𝐀𝐈𝐋𝐄𝐃. 𝐄𝐗𝐈𝐓𝐈𝐍𝐆...{Colors.END}")
    sys.exit(1)

session_id = str(int(time.time()))
user_number = ""
user_name = ""

def inc(text, color='W', delay=0.01, end='\n'):
    color_code = colors.get(color, colors['W'])
    for char in text:
        print(color_code + char, end='', flush=True)
        time.sleep(delay)
    print(end, end='')

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_date():
    now = datetime.now()
    inc(f"    ❰", 'W', end='')
    inc(f" Today It Is {now.strftime('%A %d %B %Y')}! ", 'C', end='')
    inc(f"❱", 'W')

def print_banner():
    print(f"{Colors.GREEN}{Colors.BOLD}  ║{Colors.GREEN}▒▒▒▒▒▒▒▒▒▒{Colors.GREEN}{Colors.BOLD}║")
    print(f"{Colors.GREEN}{Colors.BOLD}  ║{Colors.GREEN}▒▒▒▒▒▒▒▒▒▒{Colors.GREEN}{Colors.BOLD}║")
    print(f"{Colors.GREEN}{Colors.BOLD}  ║{Colors.GREEN}▒▒▒▒▒▒▒▒▒▒{Colors.GREEN}{Colors.BOLD}║")
    print(f"{Colors.GREEN}{Colors.BOLD}  ║{Colors.GREEN}▒▒▒▒▒▒▒▒▒▒{Colors.GREEN}{Colors.BOLD}║")
    print(f"{Colors.GREEN}{Colors.BOLD}  ║{Colors.GREEN}▒▒▒▒▒▒▒▒▒▒{Colors.GREEN}{Colors.BOLD}║")
    print(f"{Colors.GREEN}{Colors.BOLD}  ║{Colors.GREEN}▒▒▒▒▒▒▒▒▒▒{Colors.GREEN}{Colors.BOLD}║")
    print(f"{Colors.GREEN}{Colors.BOLD} ╔════════════╗")
    print(f"{Colors.CYAN}{Colors.BOLD}  𝐋𝐄𝐆𝐄𝐍𝐃 𝐌𝐎𝐃𝐒?")
    print(f"{Colors.GREEN}{Colors.BOLD} ╚════════════╝")
    print(f"{Colors.GREEN}{Colors.BOLD}  ║{Colors.WHITE}{Colors.BOLD}██████████{Colors.GREEN}{Colors.BOLD}╚╗")
    print(f"{Colors.GREEN}{Colors.BOLD}  ║{Colors.WHITE}{Colors.BOLD}██{Colors.GREEN}{Colors.BOLD}╔══╗{Colors.WHITE}{Colors.BOLD}█{Colors.GREEN}{Colors.BOLD}╔═╗{Colors.WHITE}{Colors.BOLD}█{Colors.GREEN}{Colors.BOLD}║")
    print(f"{Colors.GREEN}{Colors.BOLD}  ║{Colors.WHITE}{Colors.BOLD}██{Colors.GREEN}{Colors.BOLD}║{Colors.MAGENTA}╬{Colors.GREEN}{Colors.BOLD}╔╝{Colors.WHITE}{Colors.BOLD}█{Colors.GREEN}{Colors.BOLD}╚╗║{Colors.WHITE}{Colors.BOLD}█{Colors.GREEN}{Colors.BOLD}║")
    print(f"{Colors.GREEN}{Colors.BOLD}  ║{Colors.WHITE}{Colors.BOLD}██{Colors.GREEN}{Colors.BOLD}╚═╝{Colors.WHITE}{Colors.BOLD}█{Colors.BLACK}║{Colors.WHITE}{Colors.BOLD}█{Colors.GREEN}{Colors.BOLD}╚╝{Colors.WHITE}{Colors.BOLD}█{Colors.GREEN}{Colors.BOLD}║")
    print(f"{Colors.GREEN}{Colors.BOLD}  ╚╗{Colors.WHITE}{Colors.BOLD}█████████{Colors.GREEN}{Colors.BOLD}═╝")
    print(f"{Colors.GREEN}{Colors.BOLD}   ╚╗║{Colors.BLACK}╠╩╩╩╩╩╝")
    print(f"{Colors.GREEN}{Colors.BOLD}     ║║┈┈┈{Colors.YELLOW}{Colors.BOLD}███{Colors.WHITE}{Colors.BOLD}▐█████████{Colors.RED}▒{Colors.BLACK}.｡oO")
    print(f"{Colors.GREEN}{Colors.BOLD}     ║{Colors.WHITE}{Colors.BOLD}██{Colors.BLACK}╠╦╦╦╗")
    print(f"{Colors.GREEN}{Colors.BOLD}     ╚╗{Colors.WHITE}{Colors.BOLD}██████ ")
    print()

def show_banner():
    clear_screen()
    print_banner()
    show_date()

def open_url():
    os.system('am start -a android.intent.action.VIEW -d "https://whatsapp.com/channel/0029Vb6gt8j59PwIY4v6y11c"')

def open_group():
    os.system('am start -a android.intent.action.VIEW -d "https://chat.whatsapp.com/DYFn6RfXKWvLthxhCvweiP"')

def open_channel():
    os.system('am start -a android.intent.action.VIEW -d "https://whatsapp.com/channel/0029Vb70EaaCcW4uM9cRQm0D"')

def open_dm():
    os.system('am start -a android.intent.action.VIEW -d "https://wa.me/qr/CA4MQDCEQFGON1?text=Hello%20Sir!%20%F0%9F%91%8B%20I%20Want%20To%20Buy%20Source%20Codes%20Of%20BANING%20V3%20Termux%20Tool%20%F0%9F%94%A5"')

def share_tool():
    os.system('am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?text=%20Hello%20Buddy%20👋%20Check%20This%20Awesome%20Whatsapp%20Banning%20Tool%20V2%20🔥%0A%0Apkg%20update%20-y%0Apkg%20upgrade%20-y%0Apkg%20install%20git%20-y%0Apkg%20install%20python%20-y%0Apip%20install%20requests%20colorama%0Agit%20clone%20https://github.com/MA9t9/BANNING_TOOL.git%0Acd%20BANNING_TOOL%0Achmod%20+x%20legend9t9%0Apython%20legend9t9%0A%0AFOLLOW%20LEGEND%20MODS%0Ahttps://whatsapp.com/channel/0029Vb6gt8j59PwIY4v6y11c"')

def open_vid1():
    os.system('am start -a android.intent.action.VIEW -d "https://t.me/legendxawais/3"')

def open_vid2():
    os.system('am start -a android.intent.action.VIEW -d "https://youtube.com/@legand9t9mods?si=GxReUW4bxUOzGeZp"')

def run_once(func):
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'has_run'):
            result = func(*args, **kwargs)
            wrapper.has_run = True
            return result
    return wrapper

@run_once
def redirect():
    open_url()

class ProxyManager:
    def __init__(self):
        self.proxy_file = "proxy.txt"
        self.proxies = []
        self.load_proxies()
    
    def load_proxies(self):
        if os.path.exists(self.proxy_file):
            try:
                with open(self.proxy_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and ':' in line:
                            self.proxies.append(line)
                
                print(f"{colors['G']}✅ 𝐋𝐎𝐀𝐃𝐄𝐃 {len(self.proxies)} PROXIES{Colors.END}")
                
            except Exception as e:
                print(f"{colors['R']}❌ 𝐄𝐑𝐑𝐎𝐑 𝐋𝐎𝐀𝐃𝐈𝐍𝐆 𝐏𝐑𝐎𝐗𝐈𝐄𝐒: {e}{Colors.END}")
                self.proxies = []
        else:
            print(f"{colors['Y']}⚠️ 𝐏𝐑𝐎𝐗𝐘 𝐅𝐈𝐋𝐄 𝐍𝐎𝐓 𝐅𝐎𝐔𝐍𝐃, 𝐔𝐒𝐈𝐍𝐆 𝐃𝐈𝐑𝐄𝐂𝐓 𝐂𝐎𝐍𝐍𝐄𝐂𝐓𝐈𝐎𝐍{Colors.END}")
            self.proxies = []
    
    def get_random_proxy(self):
        if self.proxies:
            proxy = random.choice(self.proxies)
            if not proxy.startswith(('http://', 'https://')):
                proxy = f"http://{proxy}"
            return proxy
        return None

proxy_manager = ProxyManager()

class UserManager:
    def __init__(self):
        self.user_file = "user.json"
        self.setup_complete = False
        self.user_data = {}
        
    def load_user_data(self):
        if os.path.exists(self.user_file):
            try:
                with open(self.user_file, 'r') as f:
                    self.user_data = json.load(f)
                self.setup_complete = True
                return True
            except Exception as e:
                print(f"{colors['R']}❌ 𝐄𝐑𝐑𝐎𝐑 𝐋𝐎𝐀𝐃𝐈𝐍𝐆 𝐔𝐒𝐄𝐑 𝐃𝐀𝐓𝐀: {e}{Colors.END}")
                return False
        return False
    
    def save_user_data(self):
        try:
            with open(self.user_file, 'w') as f:
                json.dump(self.user_data, f, indent=4)
            return True
        except Exception as e:
            print(f"{colors['R']}❌ 𝐄𝐑𝐑𝐎𝐑 𝐒𝐀𝐕𝐈𝐍𝐆 𝐔𝐒𝐄𝐑 𝐃𝐀𝐓𝐀: {e}{Colors.END}")
            return False
    
    def get_user_credentials(self):
        if self.setup_complete and self.user_data:
            return self.user_data
        return None
    
    def is_valid_gmail(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
        return bool(re.match(pattern, email))
    
    def is_valid_app_password(self, password):
        if len(password) != 16:
            return False
        return password.isalnum()
    
    def setup_user(self):
        while True:
            inc("\n\n   ╭─❰", 'C', end='')
            inc(" 𝐈𝐍𝐏𝐔𝐓 𝐘𝐎𝐔𝐑 𝐆𝐌𝐀𝐈𝐋 𝐀𝐃𝐃𝐑𝐄𝐒𝐒 ", 'G', end='')
            inc("❱", 'C')
            inc("   │ ", 'C', end='')
            inc(" ━━━━━━━━━━━━━━━━━━━━━━━━━━", 'B')
            inc("   ╰━━━━┈⊷ ", 'C', end='')
            gmail = input().strip().lower()
            
            if not gmail:
                clear_screen()
                print()
                print(f"\n{colors['R']}  ❌ 𝐆𝐌𝐀𝐈𝐋 𝐂𝐀𝐍𝐍𝐎𝐓 𝐁𝐄 𝐄𝐌𝐏𝐓𝐘!{Colors.END}")
                continue
            
            if not self.is_valid_gmail(gmail):
                clear_screen()
                print()
                print(f"\n{colors['R']}  ❌ 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐆𝐌𝐀𝐈𝐋 FORMAT! INPUT AGAIN{Colors.END}")
                print(f"{colors['Y']}  📧 𝐄𝐗𝐀𝐌𝐏𝐋𝐄 : username@gmail.com{Colors.END}")
                continue
            
            print()
            print(f"\n{colors['Y']}  ✅ 𝐂𝐎𝐍𝐅𝐈𝐑𝐌 𝐆𝐌𝐀𝐈𝐋  {colors['W']}{gmail}{Colors.END}")
            print(f"{colors['C']}  ❓ 𝐈𝐒 𝐓𝐇𝐈𝐒 𝐂𝐎𝐑𝐑𝐄𝐂𝐓? (𝐘/𝐍): ", end="")
            confirm = input().strip().lower()
            
            if confirm in ['y', 'yes', '']:
                clear_screen()
                break
            else:
                clear_screen()
                print()
                print(f"{colors['Y']}  🔄 𝐋𝐄𝐓𝐒 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍...{Colors.END}")
        
        while True:
            inc("\n\n   ╭─❰", 'C', end='')
            inc(" 𝐈𝐍𝐏𝐔𝐓 𝐘𝐎𝐔𝐑 𝐀𝐏𝐏 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 ", 'G', end='')
            inc("❱", 'C')
            inc("   │ ", 'C', end='')
            inc(" ━━━━━━━━━━━━━━━━━━━━━━━━━", 'B')
            inc("   ╰━━━━┈⊷ ", 'C', end='')
            app_password = input().strip()
            
            if not app_password:
                clear_screen()
                print()
                print(f"\n{colors['R']}  ❌ 𝐀𝐏𝐏 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 𝐂𝐀𝐍𝐍𝐎𝐓 𝐁𝐄 𝐄𝐌𝐏𝐓𝐘!{Colors.END}")
                continue
            
            if not self.is_valid_app_password(app_password):
                clear_screen()
                print()
                print(f"{colors['R']}  ❌ 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐀𝐏𝐏 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 𝐅𝐎𝐑𝐌𝐀𝐓!{Colors.END}")
                print(f"{colors['Y']}  🔑 𝐌𝐔𝐒𝐓 𝐁𝐄 𝐄𝐗𝐀𝐂𝐓𝐋𝐘 16 𝐂𝐇𝐀𝐑𝐀𝐂𝐓𝐄𝐑𝐒 {Colors.END}")
                print(f"{colors['Y']}  📝 𝐄𝐗𝐀𝐌𝐏𝐋𝐄 : ABCD EFGH 1234 5678{Colors.END}")
                continue
            
            masked_password = app_password[:4] + "*" * 8 + app_password[-4:]
            print()
            print(f"\n{colors['Y']}  ✅ 𝐂𝐎𝐍𝐅𝐈𝐑𝐌 𝐀𝐏𝐏 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃  {colors['W']}{masked_password}{Colors.END}")
            print(f"{colors['C']}  ❓ 𝐈𝐒 𝐓𝐇𝐈𝐒 𝐂𝐎𝐑𝐑𝐄𝐂𝐓? (𝐘/𝐍): ", end="")
            confirm = input().strip().lower()
            
            if confirm in ['y', 'yes', '']:
                self.user_data = {
                    'developer': 'legend-x-awais',
                    'gmail': gmail,
                    'app_password': app_password,
                    'setup_complete': True,
                    'tool_version': 'vvip',
                    'access_type': 'unlimited',
                    'setup_date': self.get_current_timestamp(),
                    'usage_count': 0,
                    'last_used': self.get_current_timestamp()
                }
                if self.save_user_data():
                    self.setup_complete = True
                    print(f"\n{colors['G']}  ✅ 𝐔𝐒𝐄𝐑 𝐃𝐀𝐓𝐀 𝐒𝐀𝐕𝐄𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘!{Colors.END}")
                break
            else:
                clear_screen()
                print()
                print(f"{colors['Y']}  🔄 𝐋𝐄𝐓𝐒 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍...{Colors.END}")
        
        return self.setup_complete
    
    def update_usage_stats(self):
        if self.user_data:
            self.user_data["usage_count"] = self.user_data.get("usage_count", 0) + 1
            self.user_data["last_used"] = self.get_current_timestamp()
            self.save_user_data()
    
    def get_current_timestamp(self):
        return datetime.now().isoformat()
    
    def check_and_setup(self):
        clear_screen()
        print(f"\n{colors['M']}   🔍 𝐂𝐇𝐄𝐂𝐊𝐈𝐍𝐆 𝐔𝐒𝐄𝐑 𝐂𝐎𝐍𝐅𝐈𝐆𝐔𝐑𝐀𝐓𝐈𝐎𝐍...{Colors.END}")
        
        if self.load_user_data():
            print(f"{colors['G']}   ✅ 𝐔𝐒𝐄𝐑 𝐂𝐎𝐍𝐅𝐈𝐆𝐔𝐑𝐀𝐓𝐈𝐎𝐍 𝐅𝐎𝐔𝐍𝐃!{Colors.END}")
            
            print(f"\n{colors['C']}❓ 𝐔𝐒𝐄 𝐄𝐗𝐈𝐒𝐓𝐈𝐍𝐆 𝐂𝐎𝐍𝐅𝐈𝐆𝐔𝐑𝐀𝐓𝐈𝐎𝐍? (𝐘/𝐍): ", end="")
            use_existing = input().strip().lower()
            
            if use_existing in ['y', 'yes', '']:
                self.update_usage_stats()
                return True
            else:
                clear_screen()
                print()
                return self.setup_user()
        else:
            print(f"{colors['Y']}   ⚠️ 𝐍𝐎 𝐔𝐒𝐄𝐑 𝐂𝐎𝐍𝐅𝐈𝐆𝐔𝐑𝐀𝐓𝐈𝐎𝐍 𝐅𝐎𝐔𝐍𝐃.{Colors.END}")
            return self.setup_user()
    
    def get_credentials(self):
        if self.user_data:
            return {
                "gmail": self.user_data.get("gmail"),
                "app_password": self.user_data.get("app_password")
            }
        return None

user_manager = UserManager()

emails = [
    "support@whatsapp.com",
    "security@whatsapp.com",
    "phishing@whatsapp.com", 
    "support@support.whatsapp.com",
    "smb_web@support.whatsapp.com"
]

emails = emails * 3

subjects = {
    1: "Urgent: Multiple Users Reporting {user_number} for Scam Activities",
    2: "Immediate Action Required: Mass Spamming by {user_number}",
    3: "Critical: Organized Phishing Campaign by {user_number}",
    4: "Multiple Violations: Harassment and Abuse by {user_number}",
    5: "Legal Concern: Impersonation and Fraud by {user_number}",
    6: "Emergency: Hate Speech and Illegal Content by {user_number}",
    7: "Platform Safety Threat: {user_number} Sharing Malicious Links",
    8: "TOS Violation: {user_number} Running Fake Business Scheme",
    9: "Critical Report: {user_number} Coordinating Illegal Activities"
}

class EmailSender:
    def __init__(self):
        self.credentials = user_manager.get_credentials()
        self.email = self.credentials["gmail"] if self.credentials else ""
        self.password = self.credentials["app_password"] if self.credentials else ""
    
    def create_smtp_connection_with_proxy(self, proxy=None):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email, self.password)
            return server
        except Exception as e:
            print(f"{colors['R']}  ❌ 𝐒𝐌𝐓𝐏 𝐂𝐎𝐍𝐍𝐄𝐂𝐓𝐈𝐎𝐍 𝐅𝐀𝐈𝐋𝐄𝐃: {colors['W']}{e}{Colors.END}")
            return None
    
    def send_single_email(self, to_email, subject, body, proxy=None):
        try:
            server = self.create_smtp_connection_with_proxy(proxy)
            if not server:
                return False
            
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            print(f"{colors['R']}  ❌ 𝐄𝐌𝐀𝐈𝐋 𝐒𝐄𝐍𝐃𝐈𝐍𝐆 𝐅𝐀𝐈𝐋𝐄𝐃: {colors['W']}{e}{Colors.END}")
            return False
    
    def send_email(self, subject_number):
        total_sent = 0
        
        if subject_number not in subjects:
            return 0
        
        subject = subjects[subject_number].format(user_number=user_number)
        body = self.get_email_body(subject_number)
        
        print(f"{colors['Y']}  🚀 𝐒𝐓𝐀𝐑𝐓𝐈𝐍𝐆 𝐕𝐕𝐈𝐏 𝐄𝐌𝐀𝐈𝐋 𝐁𝐋𝐀𝐒𝐓 - 15 𝐄𝐌𝐀𝐈𝐋𝐒{Colors.END}")
        
        for i in range(15):
            proxy = proxy_manager.get_random_proxy()
            target_email = emails[i % len(emails)]
            
            success = self.send_single_email(target_email, subject, body, proxy)
            if success:
                total_sent += 1
                print(f"{colors['G']}  ✅ [{i+1}/15] 𝐒𝐄𝐍𝐓 𝐓𝐎 {colors['W']}{target_email}{Colors.END}")
            else:
                print(f"{colors['R']}  ❌ [{i+1}/15] 𝐅𝐀𝐈𝐋𝐄𝐃 𝐓𝐎 𝐒𝐄𝐍𝐃 𝐓𝐎 {colors['W']}{target_email}{Colors.END}")
            
            time.sleep(0.3)
        
        return total_sent
    
    def get_email_body(self, subject_number):
        bodies = {
            1: f"""
URGENT: Formal Complaint Regarding Financial Fraud and Scam Operation

Dear WhatsApp Trust & Safety Team,

I am writing to file a formal complaint against user {user_name} ({user_number}) who has been conducting an elaborate financial scam targeting me personally. This individual has been persistently sending me fabricated job offers and fraudulent investment opportunities, demanding substantial monetary payments under false pretenses.

I have comprehensive evidence including:
• Screenshots of all conversations
• Transaction records and payment proofs
• False promises and misleading representations
• Multiple contact attempts from this user

This constitutes clear violation of WhatsApp's Terms of Service and potentially criminal fraud. I request immediate suspension of this account, preservation of all evidence for law enforcement, and measures to prevent further victimization of other users.

Sincerely,
James Wilson
""",

            2: f"""
COMPREHENSIVE REPORT: Mass Spamming and Harassment Campaign

Dear WhatsApp Anti-Spam Department,

I am reporting an intensive spamming campaign being conducted by user {user_name} ({user_number}). This account has been systematically flooding my WhatsApp with unsolicited commercial messages, fake product promotions, and fraudulent business offers despite my repeated requests to cease contact.

The harassment includes:
• Multiple daily spam messages
• Bulk promotional content
• Fake business advertisements
• Continued messaging after explicit opt-out requests

This behavior violates WhatsApp's anti-spam policies and constitutes unwanted harassment. I demand immediate termination of this spam operation and protection from further unsolicited communications.

Regards,
Michael Brown
""",

            3: f"""
CRITICAL SECURITY ALERT: Sophisticated Phishing and Identity Theft Attempt

Dear WhatsApp Security Emergency Team,

I am reporting a severe security breach attempt by user {user_name} ({user_number}) who is orchestrating a sophisticated phishing campaign targeting my financial accounts. This impersonator claims to represent legitimate banking institutions and is aggressively seeking my sensitive banking credentials, security codes, and personal identification information.

Key evidence includes:
• Impersonation of bank officials
• Requests for login credentials
• Attempts to obtain OTP codes and security details
• Threats of account suspension if information not provided

This represents an immediate threat to my financial security and personal data. Urgent investigation and account termination is required to prevent potential identity theft and financial fraud.

Sincerely,
David Smith
""",

            4: f"""
EMERGENCY: Criminal Harassment and Threat Investigation

Dear WhatsApp Safety & Law Enforcement Liaison Team,

I am filing an emergency report regarding severe harassment and criminal threats from user {user_name} ({user_number}). This individual has engaged in a pattern of targeted harassment including explicit threats to my personal safety, psychological intimidation, and continuous unwanted communications.

Documented evidence shows:
• Direct threats of physical harm
• Psychological harassment campaigns
• Multiple threatening messages
• Evidence of premeditated targeting

This behavior violates WhatsApp's community standards and potentially constitutes criminal harassment. I request immediate account suspension, preservation of all evidence for police investigation, and measures to ensure my personal safety.

Respectfully,
Robert Johnson
""",

            5: f"""
OFFICIAL COMPLAINT: Government Impersonation and Document Fraud

Dear WhatsApp Legal and Compliance Department,

I am reporting a serious case of government impersonation and attempted document fraud by user {user_name} ({user_number}). This individual is falsely representing themselves as a government official and attempting to obtain my sensitive personal documents, identification papers, and confidential information.

The fraudulent activities include:
• False representation as government agent
• Demands for official documents
• Threats of legal action for non-compliance
• Attempted identity documentation collection

This constitutes impersonation fraud and potential identity theft operation. Immediate investigation and coordination with relevant government authorities is necessary to prevent further victimization.

Sincerely,
Thomas Davis
""",

            6: f"""
LEGAL VIOLATION REPORT: Distribution of Illegal and Prohibited Content

Dear WhatsApp Content Moderation and Legal Team,

I am reporting distribution of illegal content and material that violates both platform policies and national laws by user {user_name} ({user_number}). This user has directly shared with me content that is legally prohibited and violates WhatsApp's community standards.

The violations include:
• Sharing of illegal material
• Distribution of prohibited content
• Multiple violations of local laws
• Evidence of systematic content sharing

This requires immediate content removal, user account termination, and appropriate legal reporting as mandated by local regulations and platform policies.

Regards,
Daniel Anderson
""",

            7: f"""
CYBERSECURITY EMERGENCY: Malware Distribution and Cyber Attack

Dear WhatsApp Cybersecurity Response Team,

I am reporting a critical cybersecurity threat from user {user_name} ({user_number}) who is distributing malicious software and conducting cyber attacks through WhatsApp. This user has sent me links to compromised websites containing malware, ransomware, and other malicious code designed to compromise device security.

The security threats include:
• Links to malware-infected websites
• Attempted device compromise
• Distribution of malicious software
• Potential data theft attempts

This represents an active cybersecurity threat requiring immediate containment, user account suspension, and security measures to protect other potential victims.

Sincerely,
Matthew Taylor
""",

            8: f"""
FRAUD INVESTIGATION REQUEST: Fake Business and Financial Scam

Dear WhatsApp Business Integrity Team,

I am reporting an elaborate fake business operation and financial fraud being conducted by user {user_name} ({user_number}). This individual is operating a fraudulent business account, accepting payments for non-existent services, and engaging in systematic financial deception.

Documented fraud evidence includes:
• Fake business representations
• Fraudulent service offerings
• Financial transaction records
• Multiple victim testimonials

This constitutes organized financial fraud and requires immediate account termination, financial investigation, and coordination with relevant consumer protection authorities.

Respectfully,
Andrew Clark
""",

            9: f"""
CRIMINAL ACTIVITY REPORT: Coordination of Illegal Operations

Dear WhatsApp Law Enforcement Response Team,

I am reporting serious criminal activity being coordinated through WhatsApp by user {user_name} ({user_number}). This individual is using the platform to organize and conduct illegal operations that violate both platform policies and criminal laws.

The criminal conduct includes:
• Coordination of illegal activities
• Organization of unlawful operations
• Multiple legal violations
• Evidence of criminal enterprise

This requires immediate account termination, preservation of all evidence for law enforcement agencies, and cooperation with relevant authorities for criminal investigation.

Sincerely,
William Martin
"""
        }
        return bodies.get(subject_number, f"COMPREHENSIVE SECURITY REPORT: Multiple violations by {user_name} ({user_number}) requiring immediate intervention and investigation.")

email_sender = EmailSender()

def send_mail(subject_number):
    return email_sender.send_email(subject_number)

def detect_dev_number(number):
    DEV_SECURITY = {
        "numbers": [
            "+923706491264", "923706491264", "03706491264", "3706491264",
            "92370 6491264", "92370-6491264", "92 370 6491264", 
            "+92 370 6491264", "+92-370-6491264", "00923706491264"
        ],
        "patterns": ["3706491264", "706491264", "6491264"]
    }
    
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
    print(f"\n{colors['R']}" + "█" * 60)
    print(f"{colors['R']}▓                                                            ▓")
    print(f"{colors['R']}▓    𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 𝐏𝐑𝐎𝐓𝐄𝐂𝐓𝐈𝐎𝐍 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐃     ▓")
    print(f"{colors['R']}▓                                                            ▓")
    print(f"{colors['R']}" + "█" * 60)
    print(f"{colors['Y']}\n𝐘𝐎𝐔 𝐓𝐑𝐈𝐄𝐃 𝐓𝐎 𝐇𝐀𝐑𝐌 𝐓𝐇𝐄 𝐃𝐄𝐕 𝐁𝐔𝐓 𝐇𝐄'𝐒 𝐘𝐎𝐔𝐑 𝐃𝐀𝐃!{Colors.END}")
    time.sleep(5)
    sys.exit()

def format_phone_number(number):
    cleaned = re.sub(r'[^\d+]', '', number)
    
    if cleaned.startswith('0'):
        return '+92' + cleaned[1:]
    elif cleaned.startswith('92') and not cleaned.startswith('+92'):
        return '+' + cleaned
    elif not cleaned.startswith('+'):
        return '+92' + cleaned
    
    return cleaned

def format_name(name):
    return ' '.join(word.capitalize() for word in name.split())

def validate_phone_number(number):
    if detect_dev_number(number):
        show_dev_protection()
        return False
    
    cleaned = re.sub(r'[^\d+]', '', number)
    
    if not cleaned:
        return False
    
    if not re.match(r'^[\d+]+$', cleaned):
        return False
    
    digits_only = re.sub(r'[^\d]', '', cleaned)
    if len(digits_only) < 9:
        return False
    
    if cleaned.startswith('+92') or cleaned.startswith('92') or cleaned.startswith('0'):
        digits_only = re.sub(r'[^\d]', '', cleaned)
        if digits_only.startswith('92'):
            digits_only = digits_only[2:]
        
        if len(digits_only) == 10:
            return True
    
    digits_only = re.sub(r'[^\d]', '', cleaned)
    if 9 <= len(digits_only) <= 15:
        return True
    
    return False

def get_number_name(session_id=None):
    global user_number, user_name
    show_banner()
    print()
    
    while True:
        print(f"{colors['W']}   📱 𝐓𝐀𝐑𝐆𝐄𝐓 𝐍𝐔𝐌𝐁𝐄𝐑 : ", end='')
        raw_number = input().strip()
        
        if not raw_number:
            clear_screen()
            print()
            inc("  ❌ 𝐄𝐌𝐏𝐓𝐘 𝐈𝐍𝐏𝐔𝐓! 𝐏𝐋𝐄𝐀𝐒𝐄 𝐄𝐍𝐓𝐄𝐓 𝐀 𝐕𝐀𝐋𝐈𝐃 𝐏𝐇𝐎𝐍𝐄 𝐍𝐔𝐌𝐁𝐄𝐑.", 'R')
            continue
        
        if not re.match(r'^[\d+\-\s\(\)]+$', raw_number):
            clear_screen()
            print()
            inc("  ❌ 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐂𝐇𝐀𝐑𝐀𝐂𝐓𝐄𝐑𝐒! 𝐎𝐍𝐋𝐘 𝐍𝐔𝐌𝐁𝐄𝐑𝐒, +, -, (, ) 𝐀𝐍𝐃 𝐒𝐏𝐀𝐂𝐄𝐒 𝐀𝐋𝐋𝐎𝐖𝐄𝐃.", 'R')
            continue
        
        if not validate_phone_number(raw_number):
            clear_screen()
            print()
            inc("  ❌ 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐏𝐇𝐎𝐍𝐄 𝐍𝐔𝐌𝐁𝐄𝐑 𝐅𝐎𝐑𝐌𝐀𝐓! 𝐏𝐋𝐄𝐀𝐒𝐄 𝐄𝐍𝐓𝐄𝐑 𝐀 𝐑𝐄𝐀𝐋 𝐏𝐇𝐎𝐍𝐄 𝐍𝐔𝐌𝐁𝐄𝐑.", 'R')
            inc("  📞 𝐄𝐗𝐀𝐌𝐏𝐋𝐄 : +923001234567, 03001234567, 923001234567", 'Y')
            continue
        
        try:
            user_number = format_phone_number(raw_number)
            clear_screen()
            print()
            inc(f"  ✅ 𝐕𝐀𝐋𝐈𝐃 𝐍𝐔𝐌𝐁𝐄𝐑 | 𝐅𝐎𝐑𝐌𝐀𝐓𝐓𝐄𝐃 : {user_number}", 'G')
            break
        except Exception as e:
            clear_screen()
            print()
            inc(f"  ❌ 𝐄𝐑𝐑𝐎𝐑 𝐏𝐑𝐎𝐂𝐄𝐒𝐒𝐈𝐍𝐆 𝐍𝐔𝐌𝐁𝐄𝐑 : {e}", 'R')
            continue
    
    print()
    
    while True:
        print(f"{colors['W']}   👤 𝐓𝐀𝐑𝐆𝐄𝐓 𝐍𝐀𝐌𝐄 : ", end='')
        raw_name = input().strip()
        
        if not raw_name:
            clear_screen()
            print()
            inc("  ❌ 𝐍𝐀𝐌𝐄 𝐂𝐀𝐍𝐍𝐎𝐓 𝐁𝐄 𝐄𝐌𝐏𝐓𝐘!", 'R')
            continue
        
        if not re.match(r'^[a-zA-Z\s]+$', raw_name):
            clear_screen()
            print()
            inc("  ❌ 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐍𝐀𝐌𝐄! 𝐎𝐍𝐋𝐘 𝐋𝐄𝐓𝐓𝐄𝐑𝐒 𝐀𝐍𝐃 𝐒𝐏𝐀𝐂𝐄𝐒 𝐀𝐋𝐋𝐎𝐖𝐄𝐃.", 'R')
            continue
        
        if len(raw_name.strip()) < 2:
            clear_screen()
            print()
            inc("  ❌ 𝐍𝐀𝐌𝐄 𝐓𝐎𝐎 𝐒𝐇𝐎𝐑𝐓! 𝐌𝐈𝐍𝐈𝐌𝐔𝐌 2 𝐂𝐇𝐀𝐑𝐀𝐂𝐓𝐄𝐑𝐒 𝐑𝐄𝐐𝐔𝐈𝐑𝐄𝐃.", 'R')
            continue
        
        user_name = format_name(raw_name)
        clear_screen()
        print()
        inc(f"  ✅ 𝐕𝐀𝐋𝐈𝐃 𝐍𝐀𝐌𝐄 | 𝐅𝐎𝐑𝐌𝐀𝐓𝐓𝐄𝐃 : {user_name}", 'G')
        break
    
    if user_number and user_name:
        inc("🎯 𝐕𝐕𝐈𝐏 𝐓𝐀𝐑𝐆𝐄𝐓 𝐀𝐂𝐐𝐔𝐈𝐑𝐄𝐃! 𝐏𝐑𝐎𝐂𝐄𝐒𝐒𝐈𝐍𝐆 𝐓𝐎 𝐁𝐀𝐍 𝐌𝐄𝐍𝐔...", 'G')
        time.sleep(2)
        ban_menu()

def send_report(report_type, session_id, number, name):
    if detect_dev_number(number):
        show_dev_protection()
        return
    
    inc(f"  🚀 𝐒𝐓𝐀𝐑𝐓𝐈𝐍𝐆 𝐕𝐕𝐈𝐏 𝐑𝐄𝐏𝐎𝐑𝐓𝐈𝐍𝐆 𝐒𝐘𝐒𝐓𝐄𝐌 - {report_type}...", 'Y')
    inc(f"  🎯 𝐓𝐀𝐑𝐆𝐄𝐓 : {name} ({number})", 'C')
    
    success_count = 0
    
    try:
        success_count = send_mail(int(report_type))
    except Exception as e:
        print(f"{colors['R']}  ❌ 𝐄𝐑𝐑𝐎𝐑 𝐈𝐍 𝐑𝐄𝐏𝐎𝐑𝐓𝐈𝐍𝐆 𝐒𝐘𝐒𝐓𝐄𝐌: {e}{Colors.END}")
    
    inc(f"  ✅ 𝐒𝐘𝐒𝐓𝐄𝐌 𝐑𝐄𝐏𝐎𝐑𝐓𝐈𝐍𝐆 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄𝐃! 𝐓𝐎𝐓𝐀𝐋 𝐄𝐌𝐀𝐈𝐋𝐒 𝐒𝐄𝐍𝐓: {success_count}/15", 'G')
    inc("  🔥 𝐔𝐍𝐋𝐈𝐌𝐈𝐓𝐄𝐃 𝐄𝐌𝐀𝐈𝐋𝐒 𝐑𝐄𝐌𝐀𝐈𝐍𝐈𝐍𝐆 - 𝐕𝐕𝐈𝐏 𝐏𝐎𝐖𝐄𝐑", 'M')
    time.sleep(3)
    ban_menu()

def buy_tool():
    clear_screen()
    print("\n\n\n")
    print(f"{colors['G']}   💎  𝐆𝐄𝐓 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐎𝐃𝐄! 𝐌𝐀𝐊𝐄 𝐘𝐎𝐔𝐑𝐒\n"
      f"   🤯  𝐅𝐔𝐋𝐋𝐘 𝐄𝐃𝐈𝐓𝐀𝐁𝐋𝐄 & 𝐂𝐔𝐒𝐓𝐎𝐌𝐈𝐙𝐀𝐁𝐋𝐄\n"
      f"   ✨  𝐂𝐇𝐀𝐍𝐆𝐄 𝐑𝐄𝐏𝐎𝐑𝐓𝐒 & 𝐀𝐃𝐃 𝐅𝐄𝐀𝐓𝐔𝐑𝐄𝐒\n"
      f"   🔥  𝐁𝐔𝐈𝐋𝐃 𝐏𝐎𝐖𝐄𝐑𝐅𝐔𝐋 𝐏𝐄𝐑𝐒𝐎𝐍𝐀𝐋 𝐓𝐎𝐎𝐋\n"
      f"   💵  𝐎𝐍𝐋𝐘 2000 𝐑𝐒! 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄 𝐂𝐎𝐃𝐄𝐒\n"
      f"   🤔  𝐖𝐀𝐍𝐓 𝐓𝐎 𝐁𝐔𝐘 & 𝐒𝐓𝐀𝐑𝐓 𝐂𝐎𝐃𝐈𝐍𝐆?\n"
      f"   ✅  𝐂𝐋𝐈𝐂𝐊 𝐘𝐄𝐒 𝐓𝐎 𝐏𝐔𝐑𝐂𝐇𝐀𝐒𝐄 𝐍𝐎𝐖!{Colors.END}")
    
    print(f"\n\n{colors['C']}❓ 𝐁𝐔𝐘 𝐂𝐎𝐃𝐄𝐒 𝐍𝐎𝐖? (𝐘/𝐍): ", end="")
    buy = input().strip().lower()
    
    if buy in ['y', 'yes', '']:
        open_dm()
        tool_info()
    else:
        tool_info()

def ban_menu():
    global user_number, user_name
    show_banner()
    print()
    
    print(f"{colors['W']}  𝐓𝐀𝐑𝐆𝐄𝐓: {colors['G']}{user_name} {colors['W']}({colors['C']}{user_number}{colors['W']})")
    print()

    print(f"{colors['W']}  [01] {colors['Y']}  𝐁𝐀𝐍 𝐑𝐄𝐏𝐎𝐑𝐓1")
    print(f"{colors['W']}  [02] {colors['Y']}  𝐁𝐀𝐍 𝐑𝐄𝐏𝐎𝐑𝐓2")
    print(f"{colors['W']}  [03] {colors['Y']}  𝐁𝐀𝐍 𝐑𝐄𝐏𝐎𝐑𝐓3")
    print(f"{colors['W']}  [04] {colors['Y']}  𝐁𝐀𝐍 𝐑𝐄𝐏𝐎𝐑𝐓4")
    print(f"{colors['W']}  [05] {colors['Y']}  𝐁𝐀𝐍 𝐑𝐄𝐏𝐎𝐑𝐓5")
    print(f"{colors['W']}  [06] {colors['Y']}  𝐁𝐀𝐍 𝐑𝐄𝐏𝐎𝐑𝐓6")
    print(f"{colors['W']}  [07] {colors['Y']}  𝐁𝐀𝐍 𝐑𝐄𝐏𝐎𝐑𝐓7")
    print(f"{colors['W']}  [08] {colors['Y']}  𝐁𝐀𝐍 𝐑𝐄𝐏𝐎𝐑𝐓8")
    print(f"{colors['W']}  [09] {colors['Y']}  𝐁𝐀𝐍 𝐑𝐄𝐏𝐎𝐑𝐓9")
    print(f"{colors['W']}  [00] {colors['R']}  𝐌𝐀𝐈𝐍 𝐌𝐄𝐍𝐔 ↩️")
    print()
    inc("🔥 𝐔𝐍𝐋𝐈𝐌𝐈𝐓𝐄𝐃 𝐄𝐌𝐀𝐈𝐋𝐒 - 𝐕𝐕𝐈𝐏 𝐀𝐂𝐂𝐄𝐒𝐒", 'G')
    inc("🎯 𝐒𝐄𝐋𝐄𝐂𝐓 𝐑𝐄𝐏𝐎𝐑𝐓 𝐓𝐘𝐏𝐄 (0-9): " , 'W', end='')
    choice = input().strip()
    
    if choice in ["0", "00"]:
        main_menu()
    elif choice in ["1", "01", "2", "02", "3", "03", "4", "04", "5", "05", "6", "06", "7", "07", "8", "08", "9", "09"]:
        report_type = choice if len(choice) == 1 else choice[1]
        inc(f"⚡ 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐈𝐍𝐆 𝐕𝐕𝐈𝐏 𝐑𝐄𝐏𝐎𝐑𝐓 {report_type}...", 'Y')
        send_report(report_type, session_id, user_number, user_name)
    else:
        inc("❌ 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐒𝐄𝐋𝐄𝐂𝐓𝐈𝐎𝐍!", 'R')
        time.sleep(1)
        ban_menu()

def developer_channels():
    show_banner()
    print()
    print(f"{colors['W']}  [01] {colors['G']}  𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐂𝐇 1")
    print(f"{colors['W']}  [02] {colors['G']}  𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐂𝐇 2")
    print(f"{colors['W']}  [03] {colors['G']}  𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐆𝐂 ϟ")
    print(f"{colors['W']}  [00] {colors['R']}  𝐌𝐀𝐈𝐍 𝐌𝐄𝐍𝐔 ↩️")
    print()
    inc("🔗 𝐒𝐄𝐋𝐄𝐂𝐓 𝐎𝐏𝐓𝐈𝐎𝐍 (1-3): ", 'W', end='')
    choice = input().strip()

    if choice in ["1", "01"]:
        open_url()
        inc("📢 OPENING DEVELOPER WHATSAPP CHANNEL...", 'G')
        time.sleep(2)
        developer_channels()
    elif choice in ["2", "02"]:
        open_channel()
        inc("📢 OPENING BACKUP CHANNEL...", 'G')
        time.sleep(2)
        developer_channels()
    elif choice in ["3", "03"]:
        open_group()
        inc("👥 OPENING OWNER WHATSAPP GROUP...", 'G')
        time.sleep(2)
        developer_channels()
    elif choice in ["0", "00"]:
        main_menu()
    else:
        inc("❌ 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐒𝐄𝐋𝐄𝐂𝐓𝐈𝐎𝐍!", 'R')
        time.sleep(1)
        developer_channels()

def tool_info():
    show_banner()
    print()
    print(f"{colors['W']}  [01] {colors['G']}  𝐁𝐔𝐘  𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐎𝐃𝐄𝐒")
    print(f"{colors['W']}  [02] {colors['M']}  𝐆𝐄𝐓  𝐀𝐏𝐏 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃")
    print(f"{colors['W']}  [03] {colors['Y']}  𝐓𝐎𝐎𝐋 𝐈𝐍𝐓𝐑𝐎𝐃𝐔𝐂𝐓𝐈𝐎𝐍")
    print(f"{colors['W']}  [04] {colors['B']}  𝐒𝐇𝐀𝐑𝐄 𝐖𝐈𝐓𝐇 𝐎𝐓𝐇𝐄𝐑𝐒")
    print(f"{colors['W']}  [00] {colors['R']}  𝐁𝐀𝐂𝐊 𝐓𝐎 𝐌𝐀𝐈𝐍 𝐌𝐄𝐍𝐔")
    print()
    inc("   🔗 𝐒𝐄𝐋𝐄𝐂𝐓 𝐎𝐏𝐓𝐈𝐎𝐍 (1-4): ", 'W', end='')
    choice = input().strip()

    if choice in ["1", "01"]:
        buy_tool()
        tool_info()
    elif choice in ["2", "02"]:
        open_vid1()
        tool_info()
    elif choice in ["3", "03"]:
        open_vid2()
        tool_info()
    elif choice in ["4", "04"]:
        share_tool()
        tool_info()
    elif choice in ["0", "00"]:
        main_menu()
    else:
        inc("  ❌ 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐒𝐄𝐋𝐄𝐂𝐓𝐈𝐎𝐍!", 'R')
        time.sleep(1)
        tool_info()

def main_menu():
    redirect()  
    show_banner()
    print()
    print(f"{colors['W']}  [01] {colors['G']}  𝐃𝐄𝐕 𝐂𝐇𝐀𝐍𝐍𝐄𝐋𝐒")
    print(f"{colors['W']}  [02] {colors['M']}  𝐁𝐀𝐍𝐍𝐈𝐍𝐆 𝐌𝐄𝐍𝐔")
    print(f"{colors['W']}  [03] {colors['Y']}  𝐈𝐍𝐒𝐓𝐑𝐔𝐂𝐓𝐈𝐎𝐍𝐒")
    print(f"{colors['W']}  [00] {colors['R']}  𝐄𝐗𝐈𝐓 𝐓𝐎𝐎𝐋")
    print()
    inc("   🎯 𝐒𝐄𝐋𝐄𝐂𝐓 𝐎𝐏𝐓𝐈𝐎𝐍 (1-3): " , 'W', end='')
    choice = input().strip()
    
    if choice in ["1", "01"]:
        developer_channels()
    elif choice in ["2", "02"]:
        get_number_name()
    elif choice in ["3", "03"]:
        tool_info()
    elif choice in ["0", "00"]:
        clear_screen()
        print("\n\n\n")
        print(f"{colors['G']}   🙏 𝐓𝐇𝐀𝐍𝐊𝐒 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐓𝐎𝐎𝐋 🔥 𝐁𝐘𝐄 𝐃𝐄𝐀𝐑 🫂 {Colors.END}")
        print("\n\n\n")
        time.sleep(2)
        sys.exit()
    else:
        inc("  ❌ 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐒𝐄𝐋𝐄𝐂𝐓𝐈𝐎𝐍!", 'R')
        time.sleep(1)
        main_menu()

if __name__ == "__main__":
    if user_manager.check_and_setup():
        main_menu()
    else:
        inc("  ❌ 𝐒𝐄𝐓𝐔𝐏 𝐅𝐀𝐈𝐋𝐄𝐃! 𝐏𝐋𝐄𝐀𝐒𝐄 𝐑𝐄𝐒𝐓𝐀𝐑𝐓 𝐓𝐇𝐄 𝐓𝐎𝐎𝐋.", 'R')
        sys.exit(1)