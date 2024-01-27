from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from app.views import RegisterUserView, UserView, AllUsersView, OrganizationCreate
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('admin/', admin.site.urls),
    #path('', AllUsersView.as_view()),
    #path('user/', UserView.as_view()),
    #path('register/', RegisterUserView.as_view()),
    #Создание мероприятия
    #Вывод мероприятия с информацией о всех.
    #Вывод мероприятий с возможностью фильтрации
    path('orgcre/', OrganizationCreate.as_view()), #Создание организации
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
