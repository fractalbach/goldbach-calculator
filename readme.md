# goldbach's conjecture calculator

python program that takes an integer n as input, and calculate 2
primes that equal n (if n is even), or n+1 (if n is odd).  Input can
be a data stream (manual input or files), where each number is
seperated by a newline.



## Example

Invoked from bash, with `example.txt` file as the input:

~~~bash
python3 goldbach.py < example.txt
~~~


Output:

~~~
4 = 2 + 2 + 1
5 = 2 + 2
6 = 3 + 3 + 1
7 = 3 + 3
8 = 5 + 3 + 1
9 = 5 + 3
10 = 7 + 3 + 1
12 = 7 + 5 + 1
123 = 109 + 13
12345 = 12301 + 43
123456 = 123449 + 7 + 1
~~~