from django.contrib import admin
from dashboard_app_main.models import AccumulatedTime,AxisFeedrate,Position, User
# Register your models here.
admin.site.register(User)
admin.site.register(AccumulatedTime)
admin.site.register(AxisFeedrate)
admin.site.register(Position)