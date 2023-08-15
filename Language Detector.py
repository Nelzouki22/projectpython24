from langdetect import detect

def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "Unknown"

if __name__ == "__main__":
    text = input("Enter a text for language detection: ")
    language = detect_language(text)
    print(f"The detected language is: {language}")
