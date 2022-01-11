from rest_framework import serializers
from .models import Club, City, WorkingTime, Photo, Hall, Game, Table, Price, SocialNetwork, Promotion

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'url']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'file']

class WorkingTimeSerializer(serializers.ModelSerializer):
    opening_time = serializers.TimeField(format='%H:%M')
    closing_time = serializers.TimeField(format='%H:%M')
    class Meta:
        model = WorkingTime
        fields = ['id', 'name', 'opening_time', 'closing_time']

class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ['id', 'name', 'address']

class HallSerializer0(serializers.ModelSerializer):
    type = serializers.CharField (
        source='get_type_display'
    )
    class Meta:
        model = Hall
        fields = ['id', 'name', 'type',]

class TableSerializer(serializers.ModelSerializer):
    brand = serializers.CharField (
        source='get_brand_display'
    )
    cloth = serializers.CharField (
        source='get_cloth_display'
    )
    cues = serializers.CharField (
        source='get_cues_display'
    )
    balls = serializers.CharField (
        source='get_balls_display'
    )
    game = serializers.StringRelatedField()
    hall = HallSerializer0(read_only=True)
    type = serializers.CharField (
        source='get_type_display'
    )
    class Meta:
        model = Table
        fields = ['id', 'game', 'hall', 'size', 'brand', 'cloth', 'balls', 'cues', 'type']

class GameSerializer(serializers.ModelSerializer):
    tables = TableSerializer(many=True, read_only=True)
    name = serializers.CharField (
        source='get_name_display'
    )
    class Meta:
        model = Game
        fields = ['id', 'name', 'tables', 'hall']

class HallSerializer(serializers.ModelSerializer):
    games = GameSerializer(many=True, read_only=True)
    type = serializers.CharField (
        source='get_type_display'
    )
    class Meta:
        model = Hall
        fields = ['id', 'name', 'type', 'games']

class PriceSerializer(serializers.ModelSerializer):
    working_times = WorkingTimeSerializer(many=True)
    tables = TableSerializer(many=True)
    price_from = serializers.TimeField(format='%H:%M')
    price_to = serializers.TimeField(format='%H:%M')
    value = serializers.DecimalField(max_digits=5, decimal_places=0)
    class Meta:
        model = Price
        fields = ['id', 'tables', 'working_times', 'price_from', 'price_to', 'value']

class PromotionSerializer(serializers.ModelSerializer):
    customer_categories = serializers.CharField (
        source='get_customer_categories_display'
    )
    days_of_the_week = serializers.CharField (
        source='get_days_of_the_week_display'
    )
    type = serializers.CharField (
        source='get_type_display'
    )
    time_from = serializers.TimeField(format='%H:%M')
    time_to = serializers.TimeField(format='%H:%M')
    class Meta:
        model = Promotion
        fields = ['id', 'name', 'type', 'customer_categories', 'is_active', 'is_perpetual', 'time_from', 'time_to', 'discount', 'days_of_the_week']

class ClubSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    working_times = WorkingTimeSerializer(many=True, read_only=True)
    social_networks = SocialNetworkSerializer(many=True, read_only=True)
    halls = HallSerializer(many=True, read_only=True)
    prices = PriceSerializer(many=True, read_only=True)
    promotions = PromotionSerializer(many=True, read_only=True)
    payment_methods = serializers.CharField (
        source='get_payment_methods_display'
    )
    class Meta:
        model = Club
        fields = ['id', 'slug', 'district', 'city', 'name', 'address', 'photos', 'website', 'working_times', 'social_networks', 'phone', 'wardrobe', 'wc', 'air_conditioning', 'wifi', 'barroom', 'vip_hall', 'smoking_room', 'kitchen', 'sports_broadcasts', 'halls', 'prices', 'payment_methods', 'table_reservation', 'promotions', 'is_open', 'time_zone', 'is_pre_entry', 'is_medical_masks', 'works_since', 'is_qr_code', 'floor']

class ClubCardSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Club
        fields = ['id', 'slug', 'name', 'address', 'photos',]