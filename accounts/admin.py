from django.contrib import admin
from .models import CustomUser
from items.models import Item


class ItemsAdminInline(admin.TabularInline):
    model = Item
    fields = ('id', 'title', 'validated',)
    readonly_fields = ('id', 'title', 'validated',)
    can_delete = False


class My2ModelAdmin(admin.ModelAdmin):
    inlines = (ItemsAdminInline,)


admin.site.register(CustomUser, My2ModelAdmin)

