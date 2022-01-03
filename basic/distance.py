distance_in_fts = int(input('Enter the distance in fts:\n'))

distance_in_inches = distance_in_fts * 12
distance_in_yards = distance_in_fts * 0.33
distance_im_miles = distance_in_fts * 0.000189394

print(f'Distance in fts: {distance_in_fts}\n'
      f'Distance in inches: {distance_in_inches}\n'
      f'Distance in yards: {distance_in_yards:.2f}\n'
      f'Distance in miles: {distance_im_miles:.2f}')
