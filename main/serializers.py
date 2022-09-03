from tabnanny import verbose
from .models import Class, Student
from rest_framework import serializers
from django.urls import reverse
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class APIURLMixin:
    def get_url(self, obj, view_name, request, format):
        """
        Given an object, return the URL that hyperlinks to the object.

        May raise a `NoReverseMatch` if the `view_name` and `lookup_field`
        attributes are not configured to correctly match the URL conf.
        """
        # Unsaved objects will not yet have a valid URL.
        if hasattr(obj, "pk") and obj.pk in (None, ""):
            return None

        lookup_value = getattr(obj, self.lookup_field)
        kwargs = {self.lookup_url_kwarg: lookup_value, "version": settings.API_VERSION}
        return self.reverse(view_name, kwargs=kwargs, request=request, format=format)


class APIHyperlinkedRelatedField(APIURLMixin, serializers.HyperlinkedRelatedField):
    """
    Overrides the HyperlinkedRelatedField to include the API version in url.
    """

    ...


class APIHyperlinkedIdentityField(APIURLMixin, serializers.HyperlinkedIdentityField):
    """
    Overrides the HyperlinkedIdentityField to include the API version in url.
    """

    ...


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    url = APIHyperlinkedIdentityField(view_name="student-detail")
    student_class = APIHyperlinkedRelatedField(
        view_name="class-detail", queryset=Class.objects
    )

    class Meta:
        model = Student
        fields = [
            "url",
            "id",
            "student_class",
            "first_name",
            "last_name",
            "middle_name",
            "reg_no",
            "matric_no",
        ]


class ClassSerializer(serializers.HyperlinkedModelSerializer):
    url = APIHyperlinkedIdentityField(view_name="class-detail")
    slug = serializers.URLField(read_only=True)
    students = StudentSerializer(many=True)

    class Meta:
        model = Class
        fields = [
            "url",
            "name",
            "slug",
            "faculty",
            "department",
            "governor",
            "deputy_governor",
            "level",
            "session",
            "students",
        ]


class DownloadQuerySerializer(serializers.Serializer):
    FORMAT = (
        ("json", "json"),
        ("api", "api"),
    )
    FILE_FORMAT = (
        ("xlsx", "xlsx"),
        ("docx", "docx"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.update(
            {"file-format": serializers.ChoiceField(choices=self.FILE_FORMAT)}
        )

    format = serializers.ChoiceField(choices=FORMAT, required=False)
