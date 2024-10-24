from django.urls import path
from .views import registro_usuario_View, editar_usuario_View, PasswordChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
#from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
   path('registrarse/', registro_usuario_View.as_view(), name='registrarse'),
   path('editar_perfil/', editar_usuario_View.as_view(), name='editar_perfil'),
   #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
   path('password/', PasswordChangeView.as_view(template_name='registration/change-password.html')),
   path('password_succes/', views.password_success, name='password_succes'), #se corrigio
   path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
   path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
   path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
]
