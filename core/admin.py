from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Core: Importing Models
from .models import UserProfile, Connection, Post, Game


class UserProfileResource(resources.ModelResource):
    class Meta:
        model = UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(ImportExportModelAdmin):
    list_display = (
        "user",
        "is_public",
        "is_verified",
    )
    pass


class ConnectionResource(resources.ModelResource):
    class Meta:
        model = Connection


@admin.register(Connection)
class ConnectionAdmin(ImportExportModelAdmin):
    pass


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    list_display = (
        "id",
        "user",
        "text",
        "date_created",
        "date_updated",
    )
    pass


class GameResource(resources.ModelResource):
    class Meta:
        model = Game


@admin.register(Game)
class GameAdmin(ImportExportModelAdmin):
    list_display = (
        "id",
        "title",
        "slug",
        "date_created",
        "date_updated",
    )
    pass
