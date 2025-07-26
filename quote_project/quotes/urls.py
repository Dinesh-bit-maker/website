from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data/', views.quote_success, name='data'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('services1/', views.services1, name='services1'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('blog/', views.blog, name='blog'),
    path('pricing/', views.pricing, name='pricing')
]
