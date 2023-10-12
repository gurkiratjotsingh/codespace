data_of_players = []

while True:
        speed = int(input("Enter speed rating (0-5): "))
        shooting = int(input("Enter shooting rating (0-5): "))
        passing = int(input("Enter passing rating (0-5): "))
        defending = int(input("Enter defending rating (0-5): "))
        dribbling = int(input("Enter dribbling rating (0-5): "))
        physicality = int(input("Enter physicality rating (0-5): "))

        overall_rating = (speed + shooting + passing + defending + dribbling + physicality) * 100 / 30
        salary_range = 0

        if overall_rating>=80:
            salary_range = "1000"
        elif 80>overall_rating>=60:
            salary_range = "700 1000"
        elif overall_rating==60:
            salary_range = "700"
        elif 60>overall_rating>=45:
            salary_range = "400-500"
        elif overall_rating==45:
             salary_range = "500"
        elif 45>overall_rating>=30:
             salary_range="400-500"
        else:
             salary_range = "400"
        data_of_players.append((overall_rating, salary_range))

        for i in range(len(data_of_players)):
            print(i+1, data_of_players[i])

        more_players = input("Do you want to calculate for another player? (y/n)")
        if more_players.upper() != "Y" or more_players.lower() != "y":
             break


