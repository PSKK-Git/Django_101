from django.contrib import admin
from .models import Post, Product, SubProduct, SubPost, Banner

class PostAdmin(admin.ModelAdmin):
    pass
class BannerAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass
class SubProductAdmin(admin.ModelAdmin):
    pass
class SubPostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post,PostAdmin)
admin.site.register(Banner)
admin.site.register(Product)
admin.site.register(SubProduct)
admin.site.register(SubPost)



