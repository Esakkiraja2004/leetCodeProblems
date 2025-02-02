queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
pattern = "FoBaT"

res = []

for query in queries:
    query_index = 0
    pattern_index = 0
    match = True
    
    # Iterate over pattern and query
    while pattern_index < len(pattern) and query_index < len(query):
        if pattern[pattern_index] == query[query_index]:
            pattern_index += 1
        elif query[query_index].isupper():
            match = False
            break
        query_index += 1
    
    # If pattern is not fully matched or there are unmatched uppercase letters
    if pattern_index != len(pattern):
        match = False
    
    # Check if we found a match for this query
    res.append(match)

print(res)  # Output: [False, True, False, False, False]
