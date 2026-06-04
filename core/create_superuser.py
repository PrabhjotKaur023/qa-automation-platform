import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

django.setup()

from django.contrib.auth.models import User

username = "admin"
password = "admin@2003K"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        password=password,
        email="admin@test.com",
    )

print("Admin user ready")