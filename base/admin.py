from django.contrib import admin
from .models import User,Resource,Track,TrackParticipant
# Register your models here.
admin.site.register(User)
admin.site.register(Track)
admin.site.register(Resource)
admin.site.register(TrackParticipant)
