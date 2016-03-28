from django.db import models

# Create your models here.


class SignUp(models.Model):
    email = models.EmailField()#something_else = models.CharField(max_length = 120 )
    full_name = models.CharField(
                    default='',
                    max_length=120,
                    blank=True,
                    null=True
                    )
    time_stamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):  # Python 3.3 is __str__
        return self.email
