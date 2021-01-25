def func(a,results=None):
    if results is None:
        results = []
    results.append(a)
    return results

print(func(1))
print(func(2))