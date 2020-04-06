from typing import List

from test_framework import generic_test, test_utils


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    anagrams = {}
    for i in dictionary:
        anagram = "".join(sorted(i))
        if anagrams.get(anagram):
            anagrams[anagram].append(i)
        elif not anagrams.get(anagram):
            anagrams[anagram] = [i]
    ans = []
    for i in anagrams.keys():
        if len(anagrams[i]) > 1:
            ans.append(anagrams[i])

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
