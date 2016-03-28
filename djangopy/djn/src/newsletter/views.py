from django.shortcuts import render
from django.conf import settings
from .forms import SignUpForm, ContactForm
from django.core.mail import send_mail
# Create your views here.


def home(request):
    title = "welcome"
    form = SignUpForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        form.save()
        print instance

    # if request.method=='POST':
    #   print request.POST
    context = {
        "t1": title,
        "form": form
    }
    return render(request, "home.html", context)


def contact(request):

    form = ContactForm(request.POST or None)
    if form.is_valid():
    #     for key, vlaue in form.cleaned_data:
    #         print key, "-->", form.cleaned_data[key]
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        full_name = form.cleaned_data.get('full_name')
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [ from_email, ]
        contact_message = "%s:%s via %s " %(full_name, message, email)
        send_mail(
            subject,
            contact_message,
            from_email,
            [to_email],
            fail_silently=False)

    context = {
        "form": form
    }

    return render(request, "forms.html", context)
