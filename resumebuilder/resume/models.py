from django.db import models

class ResumeModel(models.Model):
    FullName=models.CharField(max_length=100) 
    ProfilePicture= models.ImageField(upload_to='Media/img')
    Email =models.EmailField()
    Phone=models.CharField(max_length=15)
    Address=models.TextField() 
    Summary=models.TextField() 
    Degree=models.TextField() 
    InstituteName=models.CharField(max_length=50)
    YearofGraduation=models.DateField()
    CompanyName=models.CharField(max_length=100)
    Position=models.CharField(max_length=100)
    YearsofExperience=models.CharField(max_length=100) 
    Skills=models.TextField()
    Hobbies=models.TextField()
    Achievements=models.TextField()
