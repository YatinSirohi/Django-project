from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.store_view, name='store'),       #passing store view as default page.
    path('tub/', views.tub_view, name = 'tub'),
    path('<int:store_id>', views.details, name = 'details'),    #To get the store information in detail
   
] 