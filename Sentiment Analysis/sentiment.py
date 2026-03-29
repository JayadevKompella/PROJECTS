import pandas as pd
from textblob import TextBlob
import tkinter as tk
from tkinter import filedialog
import os

def get_sentiment(text):
    if not isinstance(text, str):
        return 0.0, "Neutral"
    score = TextBlob(text).sentiment.polarity
    label = "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"
    return score, label

def process_file():
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if not filename:
        return
    
    df = pd.read_excel(filename, header=None)
    results = []
    for row in df.values:
        for cell in row:
            if pd.notna(cell):
                score, label = get_sentiment(str(cell))
                results.append([cell, score, label])
    
    pd.DataFrame(results, columns=["Comment", "Score", "Sentiment"]).to_excel("results.xlsx", index=False)
    print("Success. Results saved to results.xlsx")

if __name__ == "__main__":
    process_file()
