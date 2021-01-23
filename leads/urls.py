from django.urls import path
from .views import (home_page, lead_delete, lead_detail,
                    lead_create, lead_update, lead_delete)

app_name = "leads"
urlpatterns = [
    path("", home_page),
    path('<int:pk>/', lead_detail),
    path('create/', lead_create),
    path('<int:pk>/update/', lead_update),
    path('<int:pk>/delete/', lead_delete)
]
