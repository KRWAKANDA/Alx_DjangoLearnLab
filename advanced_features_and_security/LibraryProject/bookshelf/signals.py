from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.apps import apps


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.name != "bookshelf":
        return

    permissions = Permission.objects.filter(
        codename__in=["can_view", "can_create", "can_edit", "can_delete"]
    )

    # Create Groups
    viewers, _ = Group.objects.get_or_create(name="Viewers")
    editors, _ = Group.objects.get_or_create(name="Editors")
    admins, _ = Group.objects.get_or_create(name="Admins")

    # Assign Permissions
    viewers.permissions.set(permissions.filter(codename="can_view"))
    editors.permissions.set(permissions.filter(codename__in=["can_view", "can_edit", "can_create"]))
    admins.permissions.set(permissions)
