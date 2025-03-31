def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n+1):
        yield "sheep " * i # yield is a generator that produces a sequence 
                           # of results, rather than computing them all at 
                           # once and returning them in a list,

if __name__ == "__main__":
    main()