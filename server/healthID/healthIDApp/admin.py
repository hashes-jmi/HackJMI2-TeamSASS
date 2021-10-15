from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(base_user)
admin.site.register(address)
admin.site.register(basic_medical)
admin.site.register(Hospital)
admin.site.register(Allergies)
admin.site.register(Surgery)
admin.site.register(Disease)
admin.site.register(person)
admin.site.register(organization)