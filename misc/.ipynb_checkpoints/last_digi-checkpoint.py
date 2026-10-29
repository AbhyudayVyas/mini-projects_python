n = 942
# while True:
#     digits = len(str(n))
#     copy = n
#     sum = 0
#     for _ in range(digits):
#         sum+=copy%10
#         copy//=10
#     copy = sum
#     print(sum)
#     if len(str(sum))<=1:
#         break

digits = [int(d) for d in str(abs(n))]
print(digits)
copy = 0
while True:
    for digit in digits:
        copy+=digit
        print(copy)
    digits = [int(d) for d in str(abs(copy))]
    print(digits)
    if len(digits)<=1:
        break
    copy = 0
print(copy)