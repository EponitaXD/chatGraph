from django.urls import path
from .views import CreatePlot

from . import views

app_name = "experts"
urlpatterns = [
    path("create-plot/", CreatePlot.as_view(), name="create-plot"),
]
