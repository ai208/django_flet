from django.contrib import admin
from .models import Weight,Routine,RoutineRecord
# Register your models here.
admin.site.register(Weight)
admin.site.register(Routine)
admin.site.register(RoutineRecord)