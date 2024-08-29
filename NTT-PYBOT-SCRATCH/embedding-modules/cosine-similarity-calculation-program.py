# Program to measure the similarity between two sentences using cosine similarity

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample input sentences
# Uncomment the lines below to take input from the user
# X = input("Enter first string: ").lower()
# Y = input("Enter second string: ").lower()
X = "I love horror movies"
Y = "Lights out is a horror movie"

# Tokenization: splitting the sentences into words
X_list = word_tokenize(X)
Y_list = word_tokenize(Y)

# Load the list of stopwords from NLTK
sw = stopwords.words('english')

# Initialize empty lists to store the frequency of words
l1 = []
l2 = []

# Remove stopwords from the tokenized lists
X_set = {w for w in X_list if not w in sw}
Y_set = {w for w in Y_list if not w in sw}

# Form a set containing all unique words from both sentences
rvector = X_set.union(Y_set)

# Create vectors based on the presence of words in each sentence
for w in rvector:
    if w in X_set:
        l1.append(1)  # Word present in X
    else:
        l1.append(0)  # Word absent in X
    if w in Y_set:
        l2.append(1)  # Word present in Y
    else:
        l2.append(0)  # Word absent in Y

# Calculate the dot product of the vectors
c = 0
for i in range(len(rvector)):
    c += l1[i] * l2[i]

# Calculate the magnitude of the vectors
magnitude_X = sum(l1) ** 0.5
magnitude_Y = sum(l2) ** 0.5

# Calculate cosine similarity
cosine = c / float(magnitude_X * magnitude_Y)

print("similarity:", cosine)

'''
Output => similarity:  0.2886751345948129
'''

# Detailed explanation for each section:

# 1. Import necessary libraries from NLTK
#    We import the `stopwords` and `word_tokenize` functions from the NLTK library. 
#    `stopwords` provides a list of common words that are usually filtered out in text analysis. 
#    `word_tokenize` is used to split the sentences into individual words.

# 2. Sample input sentences
#    Two example sentences are given directly in the code for simplicity.
#    If you want to take input from the user, uncomment the input lines and comment out the example sentences.

# 3. Tokenization
#    The sentences are converted to lowercase and then split into individual words using `word_tokenize`. 
#    This process helps in handling each word separately for further analysis.

# 4. Stopwords
#    Stopwords are common words that do not carry significant meaning in text analysis (e.g., "the", "is"). 
#    We load the list of English stopwords from NLTK and filter them out from the tokenized lists.

# 5. Creating Vectors
#    A set containing all unique words from both sentences is created. 
#    For each unique word, we create two vectors: one for the first sentence and one for the second sentence. 
#    If a word is present in the sentence, it is represented by 1, otherwise by 0.

# 6. Dot Product
#    The dot product of the two vectors is calculated. 
#    This involves multiplying the corresponding elements of the two vectors and summing the results.

# 7. Magnitude
#    The magnitude (or length) of each vector is calculated. 
#    This is done by taking the square root of the sum of the squares of the elements of the vector.

# 8. Cosine Similarity
#    The cosine similarity is calculated using the dot product and the magnitudes of the two vectors. 
#    The result is a measure of the similarity between the two sentences, ranging from 0 to 1, where 1 indicates identical sentences.

#================================================================================================

'''
Detailed Explanation of Each Section

Import Necessary Libraries
We import stopwords and word_tokenize from the NLTK library. The stopwords function provides a list of common words that are usually filtered out in text analysis,
 while word_tokenize is used to split the sentences into individual words.

Sample Input Sentences
Two example sentences are given directly in the code for simplicity. If you want to take input from the user, you can uncomment the input lines and comment out the example sentences provided.

Tokenization
Tokenization is the process of converting sentences into a list of individual words. This is done using the word_tokenize function.
 The sentences are first converted to lowercase to ensure consistency and then split into words. This allows us to handle each word separately for further analysis.

Stopwords
Stopwords are common words that do not carry significant meaning in text analysis, such as "the", "is", and "in". 
We load the list of English stopwords from NLTK and remove these stopwords from the tokenized word lists to focus on the more meaningful words.

Creating Vectors
We create a set containing all unique words from both sentences. For each unique word, we create two vectors: one for the first sentence and one for the second sentence.
 If a word is present in a sentence, it is represented by 1 in the vector, otherwise by 0. This binary representation helps in comparing the presence or absence of words between the sentences.

Dot Product
The dot product of the two vectors is calculated by multiplying the corresponding elements of the vectors and summing the results. 
The dot product provides a measure of how many words the two sentences have in common.

Magnitude
The magnitude (or length) of each vector is calculated by taking the square root of the sum of the squares of the elements of the vector. 
The magnitude represents the size of the vector in the multi-dimensional space.

Cosine Similarity
Finally, the cosine similarity is calculated using the dot product and the magnitudes of the two vectors. 
The cosine similarity measures the cosine of the angle between the two vectors, providing a value between 0 and 1, where 1 indicates identical sentences and 0 indicates no similarity.
 This value represents the degree of similarity between the two input sentences.
 
'''
