from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'wiki'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),   
    path('upload/', views.upload_file, name='upload'),
    path('<str:pk>/edit',views.edit_page, name='edit_page'),
    path('<str:pk>/save',views.save_page, name='save_page'),
    path('<str:pk>/', views.view_page, name='detail'),
 
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
