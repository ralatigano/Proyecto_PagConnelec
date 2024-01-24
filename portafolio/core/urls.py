
from django.urls import path
from . import views
from portfolio.views import vistaProyectos

urlpatterns = [
    path('', views.home ,name="home"),
    path('about', views.about ,name="About me"),
    path('contact', views.contacto ,name="Contact"),
    path('portafolio', vistaProyectos ,name="portafolio"),
]
