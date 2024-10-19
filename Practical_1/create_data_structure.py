"""
Створити структуру даних що відповідатиме наступним умовам:
Наступні функції повинні бути O(1):
    GetLastElement(); # Отримати останній елемент
    RemoveLastElement(); # Видалити останній елемент
    AddElement() # Додати новий елемент
    GetMin() # Отримати елемент з мінімальним значенням
"""


import sys
 
stack = []
min_element = sys.maxsize
 

# function for adding a new element
def addElement(x):
     
    global min_element, stack
    if (len(stack) == 0 or x < min_element):
        min_element = x
    pair = [x, min_element]
    stack.append(pair)
    print(x, "inserted successfully")
 
# function for returning last
# element of stack
def get_last_element():
     
    global min_element, stack
     
    if (len(stack) == 0):
        print("UnderFlow Error")
        return None
    else:
        return stack[-1][0]
 
# function for removing last
# element successfully;
def remove_last_element():
     
    global min_element, stack
    if (len(stack) == 0):
        print("UnderFlow Error")
    elif (len(stack) > 1):
        min_element = stack[-2][1]
    else:
        min_element = sys.maxsize
    stack.pop()
     
    print("removed successfully")
 
# function for returning min 
# element till now;
def get_min():
     
    global min_element, stack
    if (len(stack) == 0):
        print("UnderFlow Error")
        return None
         
    return stack[-1][1]


addElement(88)
addElement(5)
addElement(32)
addElement(2)
print(stack)
remove_last_element()
print(get_min())

