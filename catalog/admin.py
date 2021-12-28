from django.contrib import admin
from .models import *
from .models import Cloth_items
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(Azbuka_items)
class AzbukaItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'availability', 'description', )
    list_display_links = ('title', 'id')
    list_filter = ['availability', 'parent_product_category']
    search_fields = ('title', 'id', 'parent_product_category')
    save_on_top = True


@admin.register(Cloth_items)
class ClothItems(admin.ModelAdmin):
    list_display = ('id', 'code_item', 'name_item', 'get_image',
                    'time_update', 'is_publish')
    list_display_links = ('name_item', 'id', 'code_item')
    list_filter = ['color_cloth', 'parent_category', 'categor_price']
    search_fields = ('name_item', 'code_item')
    save_on_top = True
    list_editable = ['is_publish']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo_item.url} width="50" height="50"')

        get_image.shot_description = "изображение"


# Register your models here.
# admin.site.register(Cloth_items)
admin.site.register(Cloth_group)
admin.site.register(Model_group)
# admin.site.register(Cloth_categor_price)
admin.site.register(Cloth_color)
admin.site.register(Vendor)
