from .models import House, City, room, Floor, Area, Direction
import django_filters
from django.db.models import Q


# Filter house by city, bedroom number, floor and area
class HouseFilter(django_filters.FilterSet):
    
    # q = django_filters.CharFilter(field_name='description', lookup_expr='icontains', label="Keywords")
    q = django_filters.CharFilter(method='my_custom_filter')
    city = django_filters.ChoiceFilter(field_name='community__city', choices=City.choices,
                                         label='城市')
    bedroom = django_filters.ChoiceFilter(field_name='bedroom', choices=room.choices,
                                         label='房型')
    area = django_filters.ChoiceFilter(field_name='area_class', choices=Area.choices,
                                         label='面積')
    floor = django_filters.ChoiceFilter(field_name='floor', choices=Floor.choices,
                                         label='樓層')
    direction = django_filters.ChoiceFilter(field_name='direction', choices=Direction.choices,
                                        label='描述')


    def my_custom_filter(self, queryset, q, value):
        return queryset.filter(Q(description__icontains=value) | Q(community__name__icontains=value))


    class Meta:
        model = House
        fields = {
            # 'title': ['icontains'],
            # 'category__name': ['icontains'],
            # 'pub_date': ['date__gte'],
        }

