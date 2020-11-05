from django.db import transaction
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from django_filters.rest_framework import DjangoFilterBackend
from advertisements.serializers import AdvertisementSerializer
from advertisements.models import Advertisement

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class=AdvertisementSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdvertisementFilter


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        #print("Удаление внутри транзакции")
        # Получаем имя пользователя, который сделал запрос
        ad_user = request.user
        #получаем имя пользователя, который создал сущность, которую нужно удалить
        instance = self.get_object()
        creator_ad=instance.creator

        if ad_user != creator_ad:
            raise ValidationError({"Advertisement": "Удалять можно только свои записи!"})

        return super().destroy(request, *args, **kwargs)


