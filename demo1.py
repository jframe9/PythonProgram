import json
print("ss")

# ls = []

# ls = [ws for ws in range(100)]
#
# print(ls)
strs = '''
[{
    "name": "Tom",
    "gender": "male"
}, {
    "name": "Jack",
    "gender": "male"   
}]
'''
data = json.loads(strs)
print(type(data))