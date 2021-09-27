#pow-wow summary: we shared code and discussed how to combine/improve the code. we figured out together how to call items in a dictionary.
#Discoveries: how to call a particular item in a dictionary; defining functions; using random; combining code from different trios
#Questions: was it intentional that we should use single quotes instead of double quotes (and if so, why)? was there a way to do this without importing random?
#Comments: helped me get familiar with Python again
import random

students={
'list1': ['Alejandro Alonso', 'Aryaman Goenka', 'Angela Zhang', 'Christopher Liu', 'Deven Maheshwari',
       'Emma Buller', 'Ella Krechmer', 'Gavin McGinley', 'Haotian Gan', 'Ivan Lam', 'Ishraq Mahid',
       'Ivan Mijacika', 'Julia Nelson', 'Lucas Lee', 'Lucas Tom Wong', 'Michelle Lo', 'Oscar Wang',
       'Owen Yaggy', 'Renggeng Zheng', 'Shriya Anand', 'Shyne Choi','Sadid Ethun', 'Tomas Acuna','Theo Fahey',
       'Tina Nguyen', 'Tami Takada', 'William Chen', 'Yusuf Elsharawy', 'Zhaoyu Lin'],
'list2': ['Alif Abdullah', 'Andrew Juang', 'Andy Lin', 'Austin Ngan', 'Annabel Zhang', 'Daniel Sooknanan',
       'Eric Guo', 'Eliza Knapp', 'Hebe Huang', 'Han Zhang', 'Yoonah Chang', 'Josephine Lee', 'Jonathan Wu',
       'Jesse Xie', 'Justin Zou', 'Kevin Cao', 'Liesel Wong', 'Michael Borczuk', 'Mark Zhu', 'Noakai Aronesty',
       'Patrick Ging','Qina Liu', 'Rachel Xiao', 'Raymond Yeung', 'Sophie Liu', 'Shadman Rakib','Thomas Yu',
       'Wenhao Dong', 'Yaying Liang Li', 'Yuqing Wu'],
}

def printName():
    print('period 1: ' + students['list1'][random.randint(0, len(students['list1']) - 1)])
    print('period 2: ' + students['list2'][random.randint(0, len(students['list2']) - 1)])
printName()
