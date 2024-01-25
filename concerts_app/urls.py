from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    ConciertoListView,
    ConciertoCreateView,
    ConciertoDetailView,
    ConciertoDeleteView,
    ConciertoUpdateView,
)

urlpatterns = [
    path("", ConciertoListView.as_view(), name="concierto_list"),
    path("detail/<int:pk>", ConciertoDetailView.as_view(), name="concierto_detail"),
    path("create/", ConciertoCreateView.as_view(), name="concierto_create"),
    path("delete/<int:pk>", ConciertoDeleteView.as_view(), name="concierto_delete"),
    path("update/<int:pk>", ConciertoUpdateView.as_view(), name="concierto_update"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
