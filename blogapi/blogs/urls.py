from django.urls import path

from .views import PostList, PostDetail

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Post API')

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path(r"swagger-docs/", schema_view)
]