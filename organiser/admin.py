from django.contrib import admin

from organiser.forms import OrganizerForm
from organiser.models import Organizer


# Register your models here.
@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    ...