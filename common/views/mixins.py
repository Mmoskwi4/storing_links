from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

class ExtendetGenericView(GenericViewSet):
    pass


class ListViewSet(ExtendetGenericView, mixins.ListModelMixin):
    pass



class CRUViewSet(ExtendetGenericView, 
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin):
    pass


class CRUDViewSet(CRUViewSet, mixins.DestroyModelMixin):
    pass