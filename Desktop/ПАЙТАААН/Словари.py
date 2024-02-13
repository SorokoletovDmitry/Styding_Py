synonyms = {
    "happy": "joyful",
    "smart": "intelligent",
    "big": "large",
    "fast": "quick"
}
last_word = list(synonyms.keys())[-1]
if last_word in synonyms:
    synonym = synonyms[last_word]
    print(f"Синоним для слова {last_word} - {synonym}")
else:
    print(f"Для слова {last_word} нет синонима в данном словаре.")
