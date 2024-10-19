from collections import deque

d = deque()

def create_deque(string):

  list_of_chars = list(string.lower().replace(" ", ""))

  for char in list_of_chars:
    d.append(char)



def is_polindrome(string):
  
  create_deque(string)
  
  while len(d) > 1:
    first_char = d.popleft()
    last_char = d.pop()

    if  first_char == last_char:
      return f'{string} - is polindrome!'
    
  return f'{string} - is NOT polindrome!'


def main():
  result = is_polindrome('A fan a plan a canal Panama')
  print(result)


if __name__ == "__main__":
  main()