from django.contrib import admin
# Register your models here.
from .models import Publication, Author, Category, Product, CartItem

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
    list_display = ["image_tag","name", "price", "publication", "category","ISBN",]
    search_fields = ["name", "price", "publication__name", "category__name",]
    list_filter = ["publication","category",]
    #readonly_fields = ["quantity",]
    #search_fields = ["name","price","quantity",]
    # list_display = ["name","price","quantity",]
    # list_filter = ["first_name","email",]
    # search_fields = ["first_name","last_name","email",]
    # readonly_fields = ["last_name",]
    # exclude = ["email"] # to exclude
    # fields = ["first_name","last_name",] # to include
    # fields vs exclude -- mutually exclusive

    class Meta:
        model = Product 
        
admin.site.register(Publication,PublicationAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product, ProductAdmin)  
admin.site.register(CartItem)   
