from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ClubViewSet, ClubCardViewSet, CityViewSet, SitemapClubViewSet

router = SimpleRouter()
router.register('clubs', ClubViewSet, basename='club')
router.register('card-clubs', ClubCardViewSet, basename='card_club')
router.register('sitemap-clubs', SitemapClubViewSet, basename='sitemap_club')
router.register('cities', CityViewSet, basename='city')

urlpatterns = [
    path('', include(router.urls))
]