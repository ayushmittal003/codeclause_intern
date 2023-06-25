import time

print("Type the following sentence: ")

para='''
       "Python is a high-level, interpreted programming language known for 
       its simplicity and readability. It was created by Guido van Rossum and 
       first released in 1991. Python's design philosophy emphasizes code 
       readability, making it easier to "write and understand, which has 
       contributed to its popularity among developers."\n
       '''
    
print(para)
input("Press Enter when you're ready to start the timer.\n")

Start_time = time.time()

User_input = input()

End_time = time.time()

duration_time = End_time - Start_time

word=para.split()

typing_speed= len(word)/(duration_time/60)

print(f"\nTotal time duration :{duration_time:.2f}seconds")
print(f"\nYour typing speed :{typing_speed:.2f}words per minute")
print()

