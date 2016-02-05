import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject='', body=''):
    """
    Uses Mandrill to send email with given
    """
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From']    = os.environ.get('FROM_EMAIL_ADDRESS', None)
    msg['To']      = os.environ.get('TO_EMAIL_ADDRESS', None)

    username = os.environ.get('MANDRILL_USERNAME', None)
    password = os.environ.get('MANDRILL_PASSWORD', None)

    s = smtplib.SMTP('smtp.mandrillapp.com', 587)

    s.login(username, password)

    part = MIMEText(body, 'plain')
    msg.attach(part)

    s.sendmail(msg['From'], msg['To'], msg.as_string())

    s.quit()

