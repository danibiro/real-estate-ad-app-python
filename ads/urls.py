from django.urls import path
from .views import AdViewWithoutParam, AdViewWithParam

urlpatterns = [
    path('', AdViewWithoutParam.as_view(), name='adWithoutParam'),
    path('<int:id>', AdViewWithParam.as_view(), name='adWithParam'),
]