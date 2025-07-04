scores = [150, 12, 123, 231, 42, 24, 543, 654 ,12, 543 ,645, 63 ,234 , 543, 432 , 934, 432, 123]

#Method1:

value = scores[0]

for i in range(len(scores)-1):
    if scores[i] > value:
        value = scores[i]

print(value)


#Method2:
max_value = 0

for score in scores:
    if score > max_value:
        max_value = score

print(max_value)