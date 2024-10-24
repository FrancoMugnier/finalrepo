from django.urls import path
from .import views
from .views import HomeView, detalle_articulo_View, agregar_post_View, update_post_View, eliminar_post_View, categoria_post_View, categoryView, categoryListView, LikeView, AddCommentView, AcercaDeView, ContactoView
urlpatterns = [
   # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
   path('articulo/<int:pk>/', detalle_articulo_View.as_view(), name='detalle-articulo'),
   path('agregar-post/', agregar_post_View.as_view(), name='agregar-post'),
   path('agregar-categoria/', categoria_post_View.as_view(), name='agregar-categoria'),
   path('articulo/editar/<int:pk>', update_post_View.as_view(), name='editar-articulo'),
   path('articulo/<int:pk>/eliminar/', eliminar_post_View.as_view(), name='eliminar-articulo'),
   path('categoria/<str:cats>/', categoryView, name='category'),
   path('categoria-lista/', categoryListView , name='category-list'),
   path('like/<int:pk>/', LikeView, name='like_post'),
   path('articulo/<int:pk>/comentario', AddCommentView.as_view(), name='add_comment'),
   path('acerca-de/', AcercaDeView.as_view(), name='acerca_de'),  #ruta para la vista AcercaDe
   path('contacto/', ContactoView.as_view(), name='contacto'),  #ruta para la vista contacto
   #esto nuevooo....

   path('filtrar_por_fecha/', views.filter_by_date, name='filter_by_date'),
   path('posts/<int:year>/<int:month>/', views.posts_by_date, name='posts_by_date'),

]
