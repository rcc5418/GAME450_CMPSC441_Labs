import requests
import random
import re

API_TOKEN = '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'
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json={"inputs": payload})
    return response.json()

def generate_paragraph(prompt, target_length=10):
    paragraph = ""
    while len(paragraph) < target_length:
        response = query(prompt)
        paragraph += str(response)
        prompt = paragraph[-200:]  # Use the last 200 characters as the prompt for the next query
    # Split the string by "'generated_text': '"
    # Remove the trailing ']'
    generated_text = paragraph[20:]
    generated_text = generated_text.rstrip("'}]")

    return generated_text

def standard_journal():
    possible_prompts=[
        "My name is Oillill. I've been traveling for ",
        "Oillill here. Recently, I've been thinking about ",
        "This journey has been long and hard, yet ",
        "I've been walking for so long, my feet ",
        "Today's travels were mostly uneventful, apart from ",
        "My travels have not been kind to my finances, "
    ]
    prompt = possible_prompts[random.randint(0,5)]
    paragraph = generate_paragraph(prompt)
    return paragraph
def battle_journal():
    possible_prompts=[
        "My name is Oillill, and my blade is sharp. ",
        "Oillill here. The bandits have been agressive, ",
        "This journey has been very treacherous, ",
        "A bandit attacked me today, but I managed to ",
        "Today's travels were harsh, I was ambushed on the road by ",
        "Don't these bandits have families? "
    ]
    prompt = possible_prompts[random.randint(0,5)]
    paragraph = generate_paragraph(prompt)
    return paragraph
def tired_journal():
    possible_prompts=[
        "My name is Oillill, and this journey may be the death of me. ",
        "Oillill here. How can this road be so long? ",
        "Between the bandits and my exhaustion, it's a wonder I can stand, but ",
        "I fear I may not survive this quest, ",
        "If you've taken this journal from my corpse's hands, please ",
        "The sun is unkind on days like these, though "
    ]
    prompt = possible_prompts[random.randint(0,5)]
    paragraph = generate_paragraph(prompt)
    return paragraph
def optimistic_journal():
    possible_prompts=[
        "My name is Oillill, and for once, things are looking up! ",
        "Oillill here. My progress today was much better than ",
        "My stores should be enough to survive me the journey, and",
        "This quest has been difficult, but rewarding. I think ",
        "I hope to read this journal to my descendants one day. Maybe ",
        "The weather has been fair, thankfully. If only "
    ]
    prompt = possible_prompts[random.randint(0,5)]
    paragraph = generate_paragraph(prompt)
    return paragraph
#print(standard_journal())
#print(battle_journal())
#print(tired_journal())
print(optimistic_journal())