# 🛒 Product Recommender System (Category-Based)

A simple yet effective **Product Recommendation System** using **Python, Pandas, Scikit-learn**, and a modern **Tkinter GUI**.

This app recommends similar products based on **brand similarity within the same category** — just like an e-commerce platform (Amazon, Flipkart) might suggest.

---

## 🚀 Features

- 🔍 Recommends products based on user selection
- 📦 Category-wise filtering for relevant suggestions
- 🖥️ User-friendly and styled GUI using Tkinter
- ⚡ Fast and lightweight — runs offline

---

## 📸 Screenshot

> ![screenshot](screenshot.png)

*_(Optional: Add a screenshot of your app GUI and name it `screenshot.png` in the repo)_*

---

## 🧠 How It Works

1. The user enters a product name
2. The system identifies its **category** (e.g., Clothing, Shoes)
3. It finds similar products **from the same category**, based on **brand**
4. Shows top 3 recommendations

---

## 🧰 Tech Stack

- Python 3.x
- Pandas
- Scikit-learn
- Tkinter (for GUI)
- Cosine Similarity & TF-IDF (for recommendation)

---

## 📂 Dataset Used

A custom CSV file with the following columns:

```csv
ProductID,Name,Category,Brand
1,Red T-Shirt,Clothing,Nike
2,Blue T-Shirt,Clothing,Adidas
...
