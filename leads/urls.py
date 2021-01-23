from django.urls import path
from .views import home_page, lead_detail

app_name = "leads"
urlpatterns = [
    path("", home_page),
    path('<pk>', lead_detail)
]
