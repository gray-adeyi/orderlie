from django.db import models
from django.utils.text import slugify

# Create your models here.


class Class(models.Model):
    LEVEL = (
        ('100', '100 Level'),
        ('200', '200 Level'),
        ('300', '300 Level'),
        ('400', '400 Level'),
        ('500', '500 Level'),
    )

    SESSION = (
        ('2018', '2018/19'),
        ('2019', '2019/20'),
        ('2020', '2020/21'),
        ('2021', '2021/22'),
        ('2019', '2022/23'),
    )
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50)
    faculty = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    governor = models.CharField(max_length=100)
    deputy_governor = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL)
    session = models.CharField(max_length=20, choices=SESSION)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'classes'


class Student(models.Model):
    student_class = models.ForeignKey(
        Class, on_delete=models.CASCADE, related_name='students')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    reg_no = models.CharField(max_length=50, unique=True)
    matric_no = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.matric_no)

    class Meta:
        ordering = ['matric_no', ]
