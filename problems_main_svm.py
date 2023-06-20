from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from string_preprocessing import *

(fragments, topics) = read_file('all_ten_categories.tsv')

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

