from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(booking)
admin.site.register(Truckpartner)
admin.site.register(fleet)
admin.site.register(billing)
