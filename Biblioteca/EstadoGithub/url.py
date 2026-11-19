from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import GitHubEventViewSet

router = DefaultRouter();
router.register (r'Github',GitHubEventViewSet,basename='github')

GithubUrls = [
    path('',include(router.urls))
]

