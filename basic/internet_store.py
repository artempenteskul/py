souvenir_quantity = int(input('Enter the quantity of souvenirs: '))
bauble_quantity = int(input('Enter the quantity of baubles: '))

total_weight = souvenir_quantity * 75 + bauble_quantity * 112

print(f'Average weight of parcel is: {total_weight / 1000:.2f} kg')
