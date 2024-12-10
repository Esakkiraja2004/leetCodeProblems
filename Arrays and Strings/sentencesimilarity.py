def areSentencesSimilar(sentence1, sentence2):
        # Split the sentences into words
        words1 = sentence1.split()
        words2 = sentence2.split()

        print(words1)
        print(words2)

        # Ensure words1 is the longer sentence
        if len(words1) < len(words2):
            words1, words2 = words2, words1
        
        start, end = 0, 0
        n1, n2 = len(words1), len(words2)
        
        # Compare from the start
        while start < n2 and words1[start] == words2[start]:
            start += 1
        
        # Compare from the end
        while end < n2 and words1[n1 - end - 1] == words2[n2 - end - 1]:
            end += 1
        
        # Check if the remaining unmatched part is in the middle
        return start + end >= n2
a = "is raja"
b = "my name is raja"
print(areSentencesSimilar(a,b))