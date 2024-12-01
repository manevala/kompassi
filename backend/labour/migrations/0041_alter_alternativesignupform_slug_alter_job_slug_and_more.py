# Generated by Django 5.0.9 on 2024-11-30 15:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("labour", "0040_alter_alternativesignupform_signup_extra_form_class_path"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alternativesignupform",
            name="slug",
            field=models.CharField(
                help_text='Tekninen nimi eli "slug" näkyy URL-osoitteissa. Sallittuja merkkejä ovat pienet kirjaimet, numerot ja väliviiva. Teknistä nimeä ei voi muuttaa luomisen jälkeen.',
                max_length=255,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Tekninen nimi saa sisältää vain pieniä kirjaimia, numeroita sekä väliviivoja.",
                        regex="^[a-z0-9-]+$",
                    )
                ],
                verbose_name="Tekninen nimi",
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="slug",
            field=models.CharField(
                help_text='Tekninen nimi eli "slug" näkyy URL-osoitteissa. Sallittuja merkkejä ovat pienet kirjaimet, numerot ja väliviiva. Teknistä nimeä ei voi muuttaa luomisen jälkeen.',
                max_length=255,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Tekninen nimi saa sisältää vain pieniä kirjaimia, numeroita sekä väliviivoja.",
                        regex="^[a-z0-9-]+$",
                    )
                ],
                verbose_name="Tekninen nimi",
            ),
        ),
        migrations.AlterField(
            model_name="jobcategory",
            name="slug",
            field=models.CharField(
                help_text='Tekninen nimi eli "slug" näkyy URL-osoitteissa. Sallittuja merkkejä ovat pienet kirjaimet, numerot ja väliviiva. Teknistä nimeä ei voi muuttaa luomisen jälkeen.',
                max_length=255,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Tekninen nimi saa sisältää vain pieniä kirjaimia, numeroita sekä väliviivoja.",
                        regex="^[a-z0-9-]+$",
                    )
                ],
                verbose_name="Tekninen nimi",
            ),
        ),
        migrations.AlterField(
            model_name="personnelclass",
            name="slug",
            field=models.CharField(
                help_text='Tekninen nimi eli "slug" näkyy URL-osoitteissa. Sallittuja merkkejä ovat pienet kirjaimet, numerot ja väliviiva. Teknistä nimeä ei voi muuttaa luomisen jälkeen.',
                max_length=255,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Tekninen nimi saa sisältää vain pieniä kirjaimia, numeroita sekä väliviivoja.",
                        regex="^[a-z0-9-]+$",
                    )
                ],
                verbose_name="Tekninen nimi",
            ),
        ),
        migrations.AlterField(
            model_name="qualification",
            name="slug",
            field=models.CharField(
                help_text='Tekninen nimi eli "slug" näkyy URL-osoitteissa. Sallittuja merkkejä ovat pienet kirjaimet, numerot ja väliviiva. Teknistä nimeä ei voi muuttaa luomisen jälkeen.',
                max_length=255,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Tekninen nimi saa sisältää vain pieniä kirjaimia, numeroita sekä väliviivoja.",
                        regex="^[a-z0-9-]+$",
                    )
                ],
                verbose_name="Tekninen nimi",
            ),
        ),
        migrations.AlterField(
            model_name="survey",
            name="slug",
            field=models.CharField(
                help_text='Tekninen nimi eli "slug" näkyy URL-osoitteissa. Sallittuja merkkejä ovat pienet kirjaimet, numerot ja väliviiva. Teknistä nimeä ei voi muuttaa luomisen jälkeen.',
                max_length=255,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Tekninen nimi saa sisältää vain pieniä kirjaimia, numeroita sekä väliviivoja.",
                        regex="^[a-z0-9-]+$",
                    )
                ],
                verbose_name="Tekninen nimi",
            ),
        ),
    ]
