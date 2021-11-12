'''import pdb
pdb.set_trace()

def is_pal(S):
    if len(S) == 1:
        return True
    if S[0] == S[-1]:
        return is_pal(S[1 : -1])
    else:
        return False

print(is_pal("wow"))
s='gadag'
print(s[1:3])



def reverse(L):
  if len(L)==1:
    return L
  M=[]
  if len(L)>=0:
    M=L[-1]
    return [M] + reverse(L[:-1])

print(reverse([10,5,1,4,9]))

def linear(P,Q,k):
  if len(P)!=len(Q):
    return False
  return P==k*Q

print(linear([10,20,30],[1,2,3],10))

P=[10,20,30]
Q=[1,2,3]
k=10
print(P)
print(P[0]==k*Q[0])

def do_something(filename):
    f = open(filename, 'r')
    maxword = f.readline().strip()
    count = 1
    # we are now at the beginning of the second line
    for line in f:
        word = line.strip()
        if len(word) > len(maxword):
            maxword = word
            count = 1
        elif len(word) == len(maxword):
            count += 1

    f.close()
    return count

print(do_something('words.txt'))
'''
f = open('pattern.txt', 'w')
letters = 'abcdefghijklmnopqrstuvwxyz'
n = len(letters) // 2
for i in range(n):
    line = letters[i] + letters[-1 - i]
    if i != n - 1:
        line = line + '\n'
    f.write(line)
f.close()