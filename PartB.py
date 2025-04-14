import sys
from PartA import tokenize

#Time Complexity: O(max(M1 * C1,M2 * C2)) where M is the number of lines in the file and c is the number of characters per line
#1 and 2 are for file1 and file2 respectively
#Dominated by the tokenize function called on each file
def intersection(file1, file2):
    #insert and lookup for set is done in constant time
    tokens1 = set(tokenize(file1))
    tokens2 = set(tokenize(file2))
    #intersection will take O(len(tokens1) + len(tokens2)))
    file_intersection = tokens1.intersection(tokens2)
    common_tokens = len(file_intersection)
    common_map = {'common_token_count': common_tokens, 'common_tokens': file_intersection}
    return common_map

#Time Complexity: O(intersection) = O(max(M1 * C1,M2 * C2)) which is the time complexity of the intersection function
#which is the dominating factor in this program
def main():
    filepath1 = sys.argv[1]
    filepath2 = sys.argv[2]

    result = intersection(filepath1, filepath2)
    print("Common tokens: \n" + str(result['common_tokens']))
    print("Common tokens count:")
    print(result['common_token_count'])


if __name__ == "__main__":
    main()
