# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

test_damages = ['100M']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(lst):
    new_lst = []
    for item in lst:
        if item == "Damages not recorded":
            new_lst.append(item)
        else:
            index = 0
            for char in item:
                if char == "M":
                    new_lst.append(float(item[0:index]) * 1000000)
                elif char == "B":
                    new_lst.append(float(item[0:index]) * 1000000000)
                else:
                    index += 1
    return new_lst

updated_damages = update_damages(damages)

test_name = ["Bob", "Tim", "Allan", "Betty"]
test_month = ["September", "October", "November", "July"]
test_year = [1991, 1991, 1993, 1993]
test_wind = [75, 150, 550, 1500]
test_area = [["New England", "Boston"], ["MidAtlantic", "Washington"], ["MidAtlantic", "Deleware"], ["Southeastern", "Florida"]]
test_damage = [1000000, 15000000, 734000, 876300]
test_death = [90, 150, 550, 1500]

# write your construct hurricane dictionary function here:
def construct_hurricane_dictionary(names, months, years, winds, areas, damages, deaths):
    values = []
    for row in zip(names, months, years, winds, areas, damages, deaths):
        values.append({"Name": row[0], "Month": row[1], "Year": row[2], "Max Sustained Wind": row[3], "Areas Affected": row[4], "Damages": row[5], "Deaths": row[6]})
    return {key:value for key, value in zip(names, values)}

hurricane_dictionary = construct_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
test_hurricane_dictionary = construct_hurricane_dictionary(test_name, test_month, test_year, test_wind, test_area, test_damage, test_death)

# write your construct hurricane by year dictionary function here:
def construct_hurricane_by_year_dictionary(input_dict):
    by_year = {}
    values = list(input_dict.values()) # dictionaries
    years = []
    for row in values:
        if row["Year"] not in years:
            years.append(row["Year"])
    print(years)
    for year in years: # compare each year to dictionaries, put all with same years in a separate list
        temp_list = []
        for row in values:
            if year == row["Year"]:
                temp_list.append(row)
        by_year.update({year: temp_list})
    return by_year

# write your count affected areas function here:
def count_affected_areas(input_dict):
    count_dict = {}
    values = list(input_dict.values())
    area_list = []
    for row in values:
        areas = row["Areas Affected"]
        for area in areas:
            area_list.append(area)
    for area in area_list:
        if area not in count_dict:
            count_dict.update({area: area_list.count(area)})
    return count_dict

count_dictionary = count_affected_areas(hurricane_dictionary)

# write your find most affected area function here:
def most_affected_area(input_dict):
    values = list(input_dict.values())
    keys = list(input_dict.keys())
    max_value = max(values)
    max_key = keys[values.index(max_value)]
    print("The area most affected by hurricanes is " + max_key + " with " + str(max_value) + " hurricanes.")

# write your greatest number of deaths function here:
def greatest_number_of_deaths(input_dict):
    max_value = 0
    i = 0
    hurricanes = list(input_dict.items())
    for hurricane in hurricanes:
        if hurricane[1]["Deaths"] >= max_value:
            max_value = hurricane[1]["Deaths"]
            i = hurricanes.index(hurricane)
    max_key = hurricanes[i][0]
    print("The hurricane that caused the most deaths was " + max_key + " with " + str(max_value) + " deaths.")

# write your catgeorize by mortality function here:
def categorize_by_mortality(input_dict):
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    death_dict = {}
    hurricanes = list(input_dict.values())
    categories = list(mortality_scale.items())
    for i in range(len(categories)):
        death_list = []
        for hurricane in hurricanes:
            if i < 4:
                if hurricane["Deaths"] > categories[i][1] and hurricane["Deaths"] <= categories[i + 1][1]:
                    death_list.append(hurricane)
            else:
                if hurricane["Deaths"] > categories[i][1]:
                    death_list.append(hurricane)
        death_dict.update({i: death_list})
    return death_dict

# write your greatest damage function here:
def greatest_damage(input_dict):
    max_value = 0
    i = 0
    hurricanes = list(input_dict.items())
    for hurricane in hurricanes:
        if hurricane[1]["Damages"] >= max_value:
            max_value = hurricane[1]["Damages"]
            i = hurricanes.index(hurricane)
    max_key = hurricanes[i][0]
    print("The hurricane that caused the most damages was " + max_key + " at $" + str(max_value))


# write your catgeorize by damage function here:
def categorize_by_damage(input_dict):
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
    damages_dict = {}
    hurricanes = list(input_dict.values())
    categories = list(damage_scale.items())
    for i in range(len(categories)):
        damages_list = []
        for hurricane in hurricanes:
            if hurricane["Damages"] == "Damages not recorded":
                continue
            if i < 4:
                if hurricane["Damages"] > categories[i][1] and hurricane["Damages"] <= categories[i + 1][1]:
                    damages_list.append(hurricane)
            else:
                if hurricane["Damages"] > categories[i][1]:
                    damages_list.append(hurricane)
        damages_dict.update({i: damages_list})
    return damages_dict
