Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # CS104
... # Kiumbura Githinji
... # PythonQueue.py
... 
... # Create a list/queue called names
... names = [Joe, John, Mike, Lisa, George, Thomas, Harry, Jadyn, Ava, Harley]
... 
... # Input 10 names into the queue
... for _ in range(10):
...     accepted_name = input("Enter a name: ")
...     names.append(accepted_name)
... 
... # Print the initial list/queue
... print("Initial Queue:", names)
... 
... # Dequeue each name and print it
... for _ in range(len(names)):
...     dequeued_name = names.pop(0)
...     print(dequeued_name)
... 
... # Print the list/queue after dequeuing
... print("Queue after dequeuing:", names)
