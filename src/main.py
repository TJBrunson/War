def get_num_of_players():
    counter = 0
    while counter < 3:
        text = input()
        try:
            string_int = int(text)
            return string_int
        except ValueError:
            counter+=1
            print("Try entering a number less than 5")
    return None

print("Welcome to the card game War!")
print("How many players are there? (max 4)")
num = get_num_of_players()


