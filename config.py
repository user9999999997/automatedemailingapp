from dotenv import load_dotenv
import os

load_dotenv()

FROM_EMAIL = os.getenv("FROM_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))
MAX_EMAILS_PER_DAY = int(os.getenv("MAX_EMAILS_PER_DAY", "15"))
MAX_EMAILS_PER_RUN = int(os.getenv("MAX_EMAILS_PER_RUN", 5))


SIGNATURE = """
Best,  
Liam Kircher  
Penticton Janitorial
kircherliam@gmail.com

If this isn't relevant, feel free to reply with "unsubscribe" and I won’t follow up.
""".strip()
