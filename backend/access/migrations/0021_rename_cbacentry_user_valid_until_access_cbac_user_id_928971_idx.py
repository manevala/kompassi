# Generated by Django 5.0.1 on 2024-01-17 13:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("access", "0020_alter_cbacentry_index_together_remove_cbacentry_mode"),
    ]

    operations = [
        migrations.RenameIndex(
            model_name="cbacentry",
            new_name="access_cbac_user_id_928971_idx",
            old_fields=("user", "valid_until"),
        ),
    ]
