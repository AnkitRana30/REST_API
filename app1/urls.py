from django.urls import path
from .views import *
urlpatterns = [
    path('create_row/',CreatUser.as_view(),name='create_row'),
    path('retrive/',RetriveData.as_view(),name='retrive'),
    path('update_data/<int:pk>',UpdateData.as_view(),name='update_data'),
    path('delete_data/<int:pk>',DeleteData.as_view(),name='delete_data')
]
