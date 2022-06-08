import streamlit as st
import numpy as np
from components.bootstrap import card
from static.core_css import main_css
from PIL import Image
import os



def main():
    st.set_page_config(layout="wide")
    st.markdown("<h1 style='text-align: center; color:#2E2E2E ;'>Twiitter Sentiment Analysis</h1>", unsafe_allow_html=True)
    #WRITE THE CODE BELOW
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h1 style='text-align: center; color: #FD2B49;'>Dilma Rousseff</h1>", unsafe_allow_html=True)
        rel_path = '../static/dilma_tweetTotalbySentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Numbers of tweet written for Dilma by the types of sentiments', use_column_width='auto')
        
        rel_path = '../static/dilma_numberDailyTweet.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Daily numbers of tweet written for Dilma', use_column_width='auto')
        
        rel_path = '../static/dilma_avgTweetsbyUser.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average number of tweets by user', use_column_width='auto')
        
        rel_path = '../static/dilma_userTweetedMost.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Top 20 Users tweeted most for Dilma', use_column_width='auto')
        
        rel_path = '../static/dilma_likesForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total likes given to sentiments', use_column_width='auto')
        
        rel_path = '../static/dilma_replyForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total number of reply given to sentiments', use_column_width='auto')
        
        rel_path = '../static/dilma_retweetForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total number of retweet by sentiments', use_column_width='auto')
        
        rel_path = '../static/dilma_sentimentsOvertime.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average sentiments over the period', use_column_width='auto')
        
        rel_path = '../static/dilma_wordCloudNegativo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Word cloud of negative tweets for Dilma', use_column_width='auto')
        
        rel_path = '../static/dilma_wordCloudPositivo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Word cloud of positivo tweets for Dilma', use_column_width='auto')


    with col2:
        st.markdown("<h1 style='text-align: center; color: #279A55;'>Aécio Neves</h1>", unsafe_allow_html=True)
        rel_path = '../static/aecio_tweetTotalbySentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Numbers of tweet written for Aécio by the types of sentiments', use_column_width='auto')
        
        rel_path = '../static/aecio_numberDailyTweet.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Daily numbers of tweet written for Aécio', use_column_width='auto')
        
        rel_path = '../static/aecio_avgTweetsbyUser.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average number of tweets by user', use_column_width='auto')
        
        rel_path = '../static/aecio_userTweetedMost.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Top 20 Users tweeted most for Aécio', use_column_width='auto')
        
        rel_path = '../static/aecio_likesForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total likes given to sentiments', use_column_width='auto')
        
        rel_path = '../static/aecio_replyForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total number of reply given to sentiments', use_column_width='auto')
        
        rel_path = '../static/aecio_retweetForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total number of retweet by sentiments', use_column_width='auto')
        
        rel_path = '../static/aecio_sentimentsOvertime.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average sentiments over the period', use_column_width='auto')
        
        rel_path = '../static/aecio_wordCloudNegativo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Word cloud of negative tweets for Aécio', use_column_width='auto')
        
        rel_path = '../static/aecio_wordCloudPositivo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Word cloud of positivo tweets for Aécio', use_column_width='auto')

main()