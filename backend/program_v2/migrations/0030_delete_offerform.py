# Generated by Django 5.0.9 on 2024-12-01 17:54

from django.db import migrations


def delete_offer_forms(apps, schema_editor):
    OfferForm = apps.get_model("program_v2", "OfferForm")
    Survey = apps.get_model("forms", "Survey")

    for offer_form in OfferForm.objects.all():
        for form in offer_form.languages.all():
            try:
                Survey.objects.get(languages=form)
            except Survey.DoesNotExist:
                pass
            except Survey.MultipleObjectsReturned:
                raise
            else:
                raise AssertionError(f"form used by both OfferForm and Survey: {form}")

            form.delete()


class Migration(migrations.Migration):
    dependencies = [
        ("program_v2", "0029_alter_programdimensionvalue_options_and_more"),
        ("forms", "0032_rename_new_value_responsedimensionvalue_value_and_more"),
    ]

    operations = [
        migrations.RunPython(
            delete_offer_forms,
            reverse_code=migrations.RunPython.noop,
            elidable=True,
        ),
        migrations.DeleteModel(
            name="OfferForm",
        ),
    ]
