class Product:
    def __init__(self, name, unit_price, gst_percentage, quantity):
        self.name = name
        self.unit_price = unit_price
        self.gst_percentage = gst_percentage
        self.quantity = quantity

    def calculate_total_price(self):
        total_price = (self.unit_price * (1 + self.gst_percentage / 100)) * self.quantity

        # Applying a 5% discount for products whose unit price is more or equal to Rs. 500
        if self.unit_price >= 500:
            total_price *= 0.95

        return total_price

leather_wallet = Product("Leather Wallet", 1100, 18, 1)
umbrella = Product("Umbrella", 900, 12, 4)
cigarette = Product("Cigarette", 200, 28, 3)
honey = Product("Honey", 100, 0, 2)

basket = [leather_wallet, umbrella, cigarette, honey]

# Identifying  the product for which the customer paid the maximum GST amount
max_gst_product = max(basket, key=lambda product: product.unit_price * product.gst_percentage / 100)
print("Product with maximum GST amount:", max_gst_product.name)

# Calculating the total amount to be paid to the shopkeeper
total_amount_to_pay = sum(product.calculate_total_price() for product in basket)

print("Total amount to be paid to the shopkeeper:", total_amount_to_pay)