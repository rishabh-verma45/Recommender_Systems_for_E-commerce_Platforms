import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import messagebox

# Load product data
df = pd.read_csv("products.csv")

# Combine only brand for similarity
def combine_features(row):
    return row['Brand']

df["Combined"] = df.apply(combine_features, axis=1)

# Recommendation logic
def recommend_product():
    user_input = entry.get().strip()

    if user_input not in df['Name'].values:
        messagebox.showerror("❌ Error", "Product not found. Try typing full name exactly.")
        return

    index = df[df['Name'] == user_input].index[0]
    selected_category = df.loc[index, 'Category']

    category_df = df[df['Category'] == selected_category].reset_index(drop=True)

    vectorizer = TfidfVectorizer()
    category_features = vectorizer.fit_transform(category_df["Brand"])
    similarity = cosine_similarity(category_features)

    category_index = category_df[category_df['Name'] == user_input].index[0]
    scores = list(enumerate(similarity[category_index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:4]

    result_text = f"\n📦 Because you liked '{user_input}', here are similar {selected_category} items:\n\n"
    for i in sorted_scores:
        result_text += f"• {category_df.iloc[i[0]]['Name']} ({category_df.iloc[i[0]]['Brand']})\n"

    result_label.config(text=result_text)

# GUI Design
root = tk.Tk()
root.title("🛒 Smart Product Recommender")
root.geometry("550x400")
root.configure(bg="#f0f4f7")

# Header
header = tk.Label(root, text="Smart Product Recommender", font=("Segoe UI", 20, "bold"), bg="#f0f4f7", fg="#0c4a6e")
header.pack(pady=20)

# Entry label
prompt = tk.Label(root, text="Enter a product name exactly (e.g. 'Red T-Shirt'):", font=("Segoe UI", 12), bg="#f0f4f7")
prompt.pack()

# Entry box
entry = tk.Entry(root, font=("Segoe UI", 12), width=40, bd=2, relief="groove")
entry.pack(pady=10)

# Button
btn = tk.Button(root, text="🔍 Recommend", font=("Segoe UI", 12, "bold"), bg="#1e90ff", fg="white", padx=10, pady=5, command=recommend_product)
btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Segoe UI", 11), bg="#f0f4f7", justify="left", wraplength=500)
result_label.pack(pady=10)

# Footer
footer = tk.Label(root, text="Made by Rishabh", font=("Segoe UI", 10), bg="#f0f4f7", fg="#888")
footer.pack(side="bottom", pady=10)

root.mainloop()
