from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Counselling)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Gmail)
admin.site.register(Phone)
admin.site.register(Notes)


admin.site.register(CounsellingPhysical)
admin.site.register(CategoryPhysical)
admin.site.register(ImagePhysical)
admin.site.register(GmailPhysical)
admin.site.register(PhonePhysical)
admin.site.register(NotesPhysical)



