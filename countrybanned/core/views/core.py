from countrybanned.core.views.base import *
from countrybanned.core.serializers import *


class CountryViewSet(viewsets.ModelViewSet, viewsets.GenericViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_object(self):
        return super(CountryViewSet, self).get_object()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        query = self.request.query_params.get('name', None)
        sort_by = self.request.query_params.get('sort_by', None)
        sort_type = self.request.query_params.get('sort_type', None)

        if query is not None:
            queryset = queryset.filter(name__icontains=query,)

        if sort_by is not None:
            if sort_type == 'desc':
                queryset = queryset.order_by('-' + str(sort_by))
            elif sort_type == 'asc':
                queryset = queryset.order_by(sort_by)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset.order_by('-name'), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return return_success(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return return_success(serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
