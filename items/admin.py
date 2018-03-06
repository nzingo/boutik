from django.contrib import admin
from .models import Item, ItemImage


class ImagesAdminInline(admin.TabularInline):
    model = ItemImage
    readonly_fields = ('image',)
    can_delete = False


class MyModelAdmin(admin.ModelAdmin):
    inlines = (ImagesAdminInline,)
    ordering = ('-created', )
    list_display = ('title', 'validated', 'created')  # , 'get_images')
    list_filter = ('validated', 'created')
    readonly_fields = ('title', 'body', 'price', 'category', 'sub_category', 'phone', 'location', 'likes')
    fieldsets = (
        (None, {
            'fields': ('validated', 'title', 'body')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (),
        }),
    )


admin.site.register(Item, MyModelAdmin)

