from django.db import models

#Models to store invoice details
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=255, unique=True)
    customer_name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.invoice_number


# Model to store individual line items for an invoice
class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='details', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.description} - {self.invoice.invoice_number}"
