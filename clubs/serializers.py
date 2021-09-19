from rest_framework import serializers
from .models import Club, City, WorkingTime, Photo, Hall, Game, Table, Price, SocialNetwork

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'url']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['file']

class WorkingTimeSerializer(serializers.ModelSerializer):
    opening_time = serializers.TimeField(format='%H:%M')
    closing_time = serializers.TimeField(format='%H:%M')
    class Meta:
        model = WorkingTime
        fields = ['name', 'opening_time', 'closing_time']

class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ['name', 'address']

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['size']

class GameSerializer(serializers.ModelSerializer):
    tables = TableSerializer(many=True, read_only=True)
    name = serializers.CharField (
        source='get_name_display'
    )
    class Meta:
        model = Game
        fields = ['name', 'tables', 'hall']

class HallSerializer(serializers.ModelSerializer):
    games = GameSerializer(many=True, read_only=True)
    class Meta:
        model = Hall
        fields = ['name', 'games']

class PriceSerializer(serializers.ModelSerializer):
    working_times = WorkingTimeSerializer(many=True)
    tables = TableSerializer(many=True)
    class Meta:
        model = Price
        fields = ['tables', 'working_times', 'price_from', 'price_to', 'value']

class ClubSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    working_times = WorkingTimeSerializer(many=True, read_only=True)
    social_networks = SocialNetworkSerializer(many=True, read_only=True)
    halls = HallSerializer(many=True, read_only=True)
    prices = PriceSerializer(many=True, read_only=True)
    class Meta:
        model = Club
        fields = ['id', 'slug', 'district', 'city', 'name', 'address', 'photos', 'website', 'working_times', 'social_networks', 'phone', 'wardrobe', 'wc', 'air_conditioning', 'wifi', 'barroom', 'vip_hall', 'smoking_room', 'kitchen', 'sports_broadcasts', 'halls', 'prices', 'payment_methods', 'table_reservation']

class ClubCardSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Club
        fields = ['id', 'slug', 'name', 'address', 'photos',]