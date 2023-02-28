#file = open('user.txt', 'w')
#file.write('AaAaAaAa\n')
#file.close()

#file = open('user.txt', 'r')
#print(file.readlines())
#file.close()
import pickle

original = {"1": "2", "3": "4"}
pickled = pickle.dumps(original)
identical = pickle.loads(pickled)
print('Original', original)
print('Pickled', pickled)
print('Indentical', indentical)