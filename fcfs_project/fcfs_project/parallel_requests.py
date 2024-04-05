import requests
from concurrent.futures import ThreadPoolExecutor

prompts = [
    "Prompt 1: What are some strategies for improving productivity at work?",
    "Prompt 2: Can you provide some insights of FCFS app!",
]

def make_llm_request(prompt):
    base_url = "http://127.0.0.1:8000/process/"

    url = base_url + "?prompt=" + prompt

    response = requests.get(url)

    return response.json()

def process_prompts(prompts):
    with ThreadPoolExecutor(max_workers=len(prompts)) as executor:
        future_to_prompt = {executor.submit(make_llm_request, prompt): prompt for prompt in prompts}
        
        for future in future_to_prompt:
            prompt = future_to_prompt[future]
            try:
                response = future.result()
                print(response)
            except Exception as exc:
                print(f"Processing of prompt '{prompt}' raised an exception: {exc}")

process_prompts(prompts)