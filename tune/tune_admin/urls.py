from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import TutorialBotView

urlpatterns = [
    path('home', admin.site.urls),
    path('webhooks/tutorial/', csrf_exempt(TutorialBotView.as_view())),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
