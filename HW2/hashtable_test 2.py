# Here are a set of very simple tests. Please make sure your code passes the provided tests -- this serves as a check that our grading script will work.
# You are encouraged to add additional tests of your own, but you do not need to submit this file.
import random

from hashtable_chaining import HashTable as HashTableChaining
from hashtable_linear_probing import HashTable as HashTableProbing

N = 10000
random.seed(-123)
for (name, HashTable) in [("chaining", HashTableChaining)]:
    table = HashTable()
    print("--------------- INSERT & RESIZE-----------------")
    for _ in range(N):
        k = int(random.random() * N * 100) % N
        table.insert("example_key" + str(k), "example_value" + str(k))
        print(table.size(), table.array_size)
        
    for i in range(N):
        print(table.get("example_key" + str(i)))

    print("------------------ REMOVE ----------------------")
    for _ in range(N):
        k = int(random.random() * N * 100) % N
        table.remove("example_key" + str(k))
        
    for i in range(N):
        print(table.get("example_key" + str(i)))


