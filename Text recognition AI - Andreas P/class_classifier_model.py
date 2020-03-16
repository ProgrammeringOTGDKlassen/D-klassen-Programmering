from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

filepath_dict = {
    # "Byggeri & energi": "data/classes/byg.txt",
    # "Dansk": "data/classes/dan.txt",
    # "Matematik": "data/classes/mat.txt",
    "yelp": "data/sentiment_analysis/yelp_labelled.txt",
    "combined": "data/classes/combined_test.txt",
}

# Labels:
# 1: Byg
# 2: Dan
# 3: Mat

df_list = []
for text_class, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names=["sentence", "label"], sep="\t")
    df["text_class"] = text_class  # Add another column filled with the source name
    df_list.append(df)

df = pd.concat(df_list)


df_yelp = df[df["text_class"] == "yelp"]

sentences = df_yelp["sentence"].values
y = df_yelp["label"].values

print(f"Yelp has the value {y=}")


df_combined = df[df["text_class"] == "combined"]

sentences = df_combined["sentence"].values
y = df_combined["label"].values

print(f"Y has the value {y=}")

sentences_train, sentences_test, y_train, y_test = train_test_split(
    sentences, y, test_size=0.25, random_state=1000
)


vectorizer = CountVectorizer()
vectorizer.fit(sentences_train)

X_train = vectorizer.transform(sentences_train)
X_test = vectorizer.transform(sentences_test)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)
score = classifier.score(X_test, y_test)
print("Accuracy:", score)

test_index = 1
for i in range(0, 10):
    test_sentence = [X_test[i], sentences_test[i]]
    prediction = classifier.predict(test_sentence[0])
    if prediction[0] == 1:
        class_name = "Byggeri og Energi"
    elif prediction[0] == 2:
        class_name = "Dansk"
    elif prediction[0] == 3:
        class_name = "Matematik"

    print(
        f'\nPrediction {i+1}: \nThe test sentence is: \n"{test_sentence[1]}"\n\nThe algorithm guesses that the class of this sentence is: {class_name}\n'
    )
