from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import (
    RetrieveModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
)
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from .serializers import ClassSerializer, StudentSerializer
from .models import Class, Student
from .views import download_class_data as downloader


class ClassViewSet(ModelViewSet):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()
    model = Class

    @action(methods=["GET"], url_name="download", url_path="download", detail=True)
    def download_class_data(self, request, pk=None, format=None, *args, **kwargs):
        """
        Download class data in the specified format using the query parameter
        `file-format` e.g `/api/{version}/class/61399/download/?file-format=xlsx`
        The currently supported formats are `xlsx` and `docx`. This endpoint also
        support the query parameter `names` which can be set to `merged` to combine
        the name fields into one column, by default the name fields are discrete.
        """
        slug = get_object_or_404(Class, pk=pk).slug
        return downloader(request=request, slug=slug)


class StudentViewSet(
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
