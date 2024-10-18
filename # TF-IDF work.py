# TF-IDF work 
import os


import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
# reading the file from folder
input_folder = r"D:\LIS 501 Intro to text mining\Japanese spoken corpora\NICT_JLE_4.1\NICT_JLE_4.1\tokens\long_token_ENG"
output_folder=r"D:\LIS 501 Intro to text mining\Japanese spoken corpora\NICT_JLE_4.1\NICT_JLE_4.1\tfidf\longer_tfidf_ENG"
os.makedirs(output_folder, exist_ok=True)

def tfidf_from_txt(file_path, output_prefix):
    # reading and getting txt text
    with open(file_path, 'r', encoding='utf-8') as file:
        documents = file.readlines()
    
    # strip out indents and \n    
    documents = [doc.strip().lower() for doc in documents if doc.strip()]
    
    
    # make a variable to initialize TF-IDF
    vectorizer = TfidfVectorizer()
    
    
    
    # transform and fit the document we need to process
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # using pandas to build a dataframe for visualization
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
    
    
      

    tfidf_df.to_csv(os.path.join(output_folder,f'{output_prefix}_tfidf.csv'), index=False)

    # make out the pronouns we wnat to examine
    pronouns = [
    'i',       # first person singular
    'you',     # second person singular/plural
    'he',      # third person singular (male)
    'she',     # third person singular (female)
    'it',      # third person singular (neutral)
    'we',      # first person plural
    'they',     # third person plural
    'my',      # first person singular possessive
    'your',    # second person singular/plural possessive
    'his',     # third person singular possessive (male)
    'her',     # third person singular possessive (female)
    'its',     # third person singular possessive (neutral)
    'our',     # first person plural possessive
    'their',   # third person plural possessive
    'that'     # can function as a subject in certain contexts
]
    #here i encountered a problem: I can not find 'I' in the vectorized file. The problem is on vectorizer

# search the targeted scores and vectors
# we need to see whether there are columns of pronouns with scores on it. 
    available_pronouns = tfidf_df.columns.intersection(pronouns)
    if not available_pronouns.empty:
           pronoun_scores = tfidf_df[available_pronouns]
           df_non_zero = pronoun_scores.loc[:, (pronoun_scores != 0).any(axis=0)]
           #print(df_non_zero)
         

   # if the score of vector is not0, it would be shown

    df_non_zero =   pronoun_scores.loc[:, (  pronoun_scores != 0).any(axis=0)]

# output the result
   # print(df_non_zero)

# save it to CSV file

    df_non_zero.to_csv(os.path.join(output_folder,f"{output_prefix}_pronoun_scores.csv"),index=False)
    
    
    return tfidf_df

# process each text file in the input folder
for filename in os. listdir(input_folder):
    if filename.endswith('.txt'):
        file_path=os. path.join(input_folder, filename)
        output_prefix=os. path. splitext(filename)[0]
        tfidf_results= tfidf_from_txt(file_path, output_prefix)





# print heads
        #print(tfidf_results.head())



# open the file and read 
# we are reading the text in a csv way
#df_non_zero = pd.read_csv( r"D:\LIS 501 Intro to text mining\Japanese spoken corpora\NICT_JLE_4.1\NICT_JLE_4.1\tf-idf result_jp\pronoun_scores001.csv")
#print(df_non_zero.head())



'''
import seaborn as sns
import matplotlib.pyplot as plt

# draw a heat map

plt.figure(figsize=(10, 6))
sns.heatmap(df_non_zero, annot=True, cmap='YlGnBu', cbar=True, fmt=".2f")
plt.title('TF-IDF Heatmap of Non-Zero Pronouns')
plt.xlabel('Terms')
plt.ylabel('Documents')
plt.show()
'''