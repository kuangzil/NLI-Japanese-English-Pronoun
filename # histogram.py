# histogram
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Replace zeros with NaN and drop rows where all values are NaN
    
df = pd.read_csv(r"D:\LIS 501 Intro to text mining\Japanese spoken corpora\NICT_JLE_4.1\NICT_JLE_4.1\tfidf\longer_ifidf_JP\longer_JP_pronoun_scores.csv")

       
# get rid of 0 because there are too many 0s， I modified data frame to strip out all the 0
df_no_zeros = df.map(lambda x: None if x == 0 else x)
      
# Plot histograms for each column 
df_no_zeros.plot(kind='hist', subplots=True ,  layout=(5, 3), figsize=(10, 12), bins=10, legend=True, sharex=False)
#use subplots=True rather than subplot= True
       
plt.tight_layout()
plt.show()
# do a log 10 transformation and z score normalization.
    

# use log 10 transformation
log_data = np.log10(df_no_zeros)

# visualization for the log10
#log_data.plot(kind='hist', subplots=True ,  layout=(5, 3), figsize=(10, 12), bins=10, legend=True, sharex=False)






# mean of the data set

μ = log_data.mean()
sd= log_data.std()

df_z_score=(log_data-μ)/sd

#print(df_z_score)

#df_z_score.plot(kind='hist', subplots=True ,  layout=(5, 3), figsize=(10, 12), bins=10, legend=True, sharex=False)
#plt.tight_layout()
#plt.show()