from django.contrib import admin
# Register your models here.
from .models import Publication, Author, Category, Product, CartItem,Slider,Tax,Shipping_Cost

class PublicationAdmin(admin.ModelAdmin):
    list_display=["name","is_active"]
    search_fields=["name",]
    class Meta:
        model = Publication

class CategoryAdmin(admin.ModelAdmin):
    list_display=["name","is_active"]
    search_fields=["name",]
    class Meta:
        model = Category

class AuthorAdmin(admin.ModelAdmin):
    list_display=["name","description","is_active"]
    search_fields=["name",]
    class Meta:
        model = Author

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","image_tag","name", "price", "publication", "category","ISBN","registered_on",]
    search_fields = ["name", "price", "publication__name", "category__name",]
    list_filter = ["publication","category",]

    class Meta:
        model = Product 

class SliderAdmin(admin.ModelAdmin):
    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False
    list_display = ['id', 'best_seller_productID', 'our_pick_productID', 'new_arrival_productID',]

    class Meta:
        model = Slider

class TaxAdmin(admin.ModelAdmin):
    list_display = ["tax_rate_in_percentage",]
    #  This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False

class Shipping_CostAdmin(admin.ModelAdmin):
    list_display = ["shipping_cost"]
    #  This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False
        
admin.site.register(Publication,PublicationAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product, ProductAdmin)  
admin.site.register(CartItem)   
admin.site.register(Slider,SliderAdmin)
admin.site.register(Tax,TaxAdmin)
admin.site.register(Shipping_Cost,Shipping_CostAdmin)
