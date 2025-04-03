# crud- urls.py file new

from django.urls import path
from crud.views import *

urlpatterns = [

    path('', emp),
    path('emp', emp, name='emp'),  # Fix: Add this route for POST requests  
    path('show', show),  
    path('edit/<int:id>', edit),  
    path('update/<int:id>', update),  
    path('delete/<int:id>', destroy), 
    
]
