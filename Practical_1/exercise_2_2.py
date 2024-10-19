from collections import deque


def is_palindrome(s) -> bool:
    
    deq = deque(s)
    
    if deq.pop() != deq.popleft():
        # Не поліндом
        pass
    # Якщо пройшли всі символи і не було різних то поліндром
    pass

print(is_palindrome("Pan ap"))


