import streamlit as st
from transformers import pipeline

# סימולציה: מודול רגשי (sentiment analysis) מדמה קריאה למודל רגשי אמיתי
def emotional_analysis(text):
    classifier = pipeline("sentiment-analysis")
    result = classifier(text)[0]
    return f"רגש: {result['label']}, ביטחון: {result['score']:.2f}"

# סימולציה: קריאה למודל קוונטי (כאן רק הדמיה)
def quantum_simulation(text):
    # בדמו פשוט מחזיר ערך מדומה לפי אורך הטקסט
    score = len(text) % 3
    quantum_states = ["|0>", "|1>", "|+>"]
    return f"מצב קוונטי סימולטיבי: {quantum_states[score]}"

st.title("דמו QNSL - SNLP + SCPU")

user_input = st.text_area("כתוב טקסט לעיבוד:")

if st.button("הפעל דמו"):
    if user_input.strip():
        st.markdown("### תוצאות ניתוח רגשי:")
        st.write(emotional_analysis(user_input))

        st.markdown("### סימולציה של מודל קוונטי:")
        st.write(quantum_simulation(user_input))
    else:
        st.warning("נא להזין טקסט לעיבוד.")
