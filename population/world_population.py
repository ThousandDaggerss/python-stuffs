
import json


#  Load the data into a list.
filename = 'population\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

#  Print the infos for each country year same as '1961'.
for pop_dict in pop_data:
    if pop_dict['Year'] == '1961':
        country_name = pop_dict['Country Name']
        population = int(float((pop_dict['Value'])))
        print(country_name + ": " + str(population))

