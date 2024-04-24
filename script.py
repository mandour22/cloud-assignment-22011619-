import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download NLTK resources (run only once)
nltk.download('punkt')
nltk.download('stopwords')

# File path to the random_paragraphs.txt within the Docker container
file_path_custom = "random_paragraphs.txt"

# Read the contents of the file
with open(file_path_custom, "r") as file_custom:
    paragraph_text_custom = file_custom.read()

# Tokenize the text into words
word_tokens_custom = nltk.word_tokenize(paragraph_text_custom)

# Remove stop words
stop_words_custom = set(stopwords.words('english'))
filtered_word_tokens_custom = [word for word in word_tokens_custom if word.lower() not in stop_words_custom]

# Count the frequency of each word
word_frequencies_custom = Counter(filtered_word_tokens_custom)

# Display word frequency count
for word_custom, frequency_custom in word_frequencies_custom.items():
    print(f"{word_custom}: {frequency_custom}")
