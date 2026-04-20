import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sky_registry.settings")
django.setup()

from django.contrib import admin
from django.contrib.admin.sites import site

print("=== ALL REGISTERED MODELS ===")
for model, admin_class in sorted(
    site._registry.items(),
    key=lambda x: x[0].__name__
):
    print(f"Model: {model.__name__}")
    print(f"  Class: {admin_class.__class__.__name__}")
    print(f"  list_display: {getattr(admin_class, 'list_display', [])}")
    print(f"  search_fields: {getattr(admin_class, 'search_fields', [])}")
    print(f"  list_filter: {getattr(admin_class, 'list_filter', [])}")
    print(f"  actions: {list(admin_class.actions or [])}")
    print(f"  inlines: {[i.__name__ for i in getattr(admin_class, 'inlines', [])]}")
    print(f"  readonly_fields: {getattr(admin_class, 'readonly_fields', [])}")
    print(f"  fieldsets: {'YES' if getattr(admin_class, 'fieldsets', None) else 'NO'}")
    print()
