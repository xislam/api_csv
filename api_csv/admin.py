from django.contrib import admin

# Register your models here.
from api_csv.models import Transaction, User, Gem

admin.site.register(Transaction)
admin.site.register(User)
admin.site.register(Gem)