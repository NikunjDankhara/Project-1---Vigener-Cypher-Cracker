from math import gcd
import string
import numpy as numpy

def shift(l1, n1):  # for left shift operation
    return l1[n1:] + l1[:n1]

num = dict(zip(range(0, 26), string.ascii_lowercase))  # for reverse mapping: numbers to letters

A = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025,
     0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.0236, 0.0015,
     0.01974, 0.00074]

a = input('Enter your cipher text here:').lower()
a = list(a)
a1 = a
c = 0
d = []
num_coincidences = 1

while num_coincidences <= 20:  # gives result of first k number of coincidences
    a1 = numpy.roll(a1, 1)  # shift the list right
    for i, j in zip(a, a1):  # zip(a,b) makes [(a0,b0),(a1,b1)] for all the element of a and b
        if i == j:  # for loop compares and increments c if the same element is found in a1 and a2
            c += 1  # c is a reference variable that contains the number of same elements
    print('Number of coincidences for', num_coincidences, 'shift is:', c)
    d.append(c)
    num_coincidences += 1
    c = 0

max_coincidence = max(d)  # for the highest number in the list
print('Maximum number of coincidence (L):', max_coincidence)
max_coincidence = d.index(max_coincidence)
max_coincidence += 1

sec_max_coincedence = sorted(set(d))[-2]  # for the second highest number in the list
print('Second highest number of coincidence (sec_max_coincedence):', sec_max_coincedence)
sec_max_coincedence = d.index(sec_max_coincedence)
sec_max_coincedence += 1

third_max_coincedence = sorted(set(d))[-3]  # for the third highest number in the list
print('Third highest number of coincidence (third_max_coincedence):', third_max_coincedence)
third_max_coincedence = d.index(third_max_coincedence)
third_max_coincedence += 1

forth_max_coincedence = sorted(set(d))[-4]  # for the fourth highest number in the list
print('Fourth highest number of coincidence (forth_max_coincedence):', forth_max_coincedence)
forth_max_coincedence = d.index(forth_max_coincedence)
forth_max_coincedence += 1

fifth_max_coincedence = sorted(set(d))[-5]  # for the fifth highest number in the list
print('Fifth highest number of coincidence (fifth_max_coincedence):', fifth_max_coincedence)
fifth_max_coincedence = d.index(fifth_max_coincedence)
fifth_max_coincedence += 1

sixth_max_conincedence = sorted(set(d))[-6]  # for the sixth highest number in the list
print('Sixth highest number of coincidence (sixth_max_conincedence):', sixth_max_conincedence)
sixth_max_conincedence = d.index(sixth_max_conincedence)
sixth_max_conincedence += 1

lth = [max_coincidence, sec_max_coincedence, third_max_coincedence, forth_max_coincedence, fifth_max_coincedence, sixth_max_conincedence]
print('\nPossible key lengths are:', max_coincidence, ',', sec_max_coincedence, ',', third_max_coincedence, ',', forth_max_coincedence, ',', fifth_max_coincedence, ',', sixth_max_conincedence)

d1 = gcd(max_coincidence, sec_max_coincedence)
d1 = gcd(d1, third_max_coincedence)
d1 = gcd(d1, forth_max_coincedence)
d1 = gcd(d1, fifth_max_coincedence)
d1 = gcd(d1, sixth_max_conincedence)
print('GCD of all above shifts:', d1)  # GCD of all elements of d

in1 = 0
while in1 <= 2:
    max_coincidence = lth[in1]
    print('\nTake', max_coincidence, 'as key length')

    # Dividing in L (max d) parts
    z = [[] for x1 in range(0, max_coincidence)]
    v1 = 0
    while v1 < max_coincidence:
        for i2 in range(v1, len(a), max_coincidence):
            z[v1].append(a[i2])
        v1 += 1

    # Cracking Caesar cipher
    v1 = 0
    Array = []
    while v1 < max_coincidence:
        W = []
        for charc in string.ascii_lowercase:
            b1 = z[v1].count(charc)
            b1 = b1 / 26
            b1 = round(b1, 7)
            W.append(b1)

        I = 24
        J = []
        t = 0
        while I >= 0:
            B = shift(A, t)
            K = numpy.dot(W, B)
            K = round(K, 6)
            J.append(K)
            I -= 1
            t += 1

        Max1 = max(J)  # for the highest number in the list
        F = [D for D, E in enumerate(J) if E == Max1]  # retrieve the index of the maximum number
        F[0] = ((26 - F[0]) % 26)
        key = num[F[0]].upper()
        Array.append(key)

        dec_num = []
        for character in z[v1]:  # loop for getting deciphered numbers
            number = ord(character) - 97
            number = ((number - F[0]) % 26)
            dec_num.append(number)

        num_to_alph = []
        for id2 in dec_num:  # loop for number to alphabet mapping
            num_to_alph.append(num[id2])

        z[v1] = num_to_alph
        v1 += 1

    print('The Encryption Key:', ''.join(Array))

    # Recovering the coincedence parts into deciphered form
    v1 = 0
    var = 0
    D1 = []
    vv = int(len(a) / max_coincidence)

    while var < vv:
        while v1 < max_coincidence:
            D1.append(z[v1][var])
            v1 += 1

        var += 1
        v1 = 0

    v1 = 0
    while v1 < (len(a) % max_coincidence):
        D1.append(z[v1][var])
        v1 += 1

    print('\nfinal plain Text:')
    print(''.join(str(elm) for elm in D1))

    in1 += 1
