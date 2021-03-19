from django.contrib import admin
from .models import Banco, Agencia, Cliente, Conta

admin.site.register([Banco, Agencia, Cliente, Conta])
