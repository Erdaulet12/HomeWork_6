from django.urls import path
from . import views

urlpatterns = [
    path('items/<str:model>/', views.ItemListView.as_view(), name='item-list'),
    path('items/<str:model>/<int:pk>/',
         views.ItemDetailView.as_view(), name='item-detail'),
]
