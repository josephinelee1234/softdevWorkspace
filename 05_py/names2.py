#pow-wow summary: we shared code and discussed how to combine/improve the code.
#Discoveries: how to call a particular item in a dictionary; defining functions; using random; combining code from different trios
#Questions: was it intentional that we should use single quotes instead of double quotes (and if so, why)?
#Comments: helped me get familiar with Python again
import random

students={
'list1': ['Rayat', 'William', 'Michelle', 'Lucas', 'Ivan'],
'list2': ['Yoonah', 'Joshua', 'Alif', 'Josephine', 'Andrew'],
}

def printName():
    print("period 1: " + students['list1'][random.randint(0, len('list1') - 1)])
    print("period 2: " + students['list2'][random.randint(0, len('list2') - 1)])
printName()
