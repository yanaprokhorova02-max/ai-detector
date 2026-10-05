# cliche_detector.py
import re

AI_PHRASES = [
    "as an ai language model", "as a large language model", "i hope this helps",
    "sure, here is", "here is", "of course!", "certainly!", "you're absolutely right!",
    "would you like", "is there anything else", "let me know", "more detailed breakdown",
    "up to my last training update", "as of my last knowledge update",
    "i cannot offer medical advice", "i'm sorry", "in this essay, i will",
    "this essay will discuss", "delve", "tapestry", "underscore", "pivotal",
    "robust", "leverage", "intricate", "nuanced", "foster", "facilitate",
    "realm", "landscape", "testament", "navigate", "embark", "myriad",
    "plethora", "multifaceted", "holistic", "synergy", "paradigm", "moreover",
    "furthermore", "additionally", "consequently", "thus", "hence", "notably",
    "importantly", "ultimately", "in conclusion", "in summary", "overall",
    "in today's fast-paced world", "in the realm of", "it is important to note that",
    "it is worth mentioning that", "when it comes to", "a testament to",
    "navigating the landscape", "it is not just", "not only", "the key to",
    "plays a crucial role in", "serves as a", "acts as a", "can be seen as",
    "stands as", "marks", "functions as", "operates as", "represents", "boasts",
    "features", "maintains", "offers", "refers to", "aligns with", "resonates with",
    "valuable insights", "boasts a", "vibrant", "rich", "profound", "enhancing",
    "showcasing", "exemplifies", "commitment to", "natural beauty", "nestled",
    "in the heart of", "groundbreaking", "renowned", "featuring", "diverse array",
    "in connection with", "connected with", "in association with", "associated with",
    "industry reports", "observers have cited", "experts argue", "some critics argue",
    "several sources", "several publications", "such as", "despite its",
    "despite these challenges", "challenges and legacy", "future outlook",
    "bolstered", "crucial", "deep dive", "emphasizing", "enduring", "enhance",
    "fostering", "garner", "highlight", "interplay", "intricacies", "key",
    "meticulous", "meticulously", "showcase", "valuable", "it's important",
    "it's crucial", "it's essential", "it's vital to note that", "it's worth noting",
    "it's mentioning", "it's highlighting that", "please note that", "notably",
    "it's clear", "it's evident", "it's apparent that", "needless to say",
    "suffice it to say", "it goes without saying", "rest assured", "allow me to",
    "without further ado", "let's delve", "let's dive into", "let's delve into",
    "embark on", "explore the intricacies", "explore the nuances",
    "explore the complexities", "in today's digital world", "in today's modern world",
    "in today's ever-changing world", "in the modern era", "in the current era",
    "in the digital era", "the fact of the matter is that", "revolutionary",
    "cutting-edge", "state-of-the-art", "game-changer", "paradigm shift",
    "seamlessly", "innovative solution", "pivotal role", "actionable insights",
    "key takeaways", "to summarize", "to wrap up", "all in all", "to sum up",
    "first and foremost", "last but not least", "at the end of the day",
    "in addition", "as a result", "therefore", "accordingly", "subsequently",
    "nevertheless", "nonetheless", "in contrast", "on the other hand",
    "it is worth noting", "it should be noted", "it is important to",
    "it is essential to", "it's vital to note that"
]

def check_text_for_ai(text):
    text_lower = text.lower()
    found_phrases = []
    
    for phrase in AI_PHRASES:
        pattern = r'\b' + re.escape(phrase) + r'\b'
        if re.search(pattern, text_lower):
            found_phrases.append(phrase)
            
    punctuation_issues = []
    
    if text.count('—') > 2:
        punctuation_issues.append("Частое использование длинного тире (—)")
        
    if re.search(r'\s—\s', text):
        punctuation_issues.append("Пробелы вокруг тире ( — )")
        
    if text.count(';') > 1:
        punctuation_issues.append("Злоупотребление точками с запятой (;)")
        
    if len(re.findall(r':\s*$', text, re.MULTILINE)) > 2:
        punctuation_issues.append("Частые двоеточия перед списками")

    total_found = len(found_phrases) + len(punctuation_issues)
    
    # Формируем результат в виде HTML-строки для списка
    if total_found == 0:
        result_html = "Признаков ИИ-текста не обнаружено. Текст выглядит естественным."
        ai_prob = 0.0
    else:
        result_html = "<b>Обнаружены признаки ИИ:</b><br>"
        if found_phrases:
            display_phrases = found_phrases[:10]
            result_html += f"<b>Характерные слова и фразы ({len(found_phrases)}):</b><br>"
            result_html += ", ".join([f"«{p}»" for p in display_phrases])
            if len(found_phrases) > 10:
                result_html += f" и еще {len(found_phrases) - 10}..."
            result_html += "<br><br>"
        if punctuation_issues:
            result_html += "<b>Особенности пунктуации:</b><br>"
            result_html += "<br>".join([f"• {issue}" for issue in punctuation_issues])
        
        # Считаем примерный процент (зависит от количества найденных совпадений)
        # Формула условная: 5% за каждое найденное клише, максимум 99.9%
        ai_prob = min(99.9, total_found * 5.0)
	
    human_prob = round(100 - ai_prob, 2)
    
    if ai_prob > 50:
        verdict = "AI"
    else:
        verdict = "Человек"

    return {
        "ai_prob": round(ai_prob, 2),
        "human_prob": human_prob,
        "verdict": verdict,
        "result": result_html
    }

if __name__ == "__main__":
    test_text = "In this essay, I will delve into the tapestry."
    print(check_text_for_ai(test_text))