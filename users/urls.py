from . import views
from django.urls import path
from .views import HomePageView
from django.views.generic.base import TemplateView
from rest_framework.routers import SimpleRouter
from .views import UserViewSet

urlpatterns = [
    # # path('accounts/login/', views.LoginView.as_view(), name='login'),
    # path('', HomePageView.as_view(), name='home'),
    # path('signup/', views.signup, name='signup'),
    # # path('signup/', SignUpView.as_view(), name='signup'),
    # # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    


    # User Registration
    path('register/', views.user_registration, name='user-registration'),

    # User Login
    path('login/', views.user_login, name='user-login'),

    # Password Reset
    path('password-reset/', views.password_reset, name='password-reset'),
    


]


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
urlpatterns =  urlpatterns + router.urls