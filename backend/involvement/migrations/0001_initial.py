# Generated by Django 5.1.5 on 2025-05-11 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core", "0043_emailverificationtoken_language_and_more"),
        ("dimensions", "0010_alter_universe_app"),
        ("forms", "0039_survey_cached_default_dimensions_and_more"),
        ("program_v2", "0038_alter_programv2eventmeta_contact_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Registry",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slug", models.SlugField()),
                ("title_en", models.CharField(max_length=255)),
                ("title_fi", models.CharField(max_length=255)),
                ("title_sv", models.CharField(max_length=255)),
                ("policy_url_en", models.URLField(blank=True)),
                ("policy_url_fi", models.URLField(blank=True)),
                ("policy_url_sv", models.URLField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "scope",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="registries", to="dimensions.scope"
                    ),
                ),
            ],
            options={
                "ordering": ("scope", "slug"),
                "unique_together": {("scope", "slug")},
            },
        ),
        migrations.CreateModel(
            name="Involvement",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "app_name",
                    models.CharField(choices=[("forms", "Surveys V2"), ("program", "Program V2")], max_length=7),
                ),
                ("cached_dimensions", models.JSONField(blank=True, default=dict)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="involvements", to="core.person"
                    ),
                ),
                (
                    "program",
                    models.ForeignKey(
                        blank=True,
                        db_index=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="involvements",
                        to="program_v2.program",
                    ),
                ),
                (
                    "response",
                    models.ForeignKey(
                        blank=True,
                        db_index=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="involvements",
                        to="forms.response",
                    ),
                ),
                (
                    "universe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="involvements",
                        to="dimensions.universe",
                    ),
                ),
                (
                    "registry",
                    models.ForeignKey(
                        db_index=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="involvements",
                        to="involvement.registry",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InvolvementDimensionValue",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dimensions",
                        to="involvement.involvement",
                    ),
                ),
                (
                    "value",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="+", to="dimensions.dimensionvalue"
                    ),
                ),
            ],
            options={
                "unique_together": {("subject", "value")},
            },
        ),
        migrations.AddIndex(
            model_name="involvement",
            index=models.Index(fields=["universe", "person", "app_name"], name="involvement_univers_eeb99e_idx"),
        ),
        migrations.AddIndex(
            model_name="involvement",
            index=models.Index(fields=["registry", "person"], name="involvement_registr_c18158_idx"),
        ),
        migrations.AddIndex(
            model_name="involvement",
            index=models.Index(
                condition=models.Q(("program__isnull", False)),
                fields=["program", "person"],
                name="involvement_program_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="involvement",
            index=models.Index(
                condition=models.Q(("response__isnull", False)),
                fields=["response", "person"],
                name="involvement_response_idx",
            ),
        ),
    ]
