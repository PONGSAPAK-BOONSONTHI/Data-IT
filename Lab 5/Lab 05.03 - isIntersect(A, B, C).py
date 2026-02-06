"""Lab 05.03 - isIntersect(A, B, C)"""
import json
a = set(json.loads(input()))
b = set(json.loads(input()))
c = set(json.loads(input()))
print(True if a&b&c else False)