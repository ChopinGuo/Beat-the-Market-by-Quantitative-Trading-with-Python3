# Ex1
# Add date afer the price
price_str = '30.14, 29.58, 26.36, 32.56, 32.82'
price_array = price_str.split(', ')

date_array = []
date_base = 20170118
# for here is used to count, useless variable is claimed by '-'
# acoording to the suggestion of Python
for _ in range(0, len(price_array)):
    date_array.append(str(date_base))
    # We only consider the sample case here, which means that the carry of
    # the date is not considered here.
    date_base += 1
print(date_array)

date_array = []
date_base = 20170118
prince_cnt = len(price_array)
while prince_cnt > 0:
    date_array.append(str(date_base))
    date_base += 1
    prince_cnt -= 1
print(date_array)
