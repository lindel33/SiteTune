from django.urls import path, include

urlpatterns = [
    path('', include('tune_admin.urls')),
]
