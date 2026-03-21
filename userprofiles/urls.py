from django.urls import path
from . import views

urlpatterns = [
    path('profile/todos/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
    path('profile/editar/<int:pk>/', views.update_profile, name='update_profile'),
]