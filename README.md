# Email Cleaner (IMAP)

A Python script to delete emails from specific senders using IMAP and environment variables.

## Setup

1. Clone the repo
2. Create a `.env` file:
    EMAIL=youremail@example.com
    PASSWORD=yourapppassword
    IMAP_SERVER=imap.gmail.com
    SENDERS_TO_DELETE=newsletter@example.com,spam@example.org
3. Run the script:
    python3 emailCleanserApp.py
