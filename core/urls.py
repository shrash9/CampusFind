from django.urls import path
from django.contrib import admin
from .views import HomeLostItemListView, LostItemCreateView, LostItemListView, LostItemDetailView, LostItemUpdateView, LostItemDeleteView
from django.urls import path, include
from . import views
from .views import LostItemUpdateView, LostItemDeleteView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', LostItemListView.as_view(), name='lostitem_list'),
    path('report/', LostItemCreateView.as_view(), name='lostitem_report'),
    path('<int:pk>/', LostItemDetailView.as_view(), name='lostitem_detail'),
    path('admin/', admin.site.urls),
    path('<int:pk>/edit/', LostItemUpdateView.as_view(), name='lostitem_edit'),
    path('<int:pk>/delete/', LostItemDeleteView.as_view(), name='lostitem_delete'),
    path('', HomeLostItemListView.as_view(), name='home'),
]
