# Generated by Django 4.2.3 on 2024-03-10 23:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("admin", "0005_auto_20230614_1322"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("authentication", "0003_rename_user_account"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Account",
            new_name="User",
        ),
    ]
