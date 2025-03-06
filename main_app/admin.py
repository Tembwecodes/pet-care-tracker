from django.contrib import admin
# main_app/admin.py
from .models import Pet, MedicalRecord, Vaccination, FeedingSchedule, Medication, TrainingProgress, Photo, Veterinarian, Appointment

# Register your models here
admin.site.register(Pet)
admin.site.register(MedicalRecord)
admin.site.register(Vaccination)
admin.site.register(FeedingSchedule)
admin.site.register(Medication)
admin.site.register(TrainingProgress)
admin.site.register(Photo)
admin.site.register(Veterinarian)
admin.site.register(Appointment)