import ollama
sentenceList = [
    "The Dynastinae are among the largest of beetles, reaching more than 15 centimetres (6 inches) in length, but are completely harmless to humans because they cannot bite or sting.", 
    "Some species have been anecdotally claimed to lift up to 850 times their own weight.", 
    "An extinct Eocene Oryctoantiquus borealis was the largest fossil scarabeid, with a length of 5 centimetres (2.0 in).", 
    "Some modern Oryctini grew up to 7 cm (3 in).", 
    "Common names of the Dynastinae refer to the characteristic horns borne only by the males of most species in the group.", 
    "Each has a horn on the head and another horn pointing forward from the center of the thorax.",
    "The horns are used in fighting other males during mating season, and for digging.", 
    "The size of the horn is a good indicator of nutrition and physical health."
    ]#[:1] #For debugging purposes
sentenceEmbeddings = []
for sentence in sentenceList:
    sentenceEmbeddings.append(ollama.embeddings(model='llama2', prompt=f'{sentence}')['embedding'])

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

print("Please enter a query (Preferably about the Rhino beetle): ")
consoleInput = input()
#consoleInput = "Rhino beetles are very large, aren't they?" #rcc: Used for debugging
inputEmbedding = ollama.embeddings(model='llama2', prompt=f'{consoleInput}')['embedding']

similarityList = []

for embedding in sentenceEmbeddings:
    similarity = cosine_similarity([inputEmbedding],[embedding])
    similarityList.append(float(similarity))

combined_data = list(zip(sentenceList, similarityList))
sorted_data = sorted(combined_data, key=lambda x: x[1], reverse=True)
sorted_sentences = [item[0] for item in sorted_data]
sorted_numbers = [item[1] for item in sorted_data]

contextSentence = ""
for i in range(3):
    contextSentence += sorted_sentences[i]
    contextSentence += " "
query = contextSentence + " " + consoleInput 
response = ollama.generate(model='llama2', prompt=query)
print(response['response'])