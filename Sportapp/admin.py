from django.contrib import admin
from .models import Account,SuperAdmin,User


admin.site.register(Account)
admin.site.register(SuperAdmin)
admin.site.register(User)

# Register your models here.
