from django.contrib import admin

# Register your models here.
from emails_validation.models import EmailVal


class EmailValAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'date_created',)


admin.site.register(EmailVal, EmailValAdmin)