from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Product ,Publication, Category, CartItem
from datetime import datetime
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CustomerRegistrationForm 
from django.views import View
from django.contrib import messages
import smtplib
# Create your views here.
def index(request):
    if request.method == "GET":
        category_id = request.GET.get("category__name") 
        publication_id = request.GET.get("publication")
        if category_id:
            filter_query = Q(category__id=category_id)
            products = Product.objects.filter(filter_query) 
        elif publication_id:
            filter_query = Q(publication__id=publication_id)
            products = Product.objects.filter(filter_query) 
        else:
            products = Product.objects.all()
            categories = Category.objects.all() 
            publications = Publication.objects.all()

            paginator=Paginator(products,per_page=8)
            page=request.GET.get('page',1 )
            try:
                books=paginator.page(page)
            except PageNotAnInteger:
                books=paginator.page(1)
            except EmptyPage:
                books=paginator.page(paginator.num_pages)
            context = {
                'products': books, 
                'categories': categories, 
                'publications': publications, 
                'search_query': '',
                }
            return render(request, 'index.html', context)
    else:
        q = request.POST.get("query")
        if "-" in q:
            price_values = q.split("-")
            filter_query = Q(price__gte=price_values[0]) & Q(price__lte=price_values[1]) 
        else:
            filter_query = Q(name__icontains=q) | Q(price__icontains=q) | Q(publication__name__icontains=q)
            products = Product.objects.filter(filter_query)
            categories = Category.objects.all()
            publications = Publication.objects.all() 
            paginator=Paginator(products,per_page=8)
            page=request.GET.get('page',1 )
            try:
                books=paginator.page(page)
            except PageNotAnInteger:
                books=paginator.page(1)
            except EmptyPage:
                books=paginator.page(paginator.num_pages)
            context = {
            'products': books, 
            'categories': categories, 
            'publications': publications, 
            'search_query': q,
            }
            return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def aboutus(request):
    return render(request, 'aboutus.html')    

def sendemail(request):
    name = request.POST.get("name") 
    email = request.POST.get("email")
    mess = request.POST.get("message")
    subject=request.POST.get("subject")
    for x in range(1,2):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('youremail','app_password')
        subject="Inquiry"+" "+subject
        body=f"Name: {name}\n Email:{email}\n Message:{mess}"
        msg=f"Subject:{subject} \n\n {body}"
        server.sendmail(
            'ayushkc9@gmail.com',
            'ayushkc101@gmail.com',
            msg
        )
        print("email has been sent {0} times".format(x))
        server.quit()
    request.session["message"]=f"Sucessfully sent message"
    return redirect(reverse('success_contact'))        


@login_required(login_url="/login")

def cart(request):
# get request data
    product_id = request.POST.get("id") 
    quantity = request.POST.get("qty")
    if product_id:
        # retrieve product data
        product = Product.objects.get(id=product_id)
        
        if quantity:
            if int(quantity)<=0:
                request.session["message"]=f"Invalid quantity:{quantity}"
                return redirect(reverse('error'))
        if quantity:
            if int(quantity)> int(product.quantity):
                request.session["message"]=f"Invalid quantity:{quantity}"
                return redirect(reverse('error'))
        try:
            # get cart item and increase quantity
            cart_item = CartItem.objects.get(user=request.user,product=product)
            cart_item.quantity += int(quantity)
            cart_item.entered_on = datetime.now() 
        except CartItem.DoesNotExist:
# initialize cart item 
            cart_item = CartItem(
                user=request.user, 
                product=product,
                quantity=int(quantity),
                entered_on = datetime.now(),
            )
# save to database 
        cart_item.save()
# retrieve the cart items for the user from db 
    cart_items = CartItem.objects.filter(user=request.user)
# calculate total
    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity
# return view 
    tax=total*0.13
    shippingcost=60
    grandtotal=total+tax+shippingcost
    context = {
        'cart_items': cart_items,
        'total': total, 
        'shippingcost':shippingcost,
        'tax':tax,
        'grandtotal':grandtotal,
        }
    
    return render(request, "cart.html", context)
    

def removecart(request, id): 
    try:
# get cart item and remove it
        product = Product.objects.get(id=id)
        cart_item = CartItem.objects.get(user=request.user, product=product) 
        cart_item.delete()
    except CartItem.DoesNotExist: 
        pass
    # redirect to cart
    return redirect(cart)    

def details(request,id):
    product= Product.objects.get(id=id)
    context = {
    'product': product,  
    }
    return render(request, "details.html", context)

def success_contact(request):
    message = request.session["message"]
    return render(request, "success_contact.html", {"message": message})

def error_contact(request):
    message = request.session["message"]
    return render(request, "error_contact.html", {"message": message})

def success_page(request):
    message = request.session["message"]
    return render(request, "success_page.html", {"message": message})

def error_page(request):
    message = request.session["message"]
    return render(request, "error_page.html", {"message": message})  

def error(request):
    message = request.session["message"]
    return render(request, "error.html", {"message": message})  

    

# def registration_view(request):
#     return render(request,"registration.html")  

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'registration.html',{'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'registration.html',{'form':form})

def changePassword(request):
    return render(request,'changepassword.html')

def filter_books(request,data=None):
    if data == None:
        books = Product.objects.all()
    elif data == 'Arts':
        books = Product.objects.filter(category__name = 'Arts')
    elif data == 'Biography':
        books = Product.objects.filter(category__name = 'Biography')
    elif data == 'Archaeology':
        books = Product.objects.filter(category__name = 'Archaeology')
    elif data == 'Astrology':
        books = Product.objects.filter(category__name = 'Astrology')
    elif data == 'History':
        books = Product.objects.filter(category__name = 'History')
    elif data == 'All':
        products = Product.objects.all()
        paginator=Paginator(products,per_page=8)
        page=request.GET.get('page',1 )
        try:
            books=paginator.page(page)
        except PageNotAnInteger:
            books=paginator.page(1)
        except EmptyPage:
            books=paginator.page(paginator.num_pages)
    else:
        books = Product.objects.all()
    return render(request,'filter_book.html',{'books':books})



