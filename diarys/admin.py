from django.contrib import admin
from .models import Routine, Routine_detail, Routine_comment
# Register your models here.

admin.site.register(Routine)
admin.site.register(Routine_detail)
admin.site.register(Routine_comment)