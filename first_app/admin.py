from django.contrib import admin
from first_app.models import Topic,WebPage,AccessRecord
from first_app.models import UserProfileInfos
# Register your models here.


admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)
admin.site.register(UserProfileInfos)
