from django.contrib import admin
from django.urls import path
from api.views import ListFoodsViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/foods/', ListFoodsViewSet.as_view()),
]
