from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from string_preprocessing import *
from extract_html import *

(fragments, topics) = read_all_htmls()

# Preprocess the text
preprocessed_fragments = [' '.join(fragment) for fragment in fragments]

# Initialize the TfidfVectorizer
vectorizer = TfidfVectorizer()

# Fit the vectorizer on the preprocessed text fragments
vectorizer.fit(preprocessed_fragments)

# Convert the preprocessed text fragments to numerical representation
X = vectorizer.transform(preprocessed_fragments)

# Create target labels
y = topics

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Perform feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train.toarray())
X_test_scaled = scaler.transform(X_test.toarray())

# Initialize the KNN classifier with K = 3
knn = KNeighborsClassifier(n_neighbors=3)

# Train the classifier on the training data
knn.fit(X_train_scaled, y_train)

# Predict the labels for the test data
y_pred = knn.predict(X_test_scaled)

# Evaluate the classifier
print(classification_report(y_test, y_pred))
