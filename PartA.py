import sys

#Time Complexity: O(M * C) where M is the number of lines
#C is the number of characters in the line
def tokenize(text_file_path):
    tokens = []
    try:
        file = open(text_file_path, encoding ='utf-8')
        #this for loop is O(M) where m is the number of lines in the file
        for line in file:
            token = ""
            #this for loop is O(C) where c is the number of characters in the line
            for char in line:
                if char.isalnum():
                    token = token + char.lower()
                elif token:
                    tokens.append(token)
                    token = ""
            #handles last token in line
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
#this function goes through each token in the token list once
def compute_word_frequency(tokens):
    freq_map = {}
    for token in tokens:
        if token in freq_map:
            freq_map[token] += 1
        else:
            freq_map[token] = 1
    return freq_map

#Time Complexity: O(Klog(K)) where K is the number of tokens in the map
#This is determined by the sorted method of O(Klog(K)) that dominates
#over the O(K) for printing
def print_freq(frequency_map):
    sorted_frequency_map = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)
    for item, frequency in sorted_frequency_map:
        print(item + " -> " + str(frequency))

#Time Complexity: O(Klog(K)) dominated by the print_freq function which is O(Klog(K))
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


