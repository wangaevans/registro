from django.contrib import admin
from .models import User,Material,HuaweiTrack,Participant
# Register your models here.
admin.site.register(User)
admin.site.register(HuaweiTrack)
admin.site.register(Material)
admin.site.register(Participant)
# admin.site.register(TrackParticipant)
