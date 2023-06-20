from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from string_preprocessing import *
from extract_html import *
from preprocess_text import *

# (fragments, topics) = read_file('all_ten_categories.tsv')
(fragments, topics) = read_all_htmls()

# Preprocess the text
preprocessed_fragments = [' '.join(fragment) for fragment in fragments]

# Create feature vectors using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_fragments)

# Create target labels
y = topics

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the SVM classifier
svm_classifier = SVC()
svm_classifier.fit(X_train, y_train)

# Predict on the test set
y_pred = svm_classifier.predict(X_test)

# Evaluate the classifier
print(classification_report(y_test, y_pred))

###################################################################################
problem1 = """The Bank of Oslo issues two types of coin: aluminum (denoted A) and bronze (denoted B). Marianne has $n$ 
aluminum 
coins and $n$ bronze coins arranged in a row in some arbitrary initial order. A chain is any subsequence of consecutive coins of the same type. Given a fixed positive integer $k \leq 2n$, Gilberty repeatedly performs the following operation: he identifies the longest chain containing the $k^{th}$ coin from the left and moves all coins in that chain to the left end of the row. For example, if $n=4$ and $k=4$, the process starting from the ordering $AABBBABA$ would be $AABBBABA \to BBBAAABA \to AAABBBBA \to BBBBAAAA \to ...$

Find all pairs $(n,k)$ with $1 \leq k \leq 2n$ such that for every initial ordering, at some moment during the process, the leftmost $n$ coins will all be of the same type."""
problem2 = """Let $\mathbb{R}^+$ denote the set of positive real numbers. Find all functions $f: \mathbb{R}^+ \to \mathbb{R}^+$ such that for each $x \in \mathbb{R}^+$, there is exactly one $y \in \mathbb{R}^+$ satisfying$$xf(y)+yf(x) \leq 2$$"""
problem3 = """Let $k$ be a positive integer and let $S$ be a finite set of odd prime numbers. Prove that there is at most one way (up to rotation and reflection) to place the elements of $S$ around the circle such that the product of any two neighbors is of the form $x^2+x+k$ for some positive integer $x$."""
problems = [problem1, problem2, problem3]
for problem in problems:
    # Load and preprocess the new sequence of tokens
    new_tokens = preprocess_text(problem)
    new_text = ' '.join(new_tokens)

    # Transform the new text into a feature vector using the same vectorizer
    new_X = vectorizer.transform([new_text])

    # Classify the new text using the trained SVM classifier
    new_prediction = svm_classifier.predict(new_X)

    # Print the predicted class
    print(new_prediction)
