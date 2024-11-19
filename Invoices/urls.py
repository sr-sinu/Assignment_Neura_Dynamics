from django.urls import path
from .views import InvoiceAPIView

# Define URL patterns for the API
urlpatterns = [
    path('invoices/', InvoiceAPIView.as_view(), name='invoice-api'),
]
