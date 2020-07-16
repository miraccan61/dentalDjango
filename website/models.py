from django.db import models
# Create your models here.
class Appointment(models.Model):
    your_name= models.CharField(max_length=40,verbose_name="Enter Your Full Name")
    your_phone=models.CharField(max_length=17,verbose_name="Telephone Number ex: +90 111 222 33 44")
    your_mail=models.EmailField(verbose_name="Enter Your Email")
    your_address=models.CharField(max_length=40,verbose_name="Enter Your Address")
    schedule_date = [
    ('Choose Your Scheldule', 'Choose Your Scheldule'),
    ('9 AM to 10 AM', '9 AM to 10 AM'),
    ('10 AM to 11 AM', '10 AM to 11 AM'),
    ('11 AM to 12 PM', '11 AM to 12 PM'),
    ('1 PM to 2 PM', '1 PM to 2 PM'),
    ('2 PM to 3 PM', '2 PM to 3 PM'),
    ('3 PM to 4 PM', '3 PM to 4 PM'),
    ('4 PM to 5 PM', '4 PM to 5 PM'),
    ]
    schedule_dates=models.CharField(
        max_length=40,
        choices=schedule_date,
        default='Choose Your Scheldule',
    )
    your_messagess=models.TextField(verbose_name="Enter Your Message")
    Schedule_Days = [
    ('Choose Your Day', 'Choose Your Day'),
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),   
    ]
    schedule_days = models.CharField(
        max_length=35,
        choices=Schedule_Days,
        default='Choose Your Scheldule Day',
    )
    time_stamp=models.DateTimeField(auto_now_add=True)
class Contact(models.Model):
    your_name = models.CharField(max_length=40,verbose_name="Enter Your Name")
    your_mail = models.EmailField(verbose_name="Enter Your Mail")
    your_messagess = models.TextField(verbose_name="Enter Your Message")
    time_stamp=models.DateTimeField(auto_now_add=True)

