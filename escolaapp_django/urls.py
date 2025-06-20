"""
URL configuration for escolaapp_django project.

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('alunos/', include('students.urls', namespace='students')),
    path('especializacoes/', include('specializations.urls', namespace='specializations')),
    path('professores/', include('teachers.urls', namespace='teachers')),
    path('materiais/', include('supplies.urls', namespace='supplies')),
    path('salas/', include('rooms.urls', namespace='rooms')),
    path('cursos/', include('classes.urls', namespace='classes')),
    path('contas/', include('accounts.urls', namespace='accounts')),
    path('matriculas/', include('enrollments.urls', namespace='enrollments')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
