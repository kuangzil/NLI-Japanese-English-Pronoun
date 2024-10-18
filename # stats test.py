# stats test
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# loading tfidf data
english_tfidf = pd.read_csv(r"D:\LIS 501 Intro to text mining\Japanese spoken corpora\NICT_JLE_4.1\NICT_JLE_4.1\tfidf\longer_tfidf_ENG\longer_token_ENG_pronoun_scores.csv", index_col=0)
japanese_tfidf = pd.read_csv(r"D:\LIS 501 Intro to text mining\Japanese spoken corpora\NICT_JLE_4.1\NICT_JLE_4.1\tfidf\longer_ifidf_JP\longer_JP_pronoun_scores.csv", index_col=0)

# get the column data for pronouns
pronouns = english_tfidf.columns.intersection(japanese_tfidf.columns)

# check whether there are 0 in the column to avoid log0 (extreme small value)
english_tfidf = english_tfidf.replace(0, np.nan)
japanese_tfidf = japanese_tfidf.replace(0, np.nan)

# doing log10 transformation
data1_log10 = np.log10(english_tfidf[pronouns])
data2_log10 = np.log10(japanese_tfidf[pronouns])

# Z-score normalization I decide not to use to because I need to mark the differences
#data1_z = data1_log10.apply(lambda x: (x - np.mean(x)) / np.std(x), axis=0)
#data2_z = data2_log10.apply(lambda x: (x - np.mean(x)) / np.std(x), axis=0)

# make visualiztion work
plt.figure(figsize=(15, 10))

for i, pronoun in enumerate(pronouns):
    plt.subplot(4, 4, i+1)  # 4x4 layout
    sns.histplot(data1_log10[pronoun], kde=True, label='English', color='blue')
    sns.histplot(data2_log10[pronoun], kde=True, label='Japanese', color='red')
    plt.title(f'Distribution for {pronoun}')
    plt.legend()

plt.tight_layout()
plt.show()

# performing t-test
for pronoun in pronouns:
    valid_data1 = data1_log10[pronoun].dropna()
    valid_data2 = data2_log10[pronoun].dropna()

    if len(valid_data1) > 1 and len(valid_data2) > 1:
        t_stat, p_value = stats.ttest_ind(valid_data1, valid_data2, equal_var=False)
        print(f"Pronoun: {pronoun}, T-statistic: {t_stat}, P-value: {p_value}")
    else:
        print(f"Pronoun: {pronoun} has insufficient data for t-test.")


