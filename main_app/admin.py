from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.

admin.site.register(Type)
admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Project)
admin.site.register(Option)
admin.site.register(Answer)
admin.site.register(F1)
admin.site.register(F2)
