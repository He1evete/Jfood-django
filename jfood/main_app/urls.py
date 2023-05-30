from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('menu/', views.menu, name="menu"),
    path('reservation/', views.get_reserv, name='Reservation'),
    path('category/<int:pk>/', views.category_menu, name='category_menu'),
    path('', views.about, name='about'),
]
