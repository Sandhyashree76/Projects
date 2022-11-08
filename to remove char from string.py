#Character can be remove in 2 ways

# Replace()

Text="Susshine"
#remove the s from the string
print(Text.replace("s",""))

# Translate()

s = "posible"
x = "b"
y = "p"
table = s.maketrans(x, y)
print(s.translate(table))
