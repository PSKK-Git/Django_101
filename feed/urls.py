from django.urls import path
from .views import HomePageView, PostDetailView, product_detail,subproduct_detail,subpost_detail,home
from . import views

app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('subproduct/<int:pk>/', views.subproduct_detail, name='subproduct_detail'),
    path('subpost/<int:pk>/', views.subpost_detail, name='subpost_detail'),
    path('', home, name='home'),
    # path('detail/subpost/<int:pk>/', views.subpost_detail, name='detail_subpost_detail'),

]