from django.urls import path
from .views import *

app_name = "causes"

urlpatterns = [
    path('causes/', CauseViewSet.as_view({'post':'create', 'get':'list'}), name='causes'),
    path('causes/<int:pk>/', CauseViewSet.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy'}), name='causes_details'), 
   
    path('causes/<int:pk>/contribute/', ContributionViewSet.as_view({'post':'create'}), name='contribution'),
]