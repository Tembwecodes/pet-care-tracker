# main_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pet, MedicalRecord, Vaccination, FeedingSchedule, Medication, TrainingProgress, Photo
from .forms import MedicalRecordForm, VaccinationForm, FeedingScheduleForm, MedicationForm, TrainingProgressForm, PhotoForm
from datetime import date, timedelta

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def pets_index(request):
    pets = Pet.objects.filter(user=request.user)
    return render(request, 'pets/index.html', {'pets': pets})

@login_required
def pets_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    
    # Check if the logged-in user owns this pet
    if pet.user != request.user:
        return redirect('pets_index')
    
    # Get related objects
    medical_records = pet.medicalrecord_set.all()
    vaccinations = pet.vaccination_set.all()
    feeding_schedules = pet.feedingschedule_set.all()
    medications = pet.medication_set.all()
    training_progress = pet.trainingprogress_set.all()
    photos = pet.photo_set.all()
    
    # Add these date variables for reminders
    today = date.today()
    today_plus_7 = today + timedelta(days=7)
    today_plus_30 = today + timedelta(days=30)
    
    # Forms for adding new related objects
    medical_record_form = MedicalRecordForm()
    vaccination_form = VaccinationForm()
    feeding_schedule_form = FeedingScheduleForm()
    medication_form = MedicationForm()
    training_progress_form = TrainingProgressForm()
    photo_form = PhotoForm()
    
    context = {
        'pet': pet,
        'medical_records': medical_records,
        'vaccinations': vaccinations,
        'feeding_schedules': feeding_schedules,
        'medications': medications,
        'training_progress': training_progress,
        'photos': photos,
        'medical_record_form': medical_record_form,
        'vaccination_form': vaccination_form,
        'feeding_schedule_form': feeding_schedule_form,
        'medication_form': medication_form,
        'training_progress_form': training_progress_form,
        'photo_form': photo_form,
        'today': today,
        'today_plus_7': today_plus_7,
        'today_plus_30': today_plus_30
    }
    
    return render(request, 'pets/detail.html', context)

# Pet CRUD classes
class PetCreate(LoginRequiredMixin, CreateView):
    model = Pet
    fields = ['name', 'species', 'breed', 'color', 'date_of_birth', 'weight', 'description', 'profile_picture']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    def form_invalid(self, form):
        print("Form errors:", form.errors)
        return super().form_invalid(form)

class PetUpdate(LoginRequiredMixin, UpdateView):
    model = Pet
    fields = ['name', 'species', 'breed', 'color', 'date_of_birth', 'weight', 'description', 'profile_picture']
    
    def dispatch(self, request, *args, **kwargs):
        pet = self.get_object()
        if pet.user != self.request.user:
            return redirect('pets_index')
        return super().dispatch(request, *args, **kwargs)

class PetDelete(LoginRequiredMixin, DeleteView):
    model = Pet
    success_url = '/pets/'
    
    def dispatch(self, request, *args, **kwargs):
        pet = self.get_object()
        if pet.user != self.request.user:
            return redirect('pets_index')
        return super().dispatch(request, *args, **kwargs)

# Authentication
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pets_index')
        else:
            error_message = 'Invalid sign up - try again'
    
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# Related Model Add Views
@login_required
def add_medical_record(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    if pet.user != request.user:
        return redirect('pets_index')
    
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.pet = pet
            new_record.save()
            return redirect('pets_detail', pet_id=pet_id)
    
    return redirect('pets_detail', pet_id=pet_id)

@login_required
def add_vaccination(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    if pet.user != request.user:
        return redirect('pets_index')
    
    if request.method == 'POST':
        form = VaccinationForm(request.POST)
        if form.is_valid():
            new_vaccination = form.save(commit=False)
            new_vaccination.pet = pet
            new_vaccination.save()
            return redirect('pets_detail', pet_id=pet_id)
    
    return redirect('pets_detail', pet_id=pet_id)

@login_required
def add_feeding_schedule(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    if pet.user != request.user:
        return redirect('pets_index')
    
    if request.method == 'POST':
        form = FeedingScheduleForm(request.POST)
        if form.is_valid():
            new_schedule = form.save(commit=False)
            new_schedule.pet = pet
            new_schedule.save()
            return redirect('pets_detail', pet_id=pet_id)
    
    return redirect('pets_detail', pet_id=pet_id)

@login_required
def add_medication(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    if pet.user != request.user:
        return redirect('pets_index')
    
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            new_medication = form.save(commit=False)
            new_medication.pet = pet
            new_medication.save()
            return redirect('pets_detail', pet_id=pet_id)
    
    return redirect('pets_detail', pet_id=pet_id)

@login_required
def add_training_progress(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    if pet.user != request.user:
        return redirect('pets_index')
    
    if request.method == 'POST':
        form = TrainingProgressForm(request.POST)
        if form.is_valid():
            new_progress = form.save(commit=False)
            new_progress.pet = pet
            new_progress.save()
            return redirect('pets_detail', pet_id=pet_id)
    
    return redirect('pets_detail', pet_id=pet_id)

@login_required
def add_photo(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    if pet.user != request.user:
        return redirect('pets_index')
    
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = form.save(commit=False)
            new_photo.pet = pet
            new_photo.save()
            return redirect('pets_detail', pet_id=pet_id)
    
    return redirect('pets_detail', pet_id=pet_id)



# Generic Update and Delete Views for Related Models
class MedicalRecordUpdate(LoginRequiredMixin, UpdateView):
    model = MedicalRecord
    fields = ['record_date', 'record_type', 'veterinarian', 'diagnosis', 'notes']
    
    def dispatch(self, request, *args, **kwargs):
        record = self.get_object()
        if record.pet.user != self.request.user:
            return redirect('pets_index')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return f'/pets/{self.object.pet.id}/'

class MedicalRecordDelete(LoginRequiredMixin, DeleteView):
    model = MedicalRecord
    
    def dispatch(self, request, *args, **kwargs):
        record = self.get_object()
        if record.pet.user != self.request.user:
            return redirect('pets_index')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return f'/pets/{self.object.pet.id}/'

class VaccinationUpdate(LoginRequiredMixin, UpdateView):
    model = Vaccination
    fields = ['vaccine_name', 'date_administered', 'next_due_date', 'administered_by', 'notes']
    
    def dispatch(self, request, *args, **kwargs):
        vaccination = self.get_object()
        if vaccination.pet.user != self.request.user:
            return redirect('pets_index')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return f'/pets/{self.object.pet.id}/'

class VaccinationDelete(LoginRequiredMixin, DeleteView):
    model = Vaccination
    
    def dispatch(self, request, *args, **kwargs):
        vaccination = self.get_object()
        if vaccination.pet.user != self.request.user:
            return redirect('pets_index')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return f'/pets/{self.object.pet.id}/'

class FeedingScheduleUpdate(LoginRequiredMixin, UpdateView):
    model = FeedingSchedule
    fields = ['food_type', 'amount', 'frequency', 'time_of_day', 'notes']
    
    def dispatch(self, request, *args, **kwargs):
        schedule = self.get_object()
        if schedule.pet.user != self.request.user:
            return redirect('pets_index')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return f'/pets/{self.object.pet.id}/'

class FeedingScheduleDelete(LoginRequiredMixin, DeleteView):
    model = FeedingSchedule
    
    def dispatch(self, request, *args, **kwargs):
        schedule = self.get_object()
        if schedule.pet.user != self.request.user:
            return redirect('pets_index')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return f'/pets/{self.object.pet.id}/'

class MedicationUpdate(LoginRequiredMixin, UpdateView):
    model = Medication
    fields = ['medication_name', 'dosage', 'start_date', 'end_date', 'frequency', 'time_of_day', 'notes']
    
    def dispatch(self, request, *args, **kwargs):
        medication = self.get_object()
        if medication.pet.user != self.request.user:
            return redirect('pets_index')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return f'/pets/{self.object.pet.id}/'

class MedicationDelete(LoginRequiredMixin, DeleteView):
    model = Medication
    
    def dispatch(self, request, *args, **kwargs):
        medication = self.get_object()
        if medication.pet.user != self.request.user:
            return redirect('pets_index')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return f'/pets/{self.object.pet.id}/'

class TrainingProgressUpdate(LoginRequiredMixin, UpdateView):
    model = TrainingProgress
    fields = ['skill', 'status', 'start_date', 'notes']
    
    def dispatch(self, request, *args, **kwargs):
        progress = self.get_object()
        if progress.pet.user != self.request.user:
            return redirect('pets_index')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return f'/pets/{self.object.pet.id}/'

class TrainingProgressDelete(LoginRequiredMixin, DeleteView):
    model = TrainingProgress
    
    def dispatch(self, request, *args, **kwargs):
        progress = self.get_object()
        if progress.pet.user != self.request.user:
            return redirect('pets_index')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return f'/pets/{self.object.pet.id}/'

class PhotoDelete(LoginRequiredMixin, DeleteView):
    model = Photo
    
    def dispatch(self, request, *args, **kwargs):
        photo = self.get_object()
        if photo.pet.user != self.request.user:
            return redirect('pets_index')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return f'/pets/{self.object.pet.id}/'

def logout_view(request):
    auth_logout(request)
    return redirect('home')