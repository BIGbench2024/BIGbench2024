import json
import os
from urllib import request, parse
import random

def queue_prompt(prompt, ip):
    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')
    req = request.Request(ip, data=data)
    response = request.urlopen(req)
    return response.read()

def load_prompts(filename):
    prompts = []
    with open(filename, "r") as file:
        for line in file:
            if '--prompt' in line:
                start = line.find('"') + 1
                end = line.rfind('"')
                if start > 0 and end > 0:
                    prompt = line[start:end]
                    prompts.append(prompt)
    return prompts

def truncate_prompt(prompt):
    parts = prompt.split(',', 3)  # 分割成最多四部分
    if len(parts) > 3:
        truncated = ','.join(parts[:3])  # 取前三部分
    else:
        truncated = prompt
    return truncated

def process_prompts(json_template, filename, ip):
    prompts = load_prompts(filename)
    for prompt_text in prompts:
        with open(json_template, 'r') as file:
          prompt = json.load(file)  
        file.close()
        prompt["6"]["inputs"]["text"] = prompt_text
        truncated_prompt = truncate_prompt(prompt_text)
        prompt["9"]["inputs"]["filename_prefix"] = truncated_prompt
        prompt["3"]["inputs"]["seed"] = random.randint(1000, 6000000000)
        response = queue_prompt(prompt, ip)
        print(f"Processed prompt: {prompt_text}, Response: {response}")

def generate_image(model, ip, data_path):
    workflow_path = model
    prompt_path = os.path.join(data_path, "prompt")
    for sub_attr in os.listdir(prompt_path):
        if sub_attr != "relation":
            for txt_file in os.listdir(os.path.join(prompt_path, sub_attr)):
                process_prompts(workflow_path, 
                                os.path.join(prompt_path, os.path.join(sub_attr, txt_file)),
                                ip)
        else:
            for sub_relation in os.listdir(os.path.join(prompt_path, sub_attr)):
                for txt_file in os.listdir(os.path.join(os.path.join(prompt_path, sub_attr), sub_relation)):
                    process_prompts(workflow_path, 
                                    os.path.join(os.path.join(prompt_path, sub_attr), os.path.join(sub_relation, txt_file)),
                                    ip)                    