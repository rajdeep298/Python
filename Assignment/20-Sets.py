def deduplicate_list_and_string(lst, str):
    lst = list(set(lst))
    str = " ".join(set(str))
    return lst, str


def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0


def cosine_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    return intersection / (len(set1) * len(set2) ** 0.5) if len(set1) * len(set2) != 0 else 0


lst = [1, 2, 2, 3, 4, 5, 5]
str = "Hello World"

lst, str = deduplicate_list_and_string(lst, str)
print("Deduplicated List:", lst)
print("Deduplicated String:", str)

# Calculate Jaccard and Cosine Similarity
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

print("Jaccard Similarity:", jaccard_similarity(set1, set2))
print("Cosine Similarity:", cosine_similarity(set1, set2))
