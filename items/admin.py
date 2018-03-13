from django.contrib import admin
from .models import Item, ItemImage


class ImagesAdminInline(admin.TabularInline):
    model = ItemImage
    fields = ('image_tag',)
    readonly_fields = ('image_tag',)
    # readonly_fields = ('image',)
    can_delete = False


class MyModelAdmin(admin.ModelAdmin):
    inlines = (ImagesAdminInline,)
    ordering = ('-created', )
    list_display = ('title', 'validated', 'created')  # , 'get_images')
    list_filter = ('validated', 'created')
    readonly_fields = ('title', 'body', 'price', 'category', 'phone', 'location', 'likes', 'color', 'size')

    fieldsets = (

        (None, {
            'fields': ('validated',),
        }),

        ('Standard info', {
            'fields': ('title', 'body'),
            'classes': ('collapse',),
        }),

        ('other info', {
            'fields': ('category', ('color', 'size', 'phone')),
            'classes': ('collapse',),
        }),
    )

    # fieldsets = (
    #     (None, {
    #         'fields': ('validated', 'title', 'body')
    #     }),
    #     ('Advanced options', {
    #         'classes': ('collapse',),
    #         'fields': (),
    #     }),
    # )


admin.site.register(Item, MyModelAdmin)

