from django.contrib import admin

# Register your models here.
from api_csv.models import Transaction

admin.site.register(Transaction)