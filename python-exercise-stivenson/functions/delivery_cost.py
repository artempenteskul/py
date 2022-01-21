parcels_quantity = int(input('Enter parcels quantity: '))

FIRST_PARCEL_COST = 10.95
NEXT_PARCEL_COST = 2.95


def delivery_cost(quantity):
    if quantity < 1:
        return 0
    elif quantity == 1:
        return 10.95
    elif quantity > 1:
        return 10.95 + ((quantity - 1) * 2.95)


print(f'Delivery cost: {delivery_cost(parcels_quantity):.2f} $')
