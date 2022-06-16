from django.db.models import Prefetch
from .serializers import FoodListSerializer
from .models import FoodCategory, Food
from rest_framework import generics


class ListFoodsViewSet(generics.ListAPIView):
    """Возвращает json только с теми категориями, где у блюд is_publish=True"""
    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects.all()

    def get_queryset(self):
        query = self.queryset.prefetch_related(
            Prefetch("food", queryset=Food.objects.filter(is_publish=True))
        )
        queryset = [cat for cat in query if cat.food.exists()]

        return queryset
