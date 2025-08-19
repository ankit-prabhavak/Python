import numpy as np

x = np.array([[10, 15, 20],
              [21, 22, 23],
              [55, 56, 57]])

y = np.array([[15, 61, 23,],
              [45, 65, 15],
              [63, 55, 63]])

print(x*y)
print(x+y)


print(np.sort(y,1))


x.concatenate(y)

ll = np.array([78,94,51,65,18,49])

anny = np.where(ll > 50)
print(anny)

granny = np.array_split(ll, 3)

guy = np.intersect1d(x, y)
print(guy)


