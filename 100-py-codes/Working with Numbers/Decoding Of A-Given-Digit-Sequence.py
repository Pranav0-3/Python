## Python Code to Count Possible Decoding Of A Given Digit Sequence.

## *************** ERROR IN CODE:( ********************


# def count_digits(dig, a):
#     cnt = [0] * (a+1)
#     cnt[0], cnt[1] = 1,1

#     for k in range(2, a+1):
#         cnt[k] = 0
#         cnt[k] = cnt[k-1]

#         if dig[k-1] == "1" or (dig[k-2] == "2" and dig[k-1] <= "6"):
#             cnt[k] += cnt[k-2]
#     return cnt[a]

# dig = input("Enter a number: ")
# print("The possible count of decoding of the seq is", count_digits(dig, len(dig)))