from is_it_slop import is_this_slop

def check_text_for_ai(text: str) -> dict:
    if len(text.strip()) < 50:
        return {
            "error": "Текст слишком короткий. Введите не менее 50 символов.",
            "ai_probability": None,
            "human_probability": None,
            "classification": "Unknown"
        }

    result = is_this_slop(text)

    return {
        "error": None,
        "ai_probability": round(result.ai_probability * 100, 2),
        "human_probability": round(result.human_probability * 100, 2),
        "classification": result.classification
    }