scores = [
    ('Jane', 'B', 12),
    ('John', 'A', 15),
    ('Dave', 'B', 11)]

# 依照第三個數字元素排序
print(sorted(scores, key = lambda s: s[-1]))