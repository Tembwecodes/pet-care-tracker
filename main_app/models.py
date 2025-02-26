from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    weight = models.FloatField()
    description = models.TextField(max_length=250)
    profile_picture = models.ImageField(upload_to='pets/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('pets_detail', kwargs={'pet_id': self.id})
    
    class Meta:
        ordering = ['name']

class MedicalRecord(models.Model):
    record_date = models.DateField()
    record_type = models.CharField(max_length=100)
    veterinarian = models.CharField(max_length=100)
    diagnosis = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.record_type} on {self.record_date}"
    
    class Meta:
        ordering = ['-record_date']

class Vaccination(models.Model):
    vaccine_name = models.CharField(max_length=100)
    date_administered = models.DateField()
    next_due_date = models.DateField()
    administered_by = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vaccine_name} on {self.date_administered}"
    
    class Meta:
        ordering = ['-date_administered']

class FeedingSchedule(models.Model):
    food_type = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    time_of_day = models.TimeField()
    notes = models.TextField(blank=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.food_type} at {self.time_of_day}"

class Medication(models.Model):
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    frequency = models.CharField(max_length=100)
    time_of_day = models.TimeField()
    notes = models.TextField(blank=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.medication_name} ({self.dosage})"
    
    class Meta:
        ordering = ['-start_date']

class TrainingProgress(models.Model):
    TRAINING_STATUS = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('mastered', 'Mastered'),
    )
    
    skill = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=TRAINING_STATUS,
        default='not_started'
    )
    start_date = models.DateField()
    notes = models.TextField(blank=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.skill}: {self.get_status_display()}"
    
    class Meta:
        ordering = ['status', 'skill']

class Photo(models.Model):
    image_file = models.ImageField(upload_to='pet_photos/')
    caption = models.CharField(max_length=250, blank=True)
    date_taken = models.DateField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for {self.pet.name} on {self.date_taken}"
    
    class Meta:
        ordering = ['-date_taken']