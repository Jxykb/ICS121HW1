import sys
from PartA import tokenize

#Time Complexity: O(N) where N is the number of characters in the largest text file.
# dominated by the tokenize function
def intersection(file1, file2):
    tokens1 = set(tokenize(file1))
    tokens2 = set(tokenize(file2))
    file_intersection = tokens1.intersection(tokens2)
    common_tokens = len(file_intersection)
    common_map = {'common_token_count': common_tokens, 'common_tokens': file_intersection}
    return common_map

def main():
    filepath1 = sys.argv[1]
    filepath2 = sys.argv[2]

    result = intersection(filepath1, filepath2)
    print("Common tokens: \n" + str(result['common_tokens']))
    print("Common tokens count:")
    print(result['common_token_count'])


if __name__ == "__main__":
    main()
