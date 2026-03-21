from django.contrib import admin
from .models import Waste, Status, QR, QRScanLog

@admin.register(Waste)
class WasteAdmin(admin.ModelAdmin):
    list_display = ['waste_type', 'quantity', 'medical_organization', 'pickup_point', 'delivery_point', 'current_status']
    list_filter  = ['waste_type', 'current_status']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['waste', 'state', 'time', 'changed_by']

@admin.register(QR)
class QRAdmin(admin.ModelAdmin):
    list_display = ['code', 'waste', 'expires_at', 'is_active', 'created_by']

@admin.register(QRScanLog)
class QRScanLogAdmin(admin.ModelAdmin):
    list_display = ['raw_code', 'scanned_by', 'scanned_at', 'success', 'fail_reason']
    list_filter  = ['success']