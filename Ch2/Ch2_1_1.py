i = 1
typ_i = type(i)
print(typ_i)

b = (1 > 2)
print(b)
typ_b = type(b)
print(typ_b)

price_str = '30.14, 29.58, 26.36, 32.56, 32.84'
print(price_str)
typ_pri = type(price_str)
print(typ_pri)

if not isinstance(price_str, str):
    # not denotes logic 'not'. If it is not str type,  tansfer it
    # into a string
    price_str = str(price_str)
# if isinstance(price_str, int) and price_str > 0:
    # and represents logic 'and'. If it is int type and positive
    price_str += 1
# elif isinstance(price_str, float) or price_str < 0:
    # or represents logic 'or'. If it is float type and negative
    price_str += 1.0
else:
    raise TypeError('price_str is str type!')

# Ch2_1_2

print('Old price_str id = {}'.format(id(price_str)))
