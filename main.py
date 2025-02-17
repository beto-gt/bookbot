def main():
  dict1 = {}
  path1 ="books/frankenstein.txt"
  
  with open(path1, "r") as f:
    file_contents = f.read().lower()
    words = len(file_contents.split())
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
   
    for char in file_contents:
      if char.isalpha():
        dict1[char] = dict1.get(char,0) + 1

  [print (f"The '{key}' character was found {value} times") for key, value in dict1.items()]

main() 
