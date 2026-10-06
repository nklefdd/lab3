from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("exchange/", include("exchange.urls")),
    path("", include("faculty.urls")),
    path("admin/", admin.site.urls),
]
