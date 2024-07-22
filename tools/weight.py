import json

with open('implicit.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

prompts_dict = {}
for line in lines:
    prompt = line.strip().split('--prompt')[1]
    key = prompt.split(',')[0]
    prompts_dict[key] = 1

json_data = json.dumps(prompts_dict, ensure_ascii=False, indent=4)

with open('prompts.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print("Prompts JSON file created successfully!")
