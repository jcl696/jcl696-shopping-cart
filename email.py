
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


#importing api information

MY_EMAIL_ADDRESS = "jcl696@stern.nyu.edu"
SENDGRID_API_KEY = "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"






message = Mail(
    from_email=MY_EMAIL_ADDRESS,
    to_emails=MY_EMAIL_ADDRESS,
    subject='Sending receipts for shopping_cart_exercise',
    html_content='<strong>YOUR RECEIPT</strong>')

sg = SendGridAPIClient(os.environ.get(SENDGRID_API_KEY))
response = sg.send(message)
print(response.status_code, response.body, response.headers)
