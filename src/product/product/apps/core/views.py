from datetime import datetime

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from product.apps.core.renderers import ApiRenderer


class SoftDestroyModelMixin:
    """
    Soft destroy a model instance.
    """

    def perform_destroy(self, instance):
        instance.deleted_at = datetime.now()


class BaseViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  SoftDestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """

    renderer_classes = [ApiRenderer]
