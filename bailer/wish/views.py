from django.shortcuts import render
from .models import Member
from django.conf import settings
from django.core.mail import send_mail
from datetime import date

def home(request):
    if request.method == "POST":
        data = request.POST
        Name = data.get('Name')
        Email = data.get('Email')
        DOB = data.get('DOB')
        Member.objects.create(
            Name=Name,
            Email=Email,
            DOB=DOB
        )
    
    result = Member.objects.all()
    today = date.today()
    users_with_birthday = result.filter(DOB__day=today.day, DOB__month=today.month)
    
    for profile in users_with_birthday:
        subject = "Happy Birthday"
        message = f"Dear {profile.Name},\n\nTeam Big Data Centre of Excellence would like to wish you a very happy birthday. May you achieve everything that you desire."
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [profile.Email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    
    return render(request, 'home.html')
