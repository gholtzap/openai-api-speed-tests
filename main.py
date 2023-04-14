import openai
from dotenv import load_dotenv
import os
import time

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

prompts = [
    ["Explain the difference between classical and quantum computing."],
    ["Summarize the plot of George Orwell's novel, 1984."],
    ["What are the health benefits of a Mediterranean diet?"],
    ["Describe the process of photosynthesis in plants."],
    ["What are the key principles of Agile software development?"],
    ["Discuss the environmental impacts of plastic waste and possible solutions."],
    ["Analyze the influence of social media on mental health."],
    ["Explain Einstein's theory of general relativity in simple terms."],
    ["Compare and contrast the leadership styles of Abraham Lincoln and Winston Churchill."],
    ["How does blockchain technology work, and what are its applications?"]
]

list_max_tokens = [
    1024,
    512,
    128,
    32
]

temperatures = [
    0,
    0.5,
    1,
    1.5,
    2
]


def query(prompt, engine, temperature, max_tokens):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
    )

    message = response.choices[0].text.strip()
    return message


engine_ids = {
    "babbage": "text-babbage-001",
    "ada": "text-ada-001",

    "davinci": "text-davinci-001",
    "davinci2": "text-davinci-002",
    "davinci3": "text-davinci-003",

    "curie": "text-curie-001",
    "gpt3.5turbo": "gpt-3.5-turbo"


}

output = []

total_elapsed_time = 0

for temperature in temperatures:
    for max_token in list_max_tokens:
        average_elapsed_time = 0
        total_elapsed_time = 0
        for prompt in prompts:
            start_time = time.time()
            response = query(prompt, "text-curie-001", temperature, max_token)
            elapsed_time = time.time() - start_time
            total_elapsed_time += elapsed_time
            print(f"prompt: {prompt}\n response: {response}\n")
        average_elapsed_time = total_elapsed_time / len(prompts)

        output.append(
            f"Average time taken: {average_elapsed_time} seconds for temperature {temperature} and max_token {max_token}")

    output.append("-------------------------------")
print("##########################################################################################################################################")

for ot in output:
    print(ot)
