from django_filters import rest_framework as filters

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    # фильтр по id
    id = filters.ModelMultipleChoiceFilter(
        field_name='id',
        to_field_name='id',
        queryset=Advertisement.objects.all(),
    )

    # фильтр по status
    status = filters.MultipleChoiceFilter(
        choices=AdvertisementStatusChoices.choices
    )

    #фильтр по дате
    created_at=filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ('id', 'status', 'created_at', 'updated_at')

