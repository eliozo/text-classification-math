from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer
from string_preprocessing import *

(fragments, topics) = read_file('all_ten_categories.tsv')

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Fit the vectorizer on the tokenized text fragments
vectorizer.fit([' '.join(f) for f in fragments])

# Convert the tokenized text fragments to numerical representation
X = vectorizer.transform([' '.join(f) for f in fragments])

# Convert the sparse matrix representation to a dense array
X = X.toarray()

# Create target labels
y = topics

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Perform feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the KNN classifier with K = 5
knn = KNeighborsClassifier(n_neighbors=5)

# Train the classifier on the training data
knn.fit(X_train, y_train)

# Predict the labels for the test data
y_pred = knn.predict(X_test)

# Initialize and train the Radius Neighbors Classifier
# classifier = RadiusNeighborsClassifier(radius=0.5)
# classifier.fit(X_train_scaled, y_train)

# Make predictions on the test set
# y_pred = classifier.predict(X_test_scaled)

# Evaluate the classifier
print(classification_report(y_test, y_pred))
