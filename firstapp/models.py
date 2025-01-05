from django.db import models


class Registration(models.Model):
    # Person Information
    person_name = models.CharField(max_length=255)
    person_mobile_no = models.CharField(max_length=15)
    adhar_no = models.CharField(max_length=12)
    
    # File Uploads
    adhar_front = models.ImageField(upload_to='uploads/adhar/', null=True, blank=True)
    adhar_back = models.ImageField(upload_to='uploads/adhar/', null=True, blank=True)
    institute_reg_copy = models.ImageField(upload_to='uploads/institute/', null=True, blank=True)

    # Institute Information
    institute_name = models.CharField(max_length=255)
    institute_govt_reg_no = models.CharField(max_length=255)
    institute_website = models.URLField()

    # Password Management
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)

    def __str__(self):
        return self.person_name

