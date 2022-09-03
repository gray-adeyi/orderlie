from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.


class Class(models.Model):

    # Preferred to `models.TextChoices` because of leading number
    LEVELS = (
        ("100 Level", "100 Level"),
        ("200 Level", "200 Level"),
        ("300 Level", "300 Level"),
        ("400 Level", "400 Level"),
        ("500 Level", "500 Level"),
    )

    # Preferred to `models.TextChoices` because of leading number
    SESSIONS = (
        ("2018/19", "2018/19"),
        ("2019/20", "2019/20"),
        ("2020/21", "2020/21"),
        ("2021/22", "2021/22"),
        ("2022/23", "2022/23"),
        ("2023/24", "2023/24"),
        ("2024/25", "2024/25"),
    )

    name = models.CharField(
        max_length=128, help_text="the name of the class you're trying to create"
    )
    slug = models.UUIDField(
        default=uuid4,
        help_text="external id used to identify each class",
        unique=True,
        blank=True,
    )
    faculty = models.CharField(
        max_length=200, help_text="the faculty the class belongs to"
    )
    department = models.CharField(
        max_length=200, help_text="the faculty the class belongs to"
    )
    governor = models.CharField(
        max_length=100, help_text="name of the class representative"
    )
    deputy_governor = models.CharField(
        max_length=100, help_text="name of the assistant class representative"
    )
    level = models.CharField(
        max_length=20, choices=LEVELS, help_text="the level the class is currently in"
    )
    session = models.CharField(
        max_length=20,
        choices=SESSIONS,
        help_text="the academic session the class belongs to",
    )

    class Meta:
        verbose_name_plural = "classes"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "class-detail",
            kwargs={"pk": self.pk, "version": settings.API_VERSION},
        )


class Student(models.Model):
    student_class = models.ForeignKey(
        Class, on_delete=models.CASCADE, related_name="students"
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    reg_no = models.CharField(
        verbose_name="registration number", max_length=50, unique=True
    )
    matric_no = models.IntegerField(verbose_name="matriculation number", unique=True)

    def __str__(self):
        return str(self.matric_no)

    class Meta:
        ordering = [
            "matric_no",
        ]
