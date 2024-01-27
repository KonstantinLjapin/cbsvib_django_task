from django.contrib import admin
from django.urls import include, path
from app.views import OrganizationCreate, EventCreate
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('organization/create/', OrganizationCreate.as_view()), #Создание организации
    path('event/create/', EventCreate.as_view()), #Создание мероприятия
    #path('event/all/', EventCreate.as_view()), #Вывод мероприятия с информацией о всех.
    #path('event/filter/', EventCreate.as_view()),     #Вывод мероприятий с возможностью фильтрации
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
