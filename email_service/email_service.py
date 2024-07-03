import smtplib
import ssl
from email.message import EmailMessage


class EmailService:
    """
    A service for sending emails using the smtplib and ssl libraries.

    Attributes:
        email_sender (str): The sender's email address.
        email_password (str): The sender's email password.
        email_receiver (list): A list of recipient email addresses.
        subject (str): The subject of the email.
        body (str): The body content of the email.
        email_message (EmailMessage): An EmailMessage object representing the email.
    """

    def __init__(self):
        self.email_sender = None
        self.email_password = None
        self.email_receiver = None
        self.subject = None
        self.body = None
        self.email_message = None

    def set_email(self):
        try:
            if not self.email_sender:
                raise ValueError("Sender email cannot be empty.")
            if not self.email_receiver or not any(self.email_receiver):
                raise ValueError("Receiver email cannot be empty.")
            if not self.subject and not self.body:
                raise ValueError("At least one of subject or body must be filled.")
            
            em = EmailMessage()
            em['From'] = self.email_sender
            em['To'] = ', '.join(self.email_receiver)
            em['Subject'] = self.subject
            em.set_content(self.body)
            self.email_message = em

        except ValueError as e:
            print(f"Error: {e}")
            self.email_message = None  # Ensure email_message is None if there's an error

    def send_email(self):
        try:
            if self.email_message is None:
                raise ValueError("Email message not set or invalid.")
            
            if self.email_password is None:
                raise ValueError("Email password is not set.")

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(self.email_sender, self.email_password)
                smtp.sendmail(self.email_sender, self.email_receiver, self.email_message.as_string())
                print("Email sent successfully!")

        except ValueError as e:
            print(f"Error: {e}")
        except smtplib.SMTPAuthenticationError as e:
            print("SMTP authentication error: Username or Password not accepted")
        except smtplib.SMTPException as e:
            print(f"SMTP error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
