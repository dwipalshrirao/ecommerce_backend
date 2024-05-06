"""ecommerce_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        #  add your swagger doc title
        title="vendors API",
        #  version of the swagger doc
        default_version='v1',
        # first line that appears on the top of the doc
        description="Ecommerce vendors APIs Documentation",
    ),
    public=True,
    permission_classes=()
)
urlpatterns = [
    re_path(f'^swagger/$', schema_view.with_ui('swagger',
        cache_timeout=0), name='schema-swagger-ui'),
        
    path('admin/', admin.site.urls),
    path('vendors/', include('vendor_profile_app.urls')),
    path('purchase_orders/', include('orders_tracking_app.urls')),
]
