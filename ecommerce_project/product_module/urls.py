from django.urls import path
from .forms import LoginForm,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm
from product_module import views
from django.contrib.auth import views as auth_views
from .views import (index,contact,cart,removecart,details,sendemail,
success_contact,error_contact,success_page,error_page,error,aboutus,changePassword,filter_books)

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('aboutus/', aboutus),
    # path('login/', login_view),
    # path('registration/', registration_view),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',
    authentication_form=LoginForm),name='customerlogin'),
    path('logout/',auth_views.LogoutView.as_view(next_page ='/login/'), name='logout'),
    path('contact/sendemail', sendemail),
    path('details/<int:id>',details),
    path('details/cart', cart),
    path('cart/',cart),
    path('cart/remove/<int:id>', removecart),
    path('success_contact/', success_contact, name="success_contact"),
    path('error_contact/', error_contact, name="error_contact"),
    path('success_page/', success_page, name="success_page"), 
    path('error_page/', error_page, name="error_page"),
    path('error/', error, name="error"),
    path('changepassword/',auth_views.PasswordChangeView.as_view(template_name='changepassword.html',
    form_class=MyPasswordChangeForm, success_url="/passwordchangedone/"),
    name="changepassword"),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name="passwordchangedone.html")),
    path('password-rest',auth_views.PasswordResetView.as_view(template_name="password_reset.html",
    form_class=MyPasswordResetForm),name="password_reset"),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
    name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html",
    form_class=MySetPasswordForm),name="password_reset_confirm"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
    name="password_reset_complete"),
    path('filter-book/<slug:data>',filter_books,name="filter_book"),
]