from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.conf import settings
from .forms import EmailForm
import smtplib

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                recipient = form.cleaned_data['recipient']
                
                html_message = render_to_string('send_email/email_template.html', {
                    'subject': subject,
                    'message': message,
                })
                
                email = EmailMessage(
                    subject,
                    html_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [recipient],
                )
                email.content_subtype = "html"
                email.send()
                
                return redirect('email_sent')
                
            except smtplib.SMTPSenderRefused as e:
                form.add_error(None, f"Sender refused: {e}")
            except smtplib.SMTPAuthenticationError as e:
                form.add_error(None, "Authentication failed. Check your email settings.")
            except Exception as e:
                form.add_error(None, f"Error sending email: {e}")
    else:
        form = EmailForm()
    
    return render(request, 'send_email/send_email.html', {'form': form})

def email_sent(request):
    return render(request, 'send_email/email_sent.html')