# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player_1 = "Ruud Gullit"
player_2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = player_1 +" "+ str(goal_0) + ',' + " " + player_2 +" "+ str(goal_1)
report = f"{player_1} scored in the {goal_0}nd minute\n{player_2} scored in the {goal_1}th minute"
player = "Ruud Gullit"
find_insertion_pos = player.find(" ")
first_name = player[:player.find(" ")]
last_name = player[find_insertion_pos + 1:]
last_name_len = (len(last_name))
name_short = player[0]+"."+" "+ last_name
chant = (first_name + "! ") * len(first_name)
chant = chant[:-1] # deze heb ik "gejat" ik kwam er maar niet uit, ik snap het nu wel
good_chant = chant[-1] != first_name + "! " # deze heb ik half gejat (de chant[-1] gedeelte) first_name = "! " gedeelte is van mezelf