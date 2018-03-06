from rest_framework.pagination import LimitOffsetPagination


class ItemLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10