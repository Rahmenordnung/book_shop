from django.urls import url
from .views import search_function

urlpatterns = [
  # path('', search_function, name='search')
  url(r'^$', search_function, name='search')
]