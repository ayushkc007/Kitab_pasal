from django.contrib import admin

# Register your models here.
from .models import PaymentGateway,InvoiceDetails,Invoice

class PaymentGatewayAdmin(admin.ModelAdmin):
    list_display = ["token", "balance", "expiry_date", "is_active",]
    readonly_fields = ('id',) 
    class Meta:
        model = PaymentGateway 


class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ["invoice", "product", "quantity","sub_amount"] 

    class Meta:
        model = InvoiceDetails

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["user", "city", "address","payment_date","total_amount"] 
    readonly_fields = ('id',)
    class Meta:
        model = InvoiceDetails  

admin.site.register(PaymentGateway, PaymentGatewayAdmin)        
admin.site.register(InvoiceDetails, InvoiceDetailAdmin) 
admin.site.register(Invoice, InvoiceAdmin)    


