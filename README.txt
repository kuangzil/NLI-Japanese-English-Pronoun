Native Language Identification (NLI) Project
Project Overview
This project investigates the linguistic differences in pronoun usage between native Japanese speakers and native English speakers. The study focuses on how cultural and grammatical distinctions shape pronoun usage, providing insights into second language acquisition (SLA) and improving Native Language Identification (NLI). By analyzing data from the NICT Japanese Learner English (NICT_JLE) Corpus, the project aims to develop a classification model for distinguishing texts based on the native language of their authors.

Objective
To create a robust model that identifies whether an English text was written by a native English speaker or a Japanese learner of English. This study emphasizes the analysis of pronoun usage and its role in text classification.

Key Linguistic Features:
Third-Person Pronouns:
Native English speakers frequently use "he," "she," and "it."
Japanese learners often omit these due to cultural reliance on context.
Demonstratives:
Expressions like "that person" are common among Japanese learners, reflecting linguistic transfer.
Possessive Determiners:
Pronouns like "his," "her," "their" show distinct patterns between groups.
Current Progress
1. Corpus
Dataset:
The NICT_JLE Corpus contains spoken English responses from TOEFL iBT exams by Japanese learners and native English speakers. The dataset is tokenized, cleaned, and balanced for analysis.
Data Balancing:
To compensate for data imbalance (fewer native English speaker samples), oversampling was applied to achieve comparable sample sizes.
2. Feature Extraction
TF-IDF Vectorization:
TF-IDF was applied to measure the importance of pronouns across texts. A log10 transformation normalized the distribution.
Statistical Validation:
T-tests demonstrated significant differences in pronoun usage between groups, supporting the hypothesis that native language influences pronoun patterns.
3. Visualization
WordClouds:
Visualized frequent pronouns like "it," "you," and "that" for native English speakers and "you" and "my" for Japanese learners.
Dimensionality Reduction:
PCA and t-SNE were employed to reduce the feature space and visualize pronoun clusters.
4. Modeling
Classifier:
Support Vector Machines (SVM) achieved an 81% accuracy rate in distinguishing between Japanese and English speaker-generated texts.
Evaluation:
Metrics such as precision, recall, and F1 score confirmed the model's reliability.
Key Findings
Pronoun Usage:
Japanese learners overuse "you" but underuse reflexive pronouns like "myself" or "herself."
Native English speakers frequently use "it" and "that" as dummy subjects, a concept absent in Japanese.
Statistical Evidence:
All p-values from t-tests were < 0.05, confirming significant linguistic differences.
Cultural Influences:
Japanese emphasizes collectivism, leading to different pronoun preferences compared to English.
Challenges
Data Imbalance:
Oversampling was required to address the disparity in dataset sizes.
Syntactic Patterns:
The study primarily focused on lexical features (e.g., pronouns) and did not incorporate syntactic dependencies.
Reflexive Pronouns:
Limited representation in the dataset restricted further analysis.
Future Directions
Incorporate Advanced NLP Models:
Utilize BERT to detect syntactic structures like dummy subjects and pro-drop phenomena.
Expand Dataset:
Include learners with varying English proficiency levels for broader applicability.
Generalization:
Extend the model to classify texts from other non-native English speaker groups.
Applications
Language Learning Tools:
Highlight challenging areas in pronoun usage for Japanese learners.
NLP Systems:
Enhance machine translation and sentiment analysis by accounting for cultural and linguistic nuances.
Native Language Identification:
Develop more effective models for multilingual text classification.
Contact
For questions or collaboration inquiries, feel free to contact:
Kuangzi Li
Master's Student in Linguistics
University of Wisconsin-Madison
Email: kli376@wisc.edu
