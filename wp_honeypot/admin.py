"""Register WPHoneypotLog with the Django Model Admin."""
from django.contrib import admin
from .models import WPHoneypotLog


class WPHoneypotLogAdmin(admin.ModelAdmin):
    """Model admin. Show email and the timestamp the honeypot was filled out."""

    list_display = ('email', 'created',)


admin.site.register(WPHoneypotLog, WPHoneypotLogAdmin)
