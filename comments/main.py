# Do not modify these lines
__winc_id__ = '63ce21059cf34d3d8ffef497ede7e317'
__human_name__ = 'comments'

# Add your code after this line
broccoli = 2 # de prijs van 1 broccoli
leek = 2
potato = 3
brussel_sprout = 7
# wat kost alles bij elkaar
sum_one_each = broccoli + leek + potato + brussel_sprout
avg_price = sum_one_each / 4 # de gemiddelde prijs van alle 4 de poducten
num_potatoes = 7
num_broccolis = 5
num_leeks = 2
num_brussel_sprouts = 10
# de totale kosten van alle boodschappen
sum_total = num_broccolis * broccoli  + num_leeks * leek  + num_potatoes * potato  + num_brussel_sprouts * brussel_sprout
discount_percentage = 30
""" tel hier alles bij elkaar
en haal dan de korting eraf"""
discounted_sum_total = sum_total - sum_total * discount_percentage / 100
""" print nu de totale kosten
min de korting """
print(discounted_sum_total)