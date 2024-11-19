from django.contrib import admin
from Invoices.models import Invoice, InvoiceDetail
# Register your models here.

admin.site.register(Invoice)
admin.site.register(InvoiceDetail)