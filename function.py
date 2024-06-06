tom=[234,23,423,43,53]
ali=[234,234,5,322,11]


def cal_total(exp):
    total=0
    for item in exp :
          total=total+item
    return total
    
tom_total=cal_total(tom)
ali_total=cal_total(ali)
print("tom",tom_total)
print("ali",ali_total)