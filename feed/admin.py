from django.contrib import admin
from .models import Post, Product, SubProduct, SubPost, Banner, Baner , About

class PostAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass
class SubProductAdmin(admin.ModelAdmin):
    pass
class SubPostAdmin(admin.ModelAdmin):
    pass
class AboutAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from .models import Product, SubProduct, SubPost, Post, Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(Post,PostAdmin)
admin.site.register(Product)
admin.site.register(SubProduct)
admin.site.register(SubPost)
admin.site.register(Baner)
admin.site.register(About)



