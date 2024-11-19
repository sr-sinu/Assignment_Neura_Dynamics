from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Invoice
from .serializers import InvoiceSerializer

# API view to handle creation and updating of invoices
class InvoiceAPIView(APIView):
    """
    Handle POST request to create a new invoice along with its details.
    """
    def post(self, request, *args, **kwargs):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, *args, **kwargs):
        """
        Handle PUT request to update an existing invoice and its details.
        """
        try:
            invoice = Invoice.objects.get(invoice_number=request.data['invoice_number'])
        except Invoice.DoesNotExist:
            return Response({"detail": "Invoice not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = InvoiceSerializer(instance=invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
