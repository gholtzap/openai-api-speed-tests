import openai
from dotenv import load_dotenv
import os
import time

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
model_id = 'gpt-3.5-turbo'


# Note: gpt-3.5 is a conversation model and currently does not support fine-tuning (temperature, character limit) yet
def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )

    conversation.append(
        {'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    
    total_tokens = response['usage']['total_tokens']

    return conversation, total_tokens

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


def test_prompts(prompts):
    timings = []
    print('hello')
    for prompt in prompts:
        conversation = [
            {'role': 'system', 'content': 'How may I help you?'},
            {'role': 'user', 'content': prompt[0]}
        ]

        start_time = time.time()
        print(start_time)
        conversation, _ = ChatGPT_conversation(conversation)
        print(conversation)
        end_time = time.time()
        print(end_time)

        response_time = end_time - start_time
        print(response_time)
        timings.append(response_time)
        print(timings)

    return timings

response_timings = test_prompts(prompts)

for i, timing in enumerate(response_timings):
    print(f"Prompt {i + 1}: {prompts[i][0]} - Time: {timing:.2f} seconds")
   
def average_time(timings):
    return sum(timings) / len(timings)

print(average_time(response_timings))