from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('', views.index, name='index'),    # boards 뒤에 아무것도 붙지 않는다는 의미
]