def number_to_words(number):
    # Define lists of words for number components
    ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens = ['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    thousands = ['', 'Thousand', 'Million']
    
    def convert_chunk(chunk):
        if chunk == 0:
            return ""
        elif chunk < 10:
            return ones[chunk] + " "
        elif chunk < 20:
            return teens[chunk - 10] + " "
        else:
            return tens[chunk // 10] + " " + ones[chunk % 10] + " "
    
    if number == 0:
        return ones[0]
    
    num_str = str(number)
    chunks = []
    while num_str:
        chunks.insert(0, int(num_str[-3:]))
        num_str = num_str[:-3]
    
    words = ""
    for i, chunk in enumerate(chunks):
        if chunk != 0:
            words += convert_chunk(chunk) + thousands[len(chunks) - i - 1] + " "
    
    return words.strip()

def main():
    number = int(input("Enter a number (up to 999,999): "))
    if number < 0 or number > 999999:
        print("Number out of range.")
    else:
        words = number_to_words(number)
        print(f"{number}: {words}")

if __name__ == "__main__":
    main()
