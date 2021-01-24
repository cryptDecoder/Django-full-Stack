
from django.contrib import admin
from django.urls import path, include
from leads.views import SignupView, HomePage
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomePage.as_view(), name="home"),
    path('leads/', include("leads.urls", namespace="leads")),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('signup/', SignupView.as_view(), name='signup'),
    path("agents/", include('agents.urls',namespace="agents"))

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
