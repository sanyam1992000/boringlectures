from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from notes import views as notes_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', notes_views.home, name='home'),
    path('<int:content_id>/', notes_views.get_notes, name='get-notes'),
    path('notes/', notes_views.GetNotes.as_view(), name='notes'),

]


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
