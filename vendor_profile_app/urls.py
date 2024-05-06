from django.urls import path
from django.urls import include

# from hype_api.post_activity.post_activity_api import PostsOfUserAPI
# from reset_password.views import ResetPasswordView
# from .user_authentication.user_authentication_api import *
# from hype_api.introduction_app.api import AppIntroAPI
# from hype_api.user_authentication.update_email_api import *
# from hype_api.user_authentication.update_mobile_api import *
# from hype_api.user_authentication.user_authentication_api import *
# from hype_api.user_profile.user_profile_api import *
# from hype_api.account_setting.account_setting_api import *
# from hype_api.user_profile_activity.user_profile_activity_api import *
# from hype_api.account_setting.account_setting_api import *
# from hype_api.reset_password import api

# router = routers.DefaultRouter(trailing_slash=False)
# router.register("reset-password", ResetPasswordView, basename="reset_password")





from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet

router = DefaultRouter()
router.register(r'', VendorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
