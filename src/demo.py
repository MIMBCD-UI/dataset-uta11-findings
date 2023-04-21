import json

# Open the JSON file and read its contents
with open('dataset/00c862f7-f081-41a3-85ba-daf14328b0a9.json') as f:
    data = json.load(f)

# Access the data in the JSON file
print(data['rawData']['studyId'])
print(data['rawData']['modality'])
print(data['rawData']['stacks'])
