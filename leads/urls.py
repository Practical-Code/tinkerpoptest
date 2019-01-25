from django.conf.urls import url
from .views import LeadListCreate

urlpatterns = [
    url(r'^$', LeadListCreate.as_view()),
]