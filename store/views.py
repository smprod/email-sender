from django.shortcuts import render, redirect
from django.views import generic
import smtplib
from email.message import EmailMessage

from .forms import (
    EmailFormset,
    TextForm
)


def create_email(request):
    msg = EmailMessage()
    msg['From'] = "django.email@bk.ru"
    email = "django.email@bk.ru"
    password = "mM9ksceVEiNgx10FP9ir"
    template_name = 'store/create_normal.html'
    heading_message = 'Отправка письма'
    form_class = TextForm(request.POST or None)
    if request.method == 'GET':
        formset = EmailFormset(request.GET or None)
    elif request.method == 'POST':
        formset = EmailFormset(request.POST)
        if formset.is_valid():
            if form_class.is_valid():
                subject = form_class.cleaned_data.get('subject')
                message = form_class.cleaned_data.get('text')
                msg['Subject'] = subject
                msg.set_content(message)

            server = smtplib.SMTP("smtp.mail.ru", 587)

            server.starttls()
            server.login(email, password)
            for form in formset:
                to_email = form.cleaned_data.get('name')
                if to_email != None:

                    server.sendmail(email, to_email, msg.as_string())
                # save book instance
            server.quit()
            return redirect('home')

    return render(request, template_name, {
        'formset': formset,
        'form': form_class,
        'heading': heading_message,
    })

