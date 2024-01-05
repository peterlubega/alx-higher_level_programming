0x09. Python - Everything is object

This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should read all documentation first (as usual :)), then take the time to think and brainstorm with your peers about what you think and why. Try to do this without coding anything for a few hours.

Trying examples in the Python interpreter will give you most of the answers without having to think about it. Don’t go this route. First read, then think, then brainstorm together. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.

Note that during interviews for Python positions, you will most likely have to answer to these type of questions.

All your answers should be only one line in a file. No space before or after the answer.

===========================================QUESTIONS:==========================================

0. Who am I?
mandatory
What function would you use to get the type of an object?

Write the name of the function in the file, without ().

1. Where are you?
mandatory
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

2. Right count
mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 100

3. Right count =
mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 89

4. Right count =
mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a

5. Right count =+
mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a + 1

6. Is equal
mandatory
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)

7. Is the same
mandatory
What do these 3 lines print?

>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

8. Is really equal
mandatory
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)

9. Is really the same
mandatory
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)


