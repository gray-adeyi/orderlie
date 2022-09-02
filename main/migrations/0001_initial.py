# Generated by Django 3.2.4 on 2021-06-05 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Class",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("slug", models.SlugField()),
                ("faculty", models.CharField(max_length=200)),
                ("department", models.CharField(max_length=200)),
                ("governor", models.CharField(max_length=100)),
                ("deputy_governor", models.CharField(max_length=100)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("100", "100 Level"),
                            ("200", "200 Level"),
                            ("300", "300 Level"),
                            ("400", "400 Level"),
                            ("500", "500 Level"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "session",
                    models.CharField(
                        choices=[
                            ("2018", "2018/19"),
                            ("2019", "2019/20"),
                            ("2020", "2020/21"),
                            ("2021", "2021/22"),
                            ("2019", "2022/23"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "classes",
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("middle_name", models.CharField(max_length=50)),
                ("reg_no", models.CharField(max_length=50, unique=True)),
                ("matric_no", models.IntegerField(unique=True)),
                (
                    "student_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="students",
                        to="main.class",
                    ),
                ),
            ],
            options={
                "ordering": ["matric_no"],
            },
        ),
    ]
