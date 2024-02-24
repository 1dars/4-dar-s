# 1  misol
# def calc(katta):
#     a = {}
#     for x in katta:
#         a[x] = x.upper()
#     return a
# print(calc(["k", "o", "e", "z","v","m","s","d"]))
# 3 misol
# def odam(lst):
#     resault = 0
#     for x in lst:
#         resault += x["pul"]
#     return resault
# print(odam([
#   { "ismi": "John", "yosh": 21, "pul": 23000 },
#   { "ismi": "Steve",  "yosh": 32, "pul": 40000 },
#   { "ismi": "Martin",  "yosh": 16, "pul": 2700 }
# ]))
# 4 misol

# def bsb(lst):
#     rezalt = 0
#     for x in lst:
#         rezalt += x.get("score")
#     return rezalt
#
# print(bsb([
#   {"tile": "N", "score": 21},
#   {"tile": "K", "score": 15},
#   {"tile": "Z", "score": 10},
#   {"tile": "X", "score": 7},
#   {"tile": "D", "score": 2},
#   {"tile": "A", "score": 11},
#   {"tile": "E", "score": 1}
# ]))
# 6 misol

# def calc(latta):
#     a = {}
#     for harf in latta:
#         a[harf] = harf.upper()
#     return a
# print(calc(["b", "v", "e", "z"]))
# 7 misol
def ismi(lst):
    a = []
    for x in lst:
        a.append(lst[x])
    return sorted(a)

print(ismi({
  "oquvchi 1": "Steve",
  "oquvchi 2": "Becky",
  "oquvchi 3": "John"
}))