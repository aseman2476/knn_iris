# ketabkhane ha v mazhol haye mored niaz

from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# vared kardan dataset

iris = datasets.load_iris()

# etela aat

observations = len(iris.data)
features = len(iris.feature_names)
print("tedad dade ha:" + str(observations))
print("tedad vizhegi ha: " + str(features))
print("")

print("vizhegi ha: ")
for i in iris.feature_names:
    print(i)
print("")

x = iris.data[0:, :2]
y = iris.target

# nemodari kardan dade ha
# c=y ranghaye motafavet

plt.figure()
plt.scatter(x[0:, 0], x[:, 1], c=y)
plt.xlabel("Sepal Length (cm)", fontsize=14)
plt.ylabel("Sepal Width (cm)", fontsize=14)
plt.title("nemodare parakandegie dadehaye iris (nesbat be tool v arze kasbarg)", fontsize=16)
plt.savefig("sepal-scatterplot.png")
plt.show()

# tolid markaz tasadofi

from random import randint

a = randint(0, 50)
b = randint(50, 100)
c = randint(100, 150)
m_a = x[a]
m_b = x[b]
m_c = x[c]

length_s = []
for i in enumerate(x):
    length.append(i[1][0])

width_s = []
for j in enumerate(x):
    width.append(j[1][1])

length_p = []
for i in enumerate(x):
    length.append(i[1][2])

width_p = []
for j in enumerate(x):
    width.append(j[1][3])

point = []
point.append(np.random.uniform(min(length), max(length)))
point.append(np.random.uniform(min(width), max(width)))
print("moratab sazi bar asas noghte ye tasadofi: ")
print("noghte tasadofi: " + str(point))
print("tedad hamsayegane nazdik (k): 10")

# mohasebe fasele noghat  az noghte tasadofi
# count = 0
#	d = np.sqrt((n[0] - point[0]) ** 2 + (n[1] - point[1]) ** 2)
#	distance.append([d, y[count]])
#	count += 1

s = 0
ve = 0
vi = 0
# distance.sort()
distance = []
for n in x:
    d1 = np.sqrt((n[0]) - m_a[0]) ** 2 + (n[1] - m_a[1]) ** 2 + (n[2] - m_[2]) ** 2 + (n[3] - m - [3] ** 2)
    d2 = np.sqrt((n[0]) - m_a[0]) ** 2 + (n[1] - m_a[1]) ** 2 + (n[2] - m_[2]) ** 2 + (n[3] - m - [3] ** 2)
    d3 = np.sqrt((n[0]) - m_a[0]) ** 2 + (n[1] - m_a[1]) ** 2 + (n[2] - m_[2]) ** 2 + (n[3] - m - [3] ** 2)

    if d1 > d2 and d2 > d3:
        print(str(n) + ("vizheghi haee shabih begoone seritosa darad"))
        s += 1


    elif d2 > d1 and d2 > d1:
        print(str(n) + ("vizheghi haee shabih begoone versicolor darad"))
        ve += 1

elif d3 > d2 and d3 > d1:
print(str(n) + ("vizheghi haee shabih begoone virginica darad"))
vi += 1

# find gone ghaleb

if s > vi and s > vi:
    print("seritosa goone ghalb ast")

elif ve > s and ve > vi:
    print("versicolor goone ghaleb ast")

elif vi > ve and vi > s:
    print("virginica goone ghaleb ast")

# top_ten = distance[0:10]

# target = []
# for i in top_ten:
#	target.append(i[1])

print("tedade goone seritosa: " + str(Counter(target)[0]))
print("tedade goone versicolor: " + str(Counter(target)[1]))
print("tedade goone virginica: " + str(Counter(target)[2]))

species = ""

if Counter(target)[0] > Counter(target)[1] and Counter(target)[0] > Counter(target)[2]:
    species = "Seritosa"
elif Counter(target)[1] > Counter(target)[0] and Counter(target)[1] > Counter(target)[2]:
    species = "Versicolor"
elif Counter(target)[2] > Counter(target)[0] and Counter(target)[2] > Counter(target)[1]:
    species = "Virginica"
else:
    species = "moteasefane goone ghaleb ra nayaftim :( "

print("goone ghaleb: " + str(species))
print("")

print('\t'"  \__/        \___/          ")
print('\t'"  /  \      //// \\\\        ")
print('\t'"  \__/         * *           ")
print('\t'"  /  \    @   \___/          ")
print('\t'"  \__/     \   _!_           ")
print('\t'"  /  \      \ /   \___       ")
print('\t'"  \__/       /     \  /      ")
print('\t'"  /  \      /       \/       ")
print('\t'"  \__/     / !     ! \       ")
print('\t'"  /  \     \_________/       ")
print('\t'"  \__/         !  !          ")
print('\t'"  /  \         ~  ~          ")

# adade delkhah

print("")
print("moratabsazi bar asas noghte delkhah: ")
print("")


def knn(user_length, user_width, user_k):
    iris = datasets.load_iris()
    x = iris.data[:, :2]
    y = iris.target

    distance = []
    count = 0

    for n in x:
        d = np.sqrt((n[0] - user_length) ** 2 + (n[1] - user_width) ** 2)
        distance.append([d, y[count]])
        count += 1

    distance.sort()
    top_k = distance[0:user_k]

    target = []
    for i in top_k:
        target.append(i[1])

    print("tedade goone seritosa: " + str(Counter(target)[0]))
    print("tedade goone versicolor: " + str(Counter(target)[1]))
    print("tedade goone virginica: " + str(Counter(target)[2]))

    species = ""

    if Counter(target)[0] > Counter(target)[1] and Counter(target)[0] > Counter(target)[2]:
        species = "Seritosa"
    elif Counter(target)[1] > Counter(target)[0] and Counter(target)[1] > Counter(target)[2]:
        species = "Versicolor"
    elif Counter(target)[2] > Counter(target)[0] and Counter(target)[2] > Counter(target)[1]:
        species = "Virginica"
    else:
        species = "moteasefane goone ghaleb ra nayaftim :( "

    print("goone ghaleb moratab sazi: " + str(species))


# karbar tool kasbarg va arze kasbarg va mizan nazdiki delkhah ra vared konad.

user_length_s = float(raw_input("yek tool kasbarg dar in baze vared konid(3.00 - 9.00 cm): "))
user_width_s = float(raw_input("yek arz kasbarg dar in baze vared konid (1.00 - 5.00 cm): "))
user_length_p = float(raw_input("yek tool golbarg dar in baze vared konid(3.00 - 9.00 cm): "))
user_width_p = float(raw_input("yek arz golbarg dar in baze vared konid (1.00 - 5.00 cm): "))

user_k = int(raw_input("yek adade sahih baray tedad nazdiktarin hamsaye ha (k) vared konid: "))
knn(user_length, user_width, user_k)

print('\t'"  \__/        \___/          ")
print('\t'"  /  \      //// \\\\        ")
print('\t'"  \__/         * *           ")
print('\t'"  /  \    @   \___/          ")
print('\t'"  \__/     \   _!_           ")
print('\t'"  /  \      \ /   \___       ")
print('\t'"  \__/       /     \  /      ")
print('\t'"  /  \      /       \/       ")
print('\t'"  \__/     / !     ! \       ")
print('\t'"  /  \     ~~~~~~~~~~~       ")
print('\t'"  \__/         !  !          ")
print('\t'"  /  \         ~  ~          ")
