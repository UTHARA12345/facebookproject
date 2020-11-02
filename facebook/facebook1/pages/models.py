from django.db import models
import uuid
# Create your models here.

class Fbuser(models.Model):
    fb_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fb_name = models.CharField(max_length=30)
    fb_email = models.EmailField()
    fb_password = models.CharField(max_length=30)
    fb_dp = models.ImageField(upload_to='users/', null=True, blank=True)


    def __str__(self):
        return self.fb_name