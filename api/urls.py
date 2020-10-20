from django.urls import path
from api.views import dog_index, dog_delete, dog_show, dog_store, dog_update

urlpatterns = [
    path('dog/store/', dog_store),
    path('dog/delete/<id>', dog_delete),
    path('dog/update/<id>', dog_update),
    path('dog/show/<id>/', dog_show),
    path('dog/index', dog_index),
]