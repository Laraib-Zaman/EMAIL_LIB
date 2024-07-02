

```markdown
# Email Service

A Python package for sending emails using Gmail's SMTP server.

## Features

- Set up and send emails programmatically.
- Supports multiple recipients.
- Secure connection using SSL.

## Installation

### Clone the Repository

1. Clone the repository:
   ```sh
   git clone https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
   ```
   
2. Navigate to the project directory:
   ```sh
   cd REPOSITORY_NAME/EMAIL
   ```

### Install the Package

3. Install the package:
   ```sh
   pip install .
   ```

## Usage

Here is an example of how to use the `EmailService` class:

```python
from email_service.email_service import EmailService

# Create an instance of EmailService
email_service = EmailService()

# Set the email details
email_service.email_sender = 'your_email@gmail.com'
email_service.email_password = 'your_app_password'
email_service.email_receiver = ['recipient1@example.com', 'recipient2@example.com']
email_service.subject = 'Test Subject'
email_service.body = 'This is a test email.'

# Set the email message
email_service.set_email()

# Send the email
email_service.send_email()
```

## Requirements

- Python 3.x

## Dependencies

- `smtplib` (part of Python standard library)
- `ssl` (part of Python standard library)
- `email.message` (part of Python standard library)




