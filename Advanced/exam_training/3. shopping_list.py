def shopping_list(budget, **kwargs):
    products_purchased = 0
    if budget < 100:
        return 'You do not have enough budget.'

    for product_name, v in kwargs.items():

        if products_purchased >= 5:
            break

        price = v[0]
        qty = v[1]

        total_price = price * qty

        if budget >= total_price:

            products_purchased += 1
            budget -= total_price
            print(f'You bought {product_name} for {total_price:.2f} leva.')

    return ''


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))



