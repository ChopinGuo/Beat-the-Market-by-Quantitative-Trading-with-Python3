# 1. String Type

price_str = '30.14, 29.58, 26.36, 32.56, 32.82'
print('Old price_str id = {}'.format(id(price_str)))

price_str = price_str.replace(' ', '')
print('New price_str id = {}'.format(id(price_str)))

print(price_str)

# 2. Content

# split splits the string acoording to ',',  and returns a number array
# price_array
print(type(price_str))
price_array = price_str.split(',')
print(price_array)
print(type(price_array))
print(price_array[0])
print(type(price_array[0]))
print(type(float(price_array[0])))

price_array.append('32.82')
print(price_array)

# set is an unordered content
price_set = set(price_array)
print(price_set)

price_array.remove('32.82')
print(price_array)

# 3. Loop
