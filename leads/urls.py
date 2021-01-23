from django.urls import path
from .views import home_page, lead_detail, lead_create

app_name = "leads"
urlpatterns = [
    path("", home_page),
    path('<int:pk>/', lead_detail),
    path('create/', lead_create)
]
