data_of_players = []
while True:
    try:
        speed = int(input("Enter speed rating (0-5): "))
        shooting = int(input("Enter shooting rating (0-5): "))
        passing = int(input("Enter passing rating (0-5): "))
        defending = int(input("Enter defending rating (0-5): "))
        dribbling = int(input("Enter dribbling rating (0-5): "))
        physicality = int(input("Enter physicality rating (0-5): "))

        salary_range = speed, shooting, passing, defending, dribbling, physicality
        overall_rating = (speed + shooting + passing + defending + dribbling + physicality) * 100 / 30
        data_of_players.append((overall_rating, salary_range))

        another_player = input("Do you want to enter data for another player? (yes/no): ")
        if another_player.lower() != "yes" and another_player.upper() != "YES":
            break
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 5 for ratings.")
