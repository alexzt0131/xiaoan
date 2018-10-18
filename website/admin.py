from django.contrib import admin

# Register your models here.
from website.models import Info, User, New, Photo

admin.site.register(Info)
admin.site.register(User)
admin.site.register(New)
admin.site.register(Photo)