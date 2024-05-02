from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import re

# Step 1: Read Data from Markdown File
with open("content_new.md", "r", encoding='utf-8') as file:
    content = file.read()

# Extracting text data from the markdown content (excluding the id)
data_set_examples = re.findall(r"###[^\n]+\n\n(.+?)(?=\n\n###[^\n]+|\Z)", content, re.DOTALL)

# Step 2: Text Vectorization
vectorizer = TfidfVectorizer()
X_transformed = vectorizer.fit_transform(data_set_examples)

# Static question types
question_types = ["Find.All", "Find.Optimal", "Find.Count", "Find.Example", "Prove", "ProveDisprove", "Algorithm"]

# Step 3: Create static question types for each example
question_types_encoded = [question_types for _ in range(len(data_set_examples))]

# Step 4: Combine Encoded Question Types with Text Features
X_combined = X_transformed.toarray()
for i in range(len(X_combined)):
    X_combined[i] = list(X_combined[i]) + list(question_types_encoded[i])

# Step 5: Split Data
X_train, X_test = train_test_split(X_combined, test_size=0.3, random_state=42)

# Step 6: Train the SVM Classifier
model = SVC(kernel='linear')  # Linear kernel is often a good choice for text classification.
model.fit(X_train, y_train)

# Step 7: Model Evaluation
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
