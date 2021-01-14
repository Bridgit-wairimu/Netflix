from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to Netflix '
    sender = 'kirikabridgit@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/moviesemail.txt',{"name": name})
    html_content = render_to_string('email/moviesemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()