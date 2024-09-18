from django.urls import path
from django.contrib import admin
from . import views
from .views import custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
    path('flights/', views.flight_list, name='flight_list'),
    path('flights/edit/<int:flight_id>/', views.edit_flight, name='edit_flight'),
    path('flights/delete/<int:flight_id>/', views.delete_flight, name='delete_flight'),
    path('flights/add/', views.add_flight, name='add_flight'),
    path('flights/search/', views.search_flight, name='search_flight'),
    path('logout/', custom_logout, name='logout'),
]
