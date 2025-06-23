import imaplib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
IMAP_SERVER = os.getenv('IMAP_SERVER', 'imap.gmail.com')
SENDERS_TO_DELETE = os.getenv('SENDERS_TO_DELETE', '').split(',')

def delete_emails_from_senders():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")

        for sender in SENDERS_TO_DELETE:
            sender = sender.strip()
            if not sender:
                continue

            # Search emails from sender
            result, data = mail.search(None, f'FROM "{sender}"')
            email_ids = data[0].split()

            print(f"🧹 Found {len(email_ids)} emails from: {sender}")

            for email_id in email_ids:
                mail.store(email_id, '+FLAGS', '\\Deleted')

        mail.expunge()
        mail.logout()
        print("✅ Done deleting emails.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    delete_emails_from_senders()
