from django.urls import path, include
from loginAPI.views import *

urlpatterns = [
    path('', defaultView),
    path('login', loginView),
    path('logout', logoutView),
    path('authorize', authView),
    path('register', registerView)

]
