import sys

#Time Complexity: O(N) where N is the number of characters in the file
def tokenize(text_file_path):
    tokens = []
    try:
        file = open(text_file_path, encoding ='utf-8')
        for line in file:
            token = ""
            for char in line:
                if char.isalnum():
                    token = token + char.lower()
                elif token:
                    tokens.append(token)
                    token = ""
            if token:
                tokens.append(token)
                token = ""
        file.close()
    except FileNotFoundError:
        print("File not found")
    except Exception as error:
        print(error)
    return tokens

#Time Complexity: O(M) where M is the number of tokens.
def compute_word_frequency(tokens):
    freq_map = {}
    for token in tokens:
        if token in freq_map:
            freq_map[token] += 1
        else:
            freq_map[token] = 1
    return freq_map

#Time Complexity: O(Klog(K)) where K is the number of unique tokens
def print_freq(frequency_map):
    sorted_frequency_map = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)
    for item, frequency in sorted_frequency_map:
        print(item + " -> " + str(frequency))

#Time Complexity: O(N) dominated by the tokenize function
def main():
    filepath = sys.argv[1]
    tokens = tokenize(filepath)
    freq_map = compute_word_frequency(tokens)
    print("Tokenized output\n")
    print(tokens)
    print("\nFrequency output\n")
    print_freq(freq_map)

if __name__ == "__main__":
    main()


