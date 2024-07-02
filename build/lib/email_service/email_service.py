import smtplib
import ssl
from email.message import EmailMessage

class EmailService:

    def __init__(self):
        self.email_sender = None       # take input from user 
        self.email_password = None             # take input from user
        self.email_receiver = None   # take input from user 
        self.subject = None                    # take input from user 
        self.body = None                       # take input from user 
        self.email_message = None              # to store the EmailMessage object

    def set_email(self):
        em = EmailMessage()
        em['From'] = self.email_sender
        em['To'] = ', '.join(self.email_receiver) 
        em['Subject'] = self.subject
        em.set_content(self.body)
        self.email_message = em
    
    def send_email(self):
        if self.email_message is None:
            raise ValueError("Email message is not set. Call set_email() first.")
        
        if self.email_password is None:
            raise ValueError("Email password is not set.")

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, self.email_receiver, self.email_message.as_string())
