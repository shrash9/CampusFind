from django.urls import path
from django.contrib import admin
from .views import LostItemCreateView, LostItemListView, LostItemDetailView
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', LostItemListView.as_view(), name='lostitem_list'),
    path('report/', LostItemCreateView.as_view(), name='lostitem_report'),
    path('<int:pk>/', LostItemDetailView.as_view(), name='lostitem_detail'),
    path('admin/', admin.site.urls),
    # path('', include('core.urls')),
]
