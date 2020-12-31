from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("portifolioprojetos", views.portifolioprojetos, name='portifolioprojetos'),
    path("portifoliodetails/<int:projeto_id>", views.portifoliodetails, name='portifoliodetails')
]
