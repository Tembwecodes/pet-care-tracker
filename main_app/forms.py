# main_app/forms.py
from django import forms
from .models import MedicalRecord, Vaccination, FeedingSchedule, Medication, TrainingProgress, Photo

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['record_date', 'record_type', 'veterinarian', 'diagnosis', 'notes']
        widgets = {
            'record_date': forms.DateInput(attrs={'type': 'date'}),
        }

class VaccinationForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = ['vaccine_name', 'date_administered', 'next_due_date', 'administered_by', 'notes']
        widgets = {
            'date_administered': forms.DateInput(attrs={'type': 'date'}),
            'next_due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class FeedingScheduleForm(forms.ModelForm):
    class Meta:
        model = FeedingSchedule
        fields = ['food_type', 'amount', 'frequency', 'time_of_day', 'notes']
        widgets = {
            'time_of_day': forms.TimeInput(attrs={'type': 'time'}),
        }

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['medication_name', 'dosage', 'start_date', 'end_date', 'frequency', 'time_of_day', 'notes']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'time_of_day': forms.TimeInput(attrs={'type': 'time'}),
        }

class TrainingProgressForm(forms.ModelForm):
    class Meta:
        model = TrainingProgress
        fields = ['skill', 'status', 'start_date', 'notes']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image_file', 'caption', 'date_taken']
        widgets = {
            'date_taken': forms.DateInput(attrs={'type': 'date'}),
        }