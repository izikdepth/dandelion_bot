import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

email_address= os.getenv("EMAIL_ADDRESS")
email_password= os.getenv("SOFTWARE_PASSWORD")

yag = yagmail.SMTP(email_address, email_password)

try:
    yag.send(
        to='receiving-email@gmail.com',
        subject='Test Email',
        contents='This is a test email.'
    )
    print("Email sent!")
except Exception as e:
    print(f"Error: {e}")
