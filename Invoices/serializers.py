from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['id', 'description', 'quantity', 'price', 'line_total']

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['id', 'invoice_number', 'customer_name', 'date', 'details']

    def validate(self, data):
        total_line_total = sum(item['line_total'] for item in data['details'])
        calculated_total = sum(item['quantity'] * item['price'] for item in data['details'])
        if total_line_total != calculated_total:
            raise serializers.ValidationError("Line totals do not match calculated totals.")
        return data

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        invoice = Invoice.objects.create(**validated_data)
        for detail in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail)
        return invoice

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details')
        instance.invoice_number = validated_data.get('invoice_number', instance.invoice_number)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.date = validated_data.get('date', instance.date)
        instance.save()

        # Replace old details with new ones
        instance.details.all().delete()
        for detail in details_data:
            InvoiceDetail.objects.create(invoice=instance, **detail)
        return instance
