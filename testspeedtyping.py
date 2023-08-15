import random
import time

def speed_typing_test():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Programming is fun and rewarding.",
        "Practice makes perfect.",
        "Python is a versatile programming language.",
        "Learning to code opens up many opportunities."
    ]

    sentence = random.choice(sentences)
    print("Type the following sentence as fast as you can:")
    print(sentence)
    
    input("Press Enter to start...")
    start_time = time.time()
    
    typed_sentence = input("Type the sentence: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words = typed_sentence.split()
    correct_words = sum(1 for typed_word, original_word in zip(words, sentence.split()) if typed_word == original_word)
    
    accuracy = (correct_words / len(sentence.split())) * 100
    words_per_minute = (len(words) / elapsed_time) * 60
    
    print("\nTyping test result:")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Words per minute: {words_per_minute:.2f} WPM")

if __name__ == "__main__":
    speed_typing_test()
