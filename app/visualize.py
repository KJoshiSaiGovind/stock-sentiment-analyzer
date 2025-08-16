import matplottlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import pandas as pd

df = pd.read_csv("data/all-data.csv", encoding='latin-1')
df.columns = ['Sentiment', 'Text']

def plot_class_distribution():
    plt.figure(figsize=(6, 4))
    sns.countplot(x='Sentiment', data=df, palette="Set2")
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.show()

def plot_wordcloud(sentiment):
    text = " ".join(df[df['Sentiment'] == sentiment]['Text'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(f"WordCloud for {sentiment} Sentiment")
    plt.show()

if __name__ == "__main__":
    plot_class_distribution()
    plot_wordcloud("positive")
    plot_wordcloud("negative")
