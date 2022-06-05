from django.urls import path
from UserAndRole import views

urlpatterns = [
    path(r'user/', views.user_list),
]
