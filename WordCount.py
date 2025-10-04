#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0
  wordCount = 0 
  letterCount = 0 
  
  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    print(words)
    for w in words:
      wordCount = wordCount + 1
    letters = list(line)
    for char in letters:
      if char.isalpha():
        letterCount = letterCount + 1
  

  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Letters:", letterCount)
  

if __name__ == '__main__':
  main()
