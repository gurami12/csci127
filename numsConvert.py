#CSci 127 Teaching Staff
#February 2019
#A program that uses functions to print out months.
#Modified by:  ADD YOUR NAME HERE

def num2string(num):
     """
     Takes as input a number, num, and
     returns the corresponding name as a string.
     Examples: num2string(0) returns "zero", num2string(1)returns "one"
     Assumes that input is an integer ranging from 0 to 9
     """
     
     numString = ""

    if num=="0":
          print("Zero")
      if num=="1":
          print("one")
      if num=="2":
          print("two")
      if num=="3":
          print("Three")
      if num=="4":
          print("Four")
      if num=="5":
          print("Five")
      if num=="6":
          print("Six")
      if num=="7":
          print("Seven")
      if num=="8":
          print("Eight")
      if num=="9":
          print("Nine")
   
     return(numString)



def main():
     nums = input('Enter a multi-digit number: ')
     newStr = ""
     for n in nums:
         word = num2string(int(n))
         newStr = newStr + " " + word
     msg = 'In words, your number is:' + newStr + "."
     print(msg)   


#Allow script to be run directly:
if __name__ == "__main__":
     main()
