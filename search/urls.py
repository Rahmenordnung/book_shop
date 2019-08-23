from django.urls import path
from .views import search_function

app_name = 'search'

urlpatterns = [
  path('', search_function, name='search')
  # url(r'^$', search_function, name='search')
]