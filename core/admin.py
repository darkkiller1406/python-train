from django.contrib import admin

# Register your models here.
from core.models import Customers, Orders, Employees, OrderItems, Products, ProductCategories


class ProductsAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    search_fields_hint = "Hint: Search by Name"
    list_display = ('product_name', 'standard_cost', 'list_price', 'quantity')
    fieldsets = (
        ('PRODUCT DETAILS', {
            'fields': ('product_name',
                       'barcode',
                       'standard_cost',
                       'list_price',
                       'quantity',
                       'category',
                       'description', 'image_url')
        }),
    )
    readonly_fields = ('barcode',)

    def get_fieldsets(self, request, obj=None):
        if obj:
            return (
                ('PRODUCT DETAILS', {
                    'fields': ('product_name',
                               'barcode',
                               'standard_cost',
                               'list_price',
                               'quantity',
                               'category',
                               'description', 'image_url')
                }),
            )
        return (
                ('PRODUCT DETAILS', {
                    'fields': ('product_name',
                               'standard_cost',
                               'list_price',
                               'quantity',
                               'category',
                               'description', 'image_url')
                }),
            )


admin.site.register(Customers)
admin.site.register(Orders)
admin.site.register(Employees)
admin.site.register(OrderItems)
admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductCategories)