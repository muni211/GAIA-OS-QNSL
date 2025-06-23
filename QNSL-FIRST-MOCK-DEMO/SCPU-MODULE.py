import json
import os

# סימולציית זיכרון למידה מתמשכת – קובץ JSON
MEMORY_FILE = "scpu_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "requests": [],
        "keywords": [],
        "code_patterns": []
    }

def save_memory(memory_data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory_data, f, ensure_ascii=False, indent=2)

def process_data(nlp_data):
    print(f"⟶ [SCPU] עיבוד רגשי־שפתי ולמידה מתמשכת...")

    # טען זיכרון קודם
    memory = load_memory()

    # עדכון מידע מהקלט הנוכחי
    new_keywords = extract_keywords(nlp_data["text"])
    memory["requests"].append(nlp_data["text"])
    memory["keywords"].extend(new_keywords)
    memory["keywords"] = list(set(memory["keywords"]))  # הסרה כפילויות

    # שמור זיכרון
    save_memory(memory)

    print(f"  🧠 מילים חדשות שנלמדו: {new_keywords}")
    print(f"  📁 זיכרון כולל: {len(memory['requests'])} בקשות")

    return {
        "nlp": nlp_data,
        "memory": memory
    }

def extract_keywords(text):
    # דמו של חילוץ מילות מפתח מהמשפט
    common_terms = ["ai", "quantum", "language", "code", "data", "model"]
    return [term for term in common_terms if term in text.lower()]
