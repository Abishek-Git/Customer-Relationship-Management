from typing import Sized
from django import forms
from django.db.models import fields
from django.forms import widgets
from django_filters.filters import DateFilter
from .models import Order
from django.forms import ModelForm
import django_filters
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class FilterForm(django_filters.FilterSet):
    start_date = DateFilter(field_name= "date_created", lookup_expr= 'gte', label= "From", )
    end_date = DateFilter(field_name= "date_created", lookup_expr= 'lte', label= "To")
    class Meta:
        model = Order
        fields = ['Customer', 'Product', 'status',]


class Register_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class user_update(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
        