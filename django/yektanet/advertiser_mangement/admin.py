from django.contrib import admin
from advertiser_mangement.models import Ad, Advertiser, Click, View

class ClickAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)

# Register your models here.
admin.site.register(Ad)
admin.site.register(Advertiser)
admin.site.register(Click, ClickAdmin)
admin.site.register(View)