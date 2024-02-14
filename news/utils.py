from datetime import datetime
from .models import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.auth.models import User
import re

def get_default_context(context):
    date = datetime.now().strftime("%A, %B %d, %Y")
    tags = Tag.objects.all()
    context['date'] = date
    context['tags'] = tags
    context['tranding_news'] = New.objects.filter(date__month=datetime.now().month).order_by('-views')[:5]
    return context


def send_gmail(title, text, email, name):
    address = 'shoprbexruzroot@gmail.com'
    message = MIMEMultipart()
    message['From'] = address
    message['To'] = address
    message['Subject'] = f'{title}'
    mail_content = f'Message from: {email} ({name})\n\n{text}'
    message.attach(MIMEText(mail_content, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(address, "oshk bbyv tixg edwm")
    text = message.as_string()
    server.sendmail(address, address, text)
    server.quit()

def custom_slugify(value):
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)