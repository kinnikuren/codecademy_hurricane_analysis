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

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(damages):
  updated_damages = []
  for i in range(len(damages)):
    updated_dmg = damages[i]
    #print(damages[i][-1])
    if (damages[i][-1] == 'M'):
      updated_dmg = float(damages[i][:-1]) * 1000000
    elif (damages[i][-1] == 'B'):
      updated_dmg = float(damages[i][:-1]) * 1000000000
    updated_damages.append(updated_dmg)
  return updated_damages

updated_damages = update_damages(damages)
#print(update_damages(damages))

# write your construct hurricane dictionary function here:
def construct_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricane_dict = {}
  for i in range(len(names)):
    hurricane_dict[names[i]] = {
      "Name": names[i],
      "Month": months[i],
      "Year": years[i],
      "Max Sustained Wind": max_sustained_winds[i],
      "Areas Affected": areas_affected[i],
      "Damage": damages[i],
      "Deaths": deaths[i]
      }

  return hurricane_dict
              
hurricane_dict = construct_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricane_dict)


# write your construct hurricane by year dictionary function here:
def construct_hurricane_dict_by_year(hurricane_dict):
  new_dict = {}
  for key, val in hurricane_dict.items():
    if val["Year"] not in new_dict:
      new_dict[val["Year"]] = [val]
    else:
      new_dict[val["Year"]].append(val)

  return new_dict

hurricane_dict_by_year = construct_hurricane_dict_by_year(hurricane_dict)
print(hurricane_dict_by_year)


# write your count affected areas function here:
def count_affected_areas(hurricane_dict):
  new_dict = {}
  for key, val in hurricane_dict.items():
    for area in val["Areas Affected"]:
      if area not in new_dict:
        new_dict[area] = 1
      else:
        new_dict[area] += 1

  return new_dict

affected_areas_dict = count_affected_areas(hurricane_dict)
print(affected_areas_dict)


# write your find most affected area function here:
def find_most_affected_area(affected_areas_dict):
  highest_val = 0
  most_affected_area = ''
  for key, val in affected_areas_dict.items():
    if val > highest_val:
      most_affected_area = key
      highest_val = val

  return (most_affected_area, highest_val)

print(find_most_affected_area(affected_areas_dict))
  

# write your greatest number of deaths function here:
def most_deaths(hurricane_dict):
  most_deaths = 0
  hurricane_most_deaths = ''
  for key, val in hurricane_dict.items():
    if val["Deaths"] > most_deaths:
      most_deaths = val["Deaths"]
      hurricane_most_deaths = key

  return (hurricane_most_deaths, most_deaths)

print(most_deaths(hurricane_dict))

# write your catgeorize by mortality function here:
def categorize_by_mortality(hurricane_dict):
  mortality_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

  for key, val in hurricane_dict.items():
    deaths = val["Deaths"]
    if deaths == 0:
      mortality_dict[0].append(val)
    elif deaths > 0 and deaths <= 100:
      mortality_dict[1].append(val)
    elif deaths > 100 and deaths <= 500:
      mortality_dict[2].append(val)
    elif deaths > 500 and deaths <= 1000:
      mortality_dict[3].append(val)
    elif deaths > 1000 and deaths <= 10000:
      mortality_dict[4].append(val)
    elif deaths > 10000:
      mortality_dict[5].append(val)


  return mortality_dict

print(categorize_by_mortality(hurricane_dict))


# write your greatest damage function here:
def most_damage(hurricane_dict):
  most_damage = 0
  hurricane_most_damage = ''
  for key, val in hurricane_dict.items():
    #print(val["Damage"])
    #sprint(type(val["Damage"]))
    if type(val["Damage"]) == int or type(val["Damage"]) == float:
      if val["Damage"] > most_damage:
        most_damage = val["Damage"]
        hurricane_most_damage = key

  return (hurricane_most_damage, most_damage)

print(most_damage(hurricane_dict))


# write your catgeorize by damage function here:
def categorize_by_damage(hurricane_dict):
  damage_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

  for key, val in hurricane_dict.items():
    damage = val["Damage"]
    if type(damage) == int or type(damage) == float:
      if damage == 0:
        damage_dict[0].append(val)
      elif damage > 0 and damage <= 100000000:
        damage_dict[1].append(val)
      elif damage > 100000000 and damage <= 1000000000:
        damage_dict[2].append(val)
      elif damage > 1000000000 and damage <= 10000000000:
        damage_dict[3].append(val)
      elif damage > 10000000000 and damage <= 50000000000:
        damage_dict[4].append(val)
      elif damage > 50000000000:
        damage_dict[5].append(val)


  return damage_dict

print(categorize_by_damage(hurricane_dict))
