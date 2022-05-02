from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet, CategoryViewSet, GenreViewSet,
    ReviewViewSet, CommentViewSet, TitleViewSet, SignUpGetTokenViewSet
)

app_name = 'api'

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('titles', TitleViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

router.register('auth', SignUpGetTokenViewSet)

urlpatterns = [
    # path('v1/auth/signup/', signup),
    # path('v1/auth/token/', get_token),
    path('v1/', include(router.urls)),
]
