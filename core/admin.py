from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Forum)
admin.site.register(Answer)
admin.site.register(Vote)
