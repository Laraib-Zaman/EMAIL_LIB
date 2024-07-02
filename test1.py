from email_service.email_service import EmailService

# Create an instance of EmailService
email_service = EmailService()



# Define email sender and receiver
# email_sender = "appedology99@gmail.com" #"myexternalemail3@gmail.com" #abdul.wajid@appedology.com
# email_password = "btgt yjqo wwhq whva"#ymnl fqyp huzm nivd" #"hlzpkicuacwspoyz" #"baqqimqgrxftvvyr"
#email_receiver = ["abdul.wajid@appedology.com", "adnan.sharaf@proglobaltechnologies.com", "sardar.saleem@proglobaltechnologies.com", "hareem.ali@appedology.com", "fahad.ahmed@appedology.com"]
# email_receiver = ["abdul.wajid@appedology.com", "ameet.kumar@appedology.com", "ahtesham.haq@appedology.com"]
# Set the email details

email_service.email_sender = 'appedology99@gmail.com'
email_service.email_password = 'btgt yjqo wwhq whva' #ymnl fqyp huzm nivd'
email_service.email_receiver = ["abdul.wajid@appedology.com", "laraib.zaman@appedology.com"]
email_service.subject = 'Test Subject'
email_service.body = 'This is a test email.'

# Set the email message
email_service.set_email()

# Send the email
email_service.send_email()
