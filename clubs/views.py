from rest_framework import viewsets
from .serializers import ClubSerializer, ClubCardSerializer, CitySerializer
from .models import Club, City

class ClubViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        city = City.objects.get(url=(self.request.query_params.get('city')))
        return Club.objects.filter(city=city).filter(is_verified=True).filter(is_active=True)
    serializer_class = ClubSerializer
    lookup_field = 'slug'

class ClubCardViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        city = City.objects.get(url=(self.request.query_params.get('city')))
        quantity = int(self.request.query_params.get('quantity'))
        if quantity:
            return Club.objects.filter(city=city).filter(is_verified=True).filter(is_active=True)[:quantity]
        else:
            return Club.objects.filter(city=city).filter(is_verified=True).filter(is_active=True)
    serializer_class = ClubCardSerializer
    lookup_field = 'slug'

class SitemapClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.filter(is_verified=True).filter(is_active=True)
    serializer_class = ClubSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'url'