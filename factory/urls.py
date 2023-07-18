from django.urls import path

from factory import views

urlpatterns = [
    path('create/', views.FactoryViewSet.as_view({'post': 'create'}), name='factory-create'),
    path('list/', views.FactoryViewSet.as_view({'get': 'list'}), name='factory-list'),
    path('<int:pk>/', views.FactoryViewSet.as_view({'get': 'retrieve'}), name='factory-list'),
]
