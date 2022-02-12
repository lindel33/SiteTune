from django.urls import path, include

urlpatterns = [
    path('', include('tune_admin.urls')),
    path('/api/', include('bot_telegram.urls')),
]
