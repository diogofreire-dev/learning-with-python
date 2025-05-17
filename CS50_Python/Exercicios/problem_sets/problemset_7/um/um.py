import re

def main():
    print(count(input("Text: ")))

def count(s):
    # Use a regular expression to find all occurrences of "um" as a word
    # \b marks a word boundary
    # (?i) makes the pattern case-insensitive
    matches = re.findall(r"(?i)\bum\b", s)
    return len(matches)

if __name__ == "__main__":
    main()