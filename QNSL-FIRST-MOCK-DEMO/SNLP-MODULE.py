def process_text(user_input):
    print(f"⟶ קלט שהתקבל: {user_input}")
    # דמו בלבד – אין עיבוד NLP אמיתי
    return {
        "intent": "generate_code",
        "emotion": "motivated",
        "language": "hebrew",
        "text": user_input
    }
