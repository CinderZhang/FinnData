# Prompt Example

* Hello, ChatGPT. I am [your name], a student in a finance course where we're learning Python with your assistance. I would like you to assign me three simple Python coding tasks related to [insert specific Python topic such as loops, functions, etc.]. The aim is to evaluate my Python coding skills. Please provide one assignment at a time and wait for my solution before proceeding to the next one. Once I've submitted all three solutions, I'd appreciate it if you could assess my performance and assign a grade from A to C based on the quality of my work.

* Replace the text in '[' ']' as appropriate

## Follow it for each weekly lesson

---

Hello, ChatGPT. I am Apple Bee, a student in a finance course where we're learning Python with your assistance. I would like you to assign me three simple Python coding tasks related to loop. The aim is to evaluate my Python coding skills. Please provide one assignment at a time and wait for my solution before proceeding to the next one. Once I've submitted all three solutions, I'd appreciate it if you could assess my performance and assign a grade from A to C based on the quality of my work.

---

**ChatGPT**: Hello Apple Bee, it's great to hear that you're learning Python and I'm glad to assist you. Let's start with the first assignment related to loops.

**Assignment 1: Fibonacci Sequence**

Write a Python program to generate the first 10 numbers in the Fibonacci sequence. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. 

Here's the start of the sequence for your reference: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

Please submit your solution when you're ready, and I'll review it before we move on to the next assignment.

---

**Apple Bee**: Can you give me a hint?

---

**ChatGPT**: Sure, I'd be happy to give you a hint!

To solve this problem, you'll want to use a loop that iterates 10 times, since we want the first 10 numbers in the Fibonacci sequence.

Here's a rough outline of what your code might look like:

1. Initialize two variables, let's call them `a` and `b`, to 0 and 1 respectively. These will hold the current and next number in the Fibonacci sequence.
2. Create a loop that runs 10 times.
3. In each iteration of the loop:
   - Print the current number in the sequence.
   - Update `a` and `b` so that `a` gets the value of `b` and `b` gets the value of `a + b`. This will move you two steps forward in the sequence.

Remember, the Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.

I hope this helps! Let me know if you have any other questions.


---

**Apple Bee**: Here is my answer:

```python
# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Loop 10 times
for i in range(10):
    # Print the current Fibonacci number
    print(a)

    # Update a and b to the next two Fibonacci numbers
    a, b = b, a + b
```

---

**ChatGPT**: Great job, Apple Bee! Your code correctly generates the first 10 numbers in the Fibonacci sequence. You've used the loop effectively and your code is clean and easy to understand.

Now, let's move on to the second assignment.

**Assignment 2: Prime Numbers**

Write a Python program that asks the user for a number `n` and prints all the prime numbers up to `n`. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, the first six prime numbers are 2, 3, 5, 7, 11, and 13.

Please submit your solution when you're ready, and I'll review it before we move on to the next assignment.

---