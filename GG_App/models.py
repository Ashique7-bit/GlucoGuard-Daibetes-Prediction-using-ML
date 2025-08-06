from django.db import models

# Create your models here.


class login_table(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    type=models.CharField(max_length=20)
class user_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    photo=models.FileField()
    address=models.CharField(max_length=20)
    email=models.EmailField()
    weight=models.FloatField()
    height=models.FloatField()
class rating_table(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    rating=models.FloatField()
    date=models.DateField()
    review=models.CharField(max_length=20)
class dietitian_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    photo = models.FileField()
    dob = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    email = models.EmailField()
class doctor_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    photo = models.FileField()
    dob = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    email = models.EmailField()
class dietplan_table(models.Model):
    dietition=models.ForeignKey(dietitian_table,on_delete=models.CASCADE)
    BMI=models.FloatField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    dietplan= models.CharField(max_length=20)
class chat_table(models.Model):
    FROM_ID = models.ForeignKey(login_table, on_delete=models.CASCADE,related_name="ff")
    TO_ID = models.ForeignKey(login_table, on_delete=models.CASCADE,related_name='tt')
    message= models.CharField(max_length=20)
    date = models.DateField()
    time=models.TimeField()
class tip_table(models.Model):
    DIETITION = models.ForeignKey(dietitian_table, on_delete=models.CASCADE)
    tips= models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
class schedule_table(models.Model):
    DOC_ID = models.ForeignKey(doctor_table, on_delete=models.CASCADE)
    date = models.DateField()
    from_time= models.TimeField()
    to_time = models.TimeField()
class booking_table(models.Model):
    SCHEDULE= models.ForeignKey(schedule_table,on_delete=models.CASCADE)
    USER= models.ForeignKey(user_table,on_delete=models.CASCADE)
    time = models.TimeField()
    status=models.CharField(max_length=20)
class doubt_table(models.Model):
    DOC_ID = models.ForeignKey(doctor_table, on_delete=models.CASCADE)
    UID = models.ForeignKey(user_table, on_delete=models.CASCADE)
    doubt=models.CharField(max_length=20)
    reply=models.CharField(max_length=20)
    date=models.DateField()

class doctor_rating_table(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    DOCTOR=models.ForeignKey(doctor_table,on_delete=models.CASCADE)
    rating=models.FloatField()
    date=models.DateField()
    review=models.CharField(max_length=20)