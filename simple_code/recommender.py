import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("products.csv")

# Combine features into a single string
def combine_features(row):
    return row['Category'] + " " + row['Brand']

df["Combined"] = df.apply(combine_features, axis=1)

# Convert text to feature vectors
vectorizer = TfidfVectorizer()
feature_matrix = vectorizer.fit_transform(df["Combined"])

# Compute cosine similarity
similarity = cosine_similarity(feature_matrix)

# Recommend products
def recommend(product_name):
    if product_name not in df['Name'].values:
        return "❌ Product not found."
    
    index = df[df['Name'] == product_name].index[0]
    similarity_scores = list(enumerate(similarity[index]))
    sorted_products = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:4]  # top 3

    print(f"\n🛒 Because you liked '{product_name}', you may also like:")
    for i in sorted_products:
        print("→", df.iloc[i[0]]["Name"])

# Example
if __name__ == "__main__":
    print("E-commerce Product Recommender")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter product name: ")

        if user_input.lower() == 'exit':
            print("👋 Goodbye!")
            break

        recommend(user_input)
