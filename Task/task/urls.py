from django.urls import path, include
from rest_framework import routers
from task import views 

app_name='pets'


router = routers.DefaultRouter()
router.register(r'pet', views.PetViewSet)
router.register(r'price', views.PriceViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.pet_list, name='listing-pet'),
    path('<int:pk>/', views.pet_detail, name='detail-pet'),
    path('', views.price_list, name='listing-price'),
    path('<int:pk>/', views.price_detail, name='detail-price'),
]

