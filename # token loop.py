import os
import pandas as pd
import nltk
import re
from bs4 import BeautifulSoup
import time
import en_core_web_sm

# loading spaCy
nlp = en_core_web_sm.load()

# folder path
folder_path = r"C:\Users\likua\OneDrive\Desktop\count"
output_folder = r"C:\Users\likua\OneDrive\Desktop\result"

# to see whether there is a file in the output folder, if there is not, create one
os.makedirs(output_folder, exist_ok=True)

# recording start time 
start_time = time.time()

# know every txt file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        
        # read what's in the file
        with open(file_path, 'r', encoding='utf-8',errors='replace') as file:
            jp1 = file.read()

        # noise removal
        soup = BeautifulSoup(jp1, 'lxml')
        cleaned_text = soup.get_text(separator=' ')
        cleaned_sentences = re.sub(r'<.+>|[0-9]+', ' ', cleaned_text)


        # tokenize
        sentences = nltk.sent_tokenize(cleaned_sentences)

        # store the tokens to DataFrame
        df = pd.DataFrame(sentences, columns=['sentence'])

        # writing in csv files
        output_file_path = os.path.join(output_folder, f'{filename}_sentences.txt')
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for sentence in sentences:
                output_file.write(sentence + '\n')

# recording end time
end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f} seconds")