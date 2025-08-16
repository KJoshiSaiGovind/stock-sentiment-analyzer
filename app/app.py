import streamlit as st
import pandas as pd
import plotly.express as px
from data_fetch import get_stock_data, get_tweets
from sentiment import analyze_sentiment

# Streamlit page setup
st.set_page_config(page_title="Stock Sentiment Analyzer", layout="centered")

st.title("📈 Real-Time Stock Sentiment Analyzer")

# Input stock symbol
symbol = st.text_input("Enter Stock Symbol", "AAPL")

if st.button("Analyze"):
    # Get stock price data
    stock_data = get_stock_data(symbol)

    if not stock_data.empty:
        # Pick correct x-axis column
        if "Date" in stock_data.columns:
            x_axis = "Date"
        elif "Datetime" in stock_data.columns:
            x_axis = "Datetime"
        else:
            x_axis = stock_data.columns[0]  # fallback

        # Plot stock price
        fig = px.line(stock_data, x=x_axis, y="Close", title=f"{symbol} Price Trend")
        st.plotly_chart(fig)
    else:
        st.error("❌ Could not fetch stock data. Try another symbol.")

    # Get tweets
    tweet_data = get_tweets(symbol)

    if not tweet_data.empty and "Error" not in tweet_data.iloc[0, 0]:
        # Apply sentiment analysis
        tweet_data["Sentiment Score"] = tweet_data["Tweet"].apply(analyze_sentiment)
        tweet_data["Sentiment"] = tweet_data["Sentiment Score"].apply(
            lambda x: "Positive" if x > 0.05 else ("Negative" if x < -0.05 else "Neutral")
        )

        # Show tweets with sentiment
        st.subheader("📰 Latest Tweet Sentiments")
        st.dataframe(tweet_data.head(20))

        # Sentiment distribution
        sentiment_counts = tweet_data["Sentiment"].value_counts().reset_index()
        sentiment_counts.columns = ["Sentiment", "Count"]

        # Pie chart
        fig_pie = px.pie(
            sentiment_counts,
            names="Sentiment",
            values="Count",
            title="Sentiment Distribution"
        )
        st.plotly_chart(fig_pie)

        # Average sentiment
        avg_score = tweet_data["Sentiment Score"].mean()
        st.subheader("📊 Sentiment Summary")
        if avg_score > 0.05:
            st.success(f"Overall Sentiment: Positive 😊 (Avg Score: {avg_score:.2f})")
        elif avg_score < -0.05:
            st.error(f"Overall Sentiment: Negative 😞 (Avg Score: {avg_score:.2f})")
        else:
            st.info(f"Overall Sentiment: Neutral 😐 (Avg Score: {avg_score:.2f})")
    else:
        st.warning("⚠️ No tweets found or snscrape error.")
