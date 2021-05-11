from django.shortcuts import render, redirect
from .models import PaymentGateway, Invoice, InvoiceDetails
from product_module.models import CartItem, Product,Tax,Shipping_Cost
from datetime import date, datetime
from django.db import transaction
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.utils.html import mark_safe
from mail_templated import send_mail
# Create your views here.
def confirmpayment(request):
	if request.method == "POST":
		token = request.POST.get("token")
		amount = request.POST.get("amount")
		city = request.POST.get("city")
		address = request.POST.get("address")
		contact_no = request.POST.get("contact_no")
		# clean up
		token = token.strip()
		amount = float(amount)
		try:
			with transaction.atomic():
				# open an atomic transaction, i.e. all successful or none
				make_payment(token, amount)
				maintain_invoice(request, token, amount,city,address,contact_no)
		except Exception as e:
			request.session["message"] = str(e)
			return redirect(reverse('error_page'))
		else:
			request.session["message"] = f"Payment successfully completed with NRs. {amount} from your balance!"
			return redirect(reverse('success_page'))
def make_payment(token, amount):
	try:
		payment_gateway = PaymentGateway.objects.get(token=token)
	except:
		raise Exception(f"Invalid token '{token}'")
	# Check if available amount is sufficient for payment
	if payment_gateway.balance < amount:
		raise Exception("Insufficient balance")
	# check for expiry date
	if payment_gateway.expiry_date < date.today():
		raise Exception("Token has expired")
	# deduct amount and save
	payment_gateway.balance -= amount
	payment_gateway.save()

def maintain_invoice(request, token, amount, city,address,contact_no):
	# retrieve cart items
	cart_items = CartItem.objects.filter(user=request.user)
	# save invoice
	invoice = Invoice(
	user = request.user,
	token = token,
	total_amount = amount,
	city=city,
	address=address,
	contact_no = contact_no,
	payment_date = datetime.now()
	)
	invoice.save()
	# invoic_id = Invoice.objects.filter(user=request.user)
	fkid = invoice.id
	# save invoice detail
	for cart_item in cart_items:
		invoice_detail = InvoiceDetails(
		invoice = invoice,
		product = cart_item.product,
		quantity = cart_item.quantity,
		sub_amount = cart_item.quantity * cart_item.product.price
		)
		invoice_detail.save()

	# adjust product quantity and clear cart
	for cart_item in cart_items:
	# reduce quantity from Product
		product = Product.objects.get(id=cart_item.product.id)
		if product.quantity < cart_item.quantity:
			raise Exception(f"Insufficient quantity {cart_item.quantity} for {product.name}")
		product.quantity -= cart_item.quantity
		product.save()
	# clear cart for the user
		cart_item.delete()
	order_confirmation(request,fkid)
def order_confirmation(request,fkid):
    tax = Tax.objects.get(pk=1)
    invoice = Invoice.objects.get(pk=fkid)
    shipping = Shipping_Cost.objects.get(pk=1)
    invoice_details = InvoiceDetails.objects.filter(invoice_id=fkid)
    total =0
    for invoice_detail in invoice_details:
        total +=invoice_detail.sub_amount
    tax_amount =total*(tax.tax_rate_in_percentage/100)
    user = request.user
    send_mail('bill.tpl', {'user': user,'invoice_details':invoice_details,'tax':tax,'tax_amount':tax_amount,'shipping':shipping,'invoice':invoice}, settings.EMAIL_HOST_USER, [user.email])
    # product=[]
    # text_content = " "
    # for invoice_detail in invoice_details:
    #     text_content = f"Name:{invoice_detail.product}" 

    # current_user = request.user
    # email = current_user.email
    # html_content = mark_safe(f"{}")
    # # text_content = strip_tags(html_content)

    # email = EmailMultiAlternatives(
    #     "Testing",
    #     html_content,
    #     settings.EMAIL_HOST_USER,
    # [email]

    # )
    # email.attach_alternative(html_content,"text/html")
    # email.send()