from django.contrib import admin
from django.urls import include, path
from app.views import OrganizationCreate, EventCreate, EventDetail, EventListFilter
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

router = routers.DefaultRouter()
router.register(r'all', EventDetail, basename='all') #Вывод мероприятия с информацией о всех.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('organization/create/', OrganizationCreate.as_view()), #Создание организации
    path('event/', include(router.urls)), #роутер мероприятия
    path('event/create/', EventCreate.as_view()), #Создание мероприятия
    path('event/filter/', EventListFilter.as_view()), #Вывод мероприятий с возможностью фильтрации
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
