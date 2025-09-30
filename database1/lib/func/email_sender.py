import time
import random
import smtplib
from email.mime.text import MIMEText
from lib.data.config import COLORS, GMAIL_ACCOUNTS
from lib.data.emails import REPORT_EMAILS
from lib.data.subjects import SUBJECTS
from lib.data.reports import REPORTS
from lib.func.utils import check_rate_limit, update_email_count

def send_report(subject_id, session_id, user_number, user_name):

    if not check_rate_limit(session_id):
        return False
    
    subject = SUBJECTS.get(subject_id)
    body_template = REPORTS.get(subject_id)
    target_emails = REPORT_EMAILS.get(subject_id, [])
    
    if not subject or not body_template or not target_emails:
        print(f"{COLORS['R']}❌ Invalid report selection!")
        return False
    
    body = body_template.format(number=user_number, name=user_name)
    
    total_emails = len(target_emails)
    available_accounts = [acc for acc in GMAIL_ACCOUNTS if acc.get('active', True)]
    
    if not available_accounts:
        print(f"{COLORS['R']}❌ No active Gmail accounts available!")
        return False
    
    emails_per_account = max(1, total_emails // len(available_accounts))
    print(f"{COLORS['C']}📊 Strategy: {total_emails} emails ÷ {len(available_accounts)} accounts")
    
    total_sent = 0
    successful_accounts = 0
    
    random.shuffle(available_accounts)
    
    for i, account in enumerate(available_accounts):
        if total_sent >= total_emails:
            break
            
        try:
            
            start_idx = i * emails_per_account
            end_idx = min(start_idx + emails_per_account, total_emails)
            account_emails = target_emails[start_idx:end_idx]
            
            if not account_emails:
                continue
                
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = account['email']
            
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(account['email'], account['password'])
            
            print(f"{COLORS['C']}🔄 Account {i+1}: {account['email']}")
            
            for j, email in enumerate(account_emails, 1):
                msg['To'] = email
                server.sendmail(account['email'], email, msg.as_string())
                total_sent += 1
                print(f"{COLORS['G']}✅ [{total_sent}] → {email}")
                time.sleep(random.uniform(1, 3))  
            
            server.quit()
            successful_accounts += 1
            print(f"{COLORS['G']}✓ {len(account_emails)} emails sent successfully")
            
        except Exception as e:
            print(f"{COLORS['R']}❌ Account failed: {str(e)[:50]}...")
            
            account['active'] = False
    
    update_email_count(session_id, total_sent)
    
    print(f"{COLORS['C']}\n🎉 RESULT: {successful_accounts} accounts | {total_sent} emails sent")
    print(f"{COLORS['Y']}📈 Your daily usage: {USER_SESSIONS[session_id]['email_count']}/{MAX_EMAILS_PER_USER}")
    time.sleep(3)
    return True