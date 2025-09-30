from colorama import Fore, Style

COLORS = {
    'R': Fore.RED + Style.BRIGHT,
    'G': Fore.GREEN + Style.BRIGHT,
    'Y': Fore.YELLOW + Style.BRIGHT,
    'C': Fore.CYAN + Style.BRIGHT,
    'W': Fore.WHITE + Style.BRIGHT,
    'M': Fore.MAGENTA + Style.BRIGHT
}

MAX_EMAILS_PER_USER = 50
USER_SESSIONS = {}

GMAIL_ACCOUNTS = [
    {"email": "your1@gmail.com", "password": "app_password_1", "active": True},
    {"email": "your2@gmail.com", "password": "app_password_2", "active": True},
    {"email": "your3@gmail.com", "password": "app_password_3", "active": True},
]
