from snlp_module import process_text
from scpu_module import process_data
from slo_module import orchestrate_code

def main():
    user_input = input("הכנס טקסט שמתאר את הבקשה שלך: ")

    print("\n🔍 שלב 1: עיבוד שפה טבעית (S-NLP)")
    nlp_result = process_text(user_input)

    print("\n🧠 שלב 2: עיבוד נתונים (S-CPU)")
    processed_data = process_data(nlp_result)

    print("\n🧩 שלב 3: תזמור קוד (SLO)")
    code_result = orchestrate_code(processed_data)

    print("\n✅ תוצאה סופית:\n")
    print(code_result)

if __name__ == "__main__":
    main()
