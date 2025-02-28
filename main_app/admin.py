from django.contrib import admin
from .models import Pet, MedicalRecord, Vaccination, FeedingSchedule, Medication, TrainingProgress, Photo

# Register your models here.

admin.site.register(Pet)
admin.site.register(MedicalRecord)
admin.site.register(Vaccination)
admin.site.register(FeedingSchedule)
admin.site.register(Medication)
admin.site.register(TrainingProgress)
admin.site.register(Photo)