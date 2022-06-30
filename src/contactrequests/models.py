from django.db import models

# Create your models here.


class ContactReq(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(null=True, max_length=255)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email
