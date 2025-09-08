from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('chickens/', views.chicken_index, name='chicken-index'),
    path('chickens/<int:chicken_id>/', views.chicken_detail, name='chicken-detail'),
    path('chickens/create/', views.ChickenCreate.as_view(), name='chicken-create'),
    path('chickens/<int:pk>/update/', views.ChickenUpdate.as_view(), name='chicken-update'),
    path('chickens/<int:pk>/delete/', views.ChickenDelete.as_view(), name='chicken-delete'),
    path('chickens/<int:chicken_id>/add-escape/', views.add_escape, name='add-escape'),
    path('accounts/signup/', views.signup, name='signup'),
    
]