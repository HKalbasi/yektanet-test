from django.contrib import admin
from advertiser_mangement.models import Ad, Advertiser, Click, View

class ClickAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)

class AdAdmin(admin.ModelAdmin):
  list_filter = ('approved',)
  search_fields = ['title']

# Register your models here.
admin.site.register(Ad, AdAdmin)
admin.site.register(Advertiser)
admin.site.register(Click, ClickAdmin)
admin.site.register(View)