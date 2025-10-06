import os
import sys
import time
from lib.func.utils import get_user_session, show_banner
from lib.func.menu import main_menu

if __name__ == "__main__":
    try:
        session_id = get_user_session()
        show_banner()
        print(f"\n🎯 New session started: User {session_id}")
        time.sleep(1)
        main_menu(session_id)
    except KeyboardInterrupt:
        print(f"\n👋 Program interrupted. Goodbye!")
        sys.exit()
    except Exception as e:
        print(f"\n💥 Error: {e}")
        sys.exit()
