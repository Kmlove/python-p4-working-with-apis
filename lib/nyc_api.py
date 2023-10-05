
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content


  def program_schools(self):
    programs = json.loads(self.get_programs())

    agencies = [program["agency"] for program in json.loads(self.get_programs())]
    return agencies

# Makes creates an instance of GetPrograms and then calls the instance method all in one like
programs = GetPrograms().program_schools()

for school in set(programs):
  print(school)

# Another method to go about it
# programs = GetPrograms() # First create an instance of GetPrograms
# print(programs.get_programs()) # Calling the instance method on the object
