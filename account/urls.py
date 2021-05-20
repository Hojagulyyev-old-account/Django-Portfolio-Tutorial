from django.urls import path

from . import views

urlpatterns = [
    # Router => HomePage
    path('', views.index, name='index'),
    # Router => AccountLogin
    path('account/login/', views.loginView, name='login'),
]
