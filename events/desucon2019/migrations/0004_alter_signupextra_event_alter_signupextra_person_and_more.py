# Generated by Django 4.2.7 on 2023-11-26 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0039_alter_person_birth_date_alter_person_email_and_more"),
        ("desucon2019", "0003_auto_20190909_2157"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signupextra",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="%(app_label)s_signup_extras", to="core.event"
            ),
        ),
        migrations.AlterField(
            model_name="signupextra",
            name="person",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, related_name="%(app_label)s_signup_extra", to="core.person"
            ),
        ),
        migrations.AlterField(
            model_name="signupextra",
            name="special_diet",
            field=models.ManyToManyField(
                blank=True,
                related_name="_desucon2019_signupextra_special_diet+",
                to="desucon2019.specialdiet",
                verbose_name="Erikoisruokavalio",
            ),
        ),
    ]
