from django.contrib import admin

# Register your models here.
from .models import PaymentGateway,InvoiceDetails,Invoice

class PaymentGatewayAdmin(admin.ModelAdmin):
    list_display = ["token", "balance", "expiry_date", "is_active",]
    readonly_fields = ('id',) 
    class Meta:
        model = PaymentGateway 


class InvoiceDetailAdmin(admin.ModelAdmin):
    fields = ('shipping_status', )
    list_display = ["id","invoice_id", "product", "quantity","sub_amount","shipping_status"] 
    search_fields = ["invoice__id"]
     #  This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False

    class Meta:
        model = InvoiceDetails

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["id","user", "city", "address","contact_no","payment_date","total_amount"] 
    search_fields = ["id"]
    readonly_fields = ('id',)
     #  This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False
    class Meta:
        model = InvoiceDetails  

admin.site.register(PaymentGateway, PaymentGatewayAdmin)        
admin.site.register(InvoiceDetails, InvoiceDetailAdmin) 
admin.site.register(Invoice, InvoiceAdmin)    


