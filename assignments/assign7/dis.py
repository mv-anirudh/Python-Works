# Open the file in read mode
with open("C:\\Users\\Ashok\\OneDrive\\Desktop\\PythonJuneWorks\\assignments\\assign7\\dis.txt", "r") as f:
   
    death_counts = {}
    flood_count={}
    year_count={}
    
    for line in f:
        word_list = line.rstrip("\n").split(" ")
        state = word_list[0]
        year = word_list[1]
        deaths = int(word_list[2])
        if state in death_counts:
            death_counts[state] +=deaths
        else:
            death_counts[state] =deaths
        if state in flood_count:
            flood_count[state] += 1
        else:
            flood_count[state] = 1
        
        if year in year_count:
            year_count[year] += 1
        else:
            year_count[year] = 1
max_deaths_state = max(death_counts, key=death_counts.get)
max_deaths_count = death_counts[max_deaths_state]

max_flood_year = max(year_count, key=year_count.get)
max_flood_year_count = year_count[max_flood_year]

max_flood_state = max(flood_count, key=flood_count.get)
max_flood_state_count = flood_count[max_flood_state]


min_deaths_state = min(death_counts, key=death_counts.get)
min_deaths_count = death_counts[min_deaths_state]


min_flood_state = min(flood_count, key=flood_count.get)
min_flood_state_count = flood_count[min_flood_state]
print(f"The state with the most deaths is {max_deaths_state} with {max_deaths_count} deaths.")
print(f"The year with the most floods is {max_flood_year} with {max_flood_year_count} flood occurrences.")
print(f"The state with the most floods is {max_flood_state} with {max_flood_state_count} flood occurrences.")
print(f"The state with the least deaths is {min_deaths_state} with {min_deaths_count} deaths.")
print(f"The state with the least floods is {min_flood_state} with {min_flood_state_count} flood occurrences.")
