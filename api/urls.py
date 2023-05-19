from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from api.views.buyers import BuyerViewSet
from api.views.code_confirmation import CodeConfirmView, CodeConfirmVerifyView
from api.views.companies import CompanyViewSet, MerchantViewSet
from api.views.image import ImageViewSet
from api.views.login import LoginView
from api.views.main import MainView
from api.views.orders import OderViewSet, OrderExportView
from api.views.products import CategoryViewSet, ProductViewSet
from api.views.users import User as UserMe, SettingsRetrieveAPIView, SettingsUpdateAPIView, SettingsCreateAPIView

router = DefaultRouter()
router.include_root_view = False
router.register('categories', CategoryViewSet, basename='categories')
router.register('products', ProductViewSet, basename='products')

router.register('buyers', BuyerViewSet, basename='buyers')
router.register('companies', CompanyViewSet, basename='companies')
router.register('merchants', MerchantViewSet, basename='merchants')
router.register('images', ImageViewSet, basename='images')
router.register('orders', OderViewSet, basename='orders')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('main/', MainView.as_view(), name='main'),
    path('token/refresh/', jwt_views.token_refresh, name='token-refresh'),
    path('token/verify/', jwt_views.token_verify, name='token-verify'),
    path('token/blacklist/', jwt_views.token_blacklist, name='token-blacklist'),
    path('user/me/', UserMe.as_view(), name='user-me'),
    path('settings/', SettingsRetrieveAPIView.as_view(), name='settings'),
    path('settings/create/', SettingsCreateAPIView.as_view(), name='settings-create'),
    path('settings/update/', SettingsUpdateAPIView.as_view(), name='settings-update'),
    path('code-confirmation/', CodeConfirmView.as_view(), name='code-confirmation'),
    path('code-confirmation/verify/', CodeConfirmVerifyView.as_view(), name='code-confirmation'),

    path('', include(router.urls)),
    path('orders/export/<int:order_id>/', OrderExportView.as_view(), name='orders-export'),
]
