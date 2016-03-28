from django.contrib import admin
from .forms import SignUpForm
# Register your models here.
from .models import SignUp


admin.site.register(SignUp)