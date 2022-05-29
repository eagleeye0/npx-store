from django.contrib import admin

# from control.models import Category, Order, ParentCategory, Product, Photo, Seller
from control.models import Customer

# # Register your models here.


# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'url_slug': ('category_name',)}
#     list_display = ['category_name', 'url_slug', 'parent_category']


# class ParentCategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']


# class ProductsAdmin(admin.ModelAdmin):
#     list_display = ['product_name', 'url_slug']


# class PhotoAdmin(admin.ModelAdmin):
#     list_display = ['product']



admin.site.register(Customer)
# admin.site.register(ParentCategory, ParentCategoryAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product, ProductsAdmin)
# admin.site.register(Photo, PhotoAdmin)
# admin.site.register(Seller)
# admin.site.register(Order)
