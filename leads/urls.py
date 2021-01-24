from django.urls import path
from .views import (LeadListView, lead_delete, lead_detail, LeadDetailView,
                    lead_create, lead_update, LeadCreateView, LeadUpdateView)

app_name = "leads"
urlpatterns = [
    path("", LeadListView.as_view(), name='lead_list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('create/', LeadCreateView.as_view(), name='lead_create'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead_update'),
    path('<int:pk>/delete/', lead_delete, name='lead_delete')
]
