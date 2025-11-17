from django.contrib import admin
from .models import Product, Cart, CartItem

# Реєстрація моделі Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'added_by')
    list_filter = ('category',)
    search_fields = ('name',)

# Реєстрація моделі Cart
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')

# Реєстрація моделі CartItem
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'total_price')