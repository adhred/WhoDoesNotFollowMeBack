import json

# Read the JSON data
with open('following.json', 'r') as file:
    data = json.load(file)

with open('followers_1.json', 'r') as file:
    data_1 = json.load(file)

# Extract following list
following_list = []
follower_list = []

for relationship in data['relationships_following']:
    string_list_data = relationship['string_list_data']
    for item in string_list_data:
        following_list.append(item['value'])

for entry in data_1:
    string_list_data = entry['string_list_data']
    for item in string_list_data:
        follower_list.append(item['value'])

result = list(set(following_list).difference(follower_list))
print(result)
