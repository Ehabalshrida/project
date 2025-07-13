"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
# Import static files handling
from django.conf import settings
from django.conf.urls.static import static
# from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # name is used to refer to the URL in templates and redirects, and it is optional
    path('app/', include('app.urls'), name='app'),
    # Include Django's built-in authentication URLs
    # This will include login, logout, password change, and password reset views
    path('accounts/', include('django.contrib.auth.urls')),
    # Redirect root URL to app
    path('', RedirectView.as_view(url='app/', permanent=True)),  
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
