from django.urls import path
from .views import *

urlpatterns = [
    path('', main),
    path('catalog/<int:category_id>/', catalog),
    path('catalog/tag/<int:tag_id>/', catalog_tag)
]