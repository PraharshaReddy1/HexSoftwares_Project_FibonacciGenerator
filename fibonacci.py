
# fibonacci.py

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

if __name__ == "__main__":
    terms = int(input("Enter number of terms: "))
    fibonacci(terms)
