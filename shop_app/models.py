from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва товару")
    description = models.TextField(verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    category = models.CharField(max_length=50,
                                choices=[('New Arrivals', 'Нові надходження'), ('Best Sellers', 'Хіти продажів')],
                                default='New Arrivals', verbose_name="Категорія")


    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 verbose_name="Додано адміністратором")

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Користувач")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")

    def __str__(self):
        return f"Кошик користувача: {self.user.username}"


# 3. Таблиця "Елемент Кошика" (Для зв'язку Кошик - Товар)
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Кошик")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.IntegerField(default=1, verbose_name="Кількість")

    def total_price(self):
        # Розрахунок загальної ціни за цю позицію
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name} у кошику {self.cart.user.username}"