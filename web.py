import streamlit as st
from translation import translate


title = st.text_input('English Text', 'Enter your english text here')

langugage = st.selectbox(
    'What language do you want to translate to?',
    ('Yoruba', 'Igbo', 'Hausa'))

dict_lang = { "Yoruba": "yo",
                "Igbo": "ig",
                "Hausa": "ha"}

translation = translate(dict_lang[langugage], title)
st.write(f'Your translation from English to {langugage} is: ', translation)
