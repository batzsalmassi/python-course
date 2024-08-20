# צרו תוכנית שבה שני list
# צרו מיפוי כך ש:
# dict{list1:list2}
# אם len(list1)>len(list2)
#   הכניסו list1:none

list1 = ['1', '2', '3', '4', '5', '6', '7']
list2 = ['a', 'b', 'c', 'd', 'e']
dict = {}
for k in range (len(list1)):
    if k < len(list2):
        dict[list1[k]] = list2[k]
    else:
        dict[list1[k]] = None
print(dict)