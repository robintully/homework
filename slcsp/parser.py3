zip_array = []
states_and_areas = []
final_array = []

# add all the zips to the zip array
f = open('slcsp.csv', 'r')
try:
  for line in f.readlines()[1:]:
    zip_array.append(int(line[:-2]))
finally:
   f.close()

# Get the state and region code
h = open('zips.csv', 'r')
try:
  for line in h.readlines()[1:]:
    line = line[:-1].split(',')
    line [0] = int(line[0])
    line [4] = int(line[4])
    states_and_areas.append(line)
finally:
   h.close()

# formate the plans
h = open('zips.csv', 'r')
try:
  for line in h.readlines()[1:]:
    line = line[:-1].split(',')
    line [0] = int(line[0])
    line [4] = int(line[4])
    states_and_areas.append(line)
finally:
   h.close()

for line in zip_array:
  location = next(x for x in states_and_areas if x[0]== line)
  location = [location[1],location[4]]
  


print(final_array)
# print(next(x for x in states_and_areas if x[0]== 64148))

# zips can be found with bisectional serach, don't need brute force