class Solution(object):
    def mostWordsFound(self, sentences):
        counter = 0
        for sentence in sentences:
            store = len(sentence.split())
            if store > counter:
                counter = store
        return counter
