# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('custom-logout/', views.logout_view, name='custom_logout'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pets/', views.pets_index, name='pets_index'),
    path('pets/<int:pet_id>/', views.pets_detail, name='pets_detail'),
    path('pets/create/', views.PetCreate.as_view(), name='pets_create'),
    path('pets/<int:pk>/update/', views.PetUpdate.as_view(), name='pets_update'),
    path('pets/<int:pk>/delete/', views.PetDelete.as_view(), name='pets_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    
    # Medical Records
    path('pets/<int:pet_id>/add_medical_record/', views.add_medical_record, name='add_medical_record'),
    path('medical_records/<int:pk>/update/', views.MedicalRecordUpdate.as_view(), name='medical_records_update'),
    path('medical_records/<int:pk>/delete/', views.MedicalRecordDelete.as_view(), name='medical_records_delete'),
    
    # Vaccinations
    path('pets/<int:pet_id>/add_vaccination/', views.add_vaccination, name='add_vaccination'),
    path('vaccinations/<int:pk>/update/', views.VaccinationUpdate.as_view(), name='vaccinations_update'),
    path('vaccinations/<int:pk>/delete/', views.VaccinationDelete.as_view(), name='vaccinations_delete'),
    
    # Feeding Schedules
    path('pets/<int:pet_id>/add_feeding_schedule/', views.add_feeding_schedule, name='add_feeding_schedule'),
    path('feeding_schedules/<int:pk>/update/', views.FeedingScheduleUpdate.as_view(), name='feeding_schedules_update'),
    path('feeding_schedules/<int:pk>/delete/', views.FeedingScheduleDelete.as_view(), name='feeding_schedules_delete'),
    
    # Medications
    path('pets/<int:pet_id>/add_medication/', views.add_medication, name='add_medication'),
    path('medications/<int:pk>/update/', views.MedicationUpdate.as_view(), name='medications_update'),
    path('medications/<int:pk>/delete/', views.MedicationDelete.as_view(), name='medications_delete'),
    
    # Training Progress
    path('pets/<int:pet_id>/add_training_progress/', views.add_training_progress, name='add_training_progress'),
    path('training_progress/<int:pk>/update/', views.TrainingProgressUpdate.as_view(), name='training_progress_update'),
    path('training_progress/<int:pk>/delete/', views.TrainingProgressDelete.as_view(), name='training_progress_delete'),
    
    # Photos
    path('pets/<int:pet_id>/add_photo/', views.add_photo, name='add_photo'),
    path('photos/<int:pk>/delete/', views.PhotoDelete.as_view(), name='photos_delete'),
]