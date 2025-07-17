from django.urls import path
from .views import LostItemCreateView, LostItemListView, LostItemDetailView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lost-items/', LostItemListView.as_view(), name='lostitem_list'),
    path('lost-items/report/', LostItemCreateView.as_view(), name='lostitem_report'),
    path('lost-items/<int:pk>/', LostItemDetailView.as_view(), name='lostitem_detail'),
]
