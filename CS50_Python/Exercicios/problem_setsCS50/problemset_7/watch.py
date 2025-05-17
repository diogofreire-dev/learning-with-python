import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Pattern to find iframe with YouTube embed URL
    # Looking for src attribute containing youtube.com/embed/ followed by the video ID
    pattern = r'<iframe[^>]*src="(https?://)?(www\.)?youtube\.com/embed/([^"]+)"'
    
    # Search for the pattern in the input string
    match = re.search(pattern, s)
    
    # If a match is found, return the youtu.be URL
    if match:
        video_id = match.group(3)
        return f"https://youtu.be/{video_id}"
    
    # Return None if no match is found
    return None


if __name__ == "__main__":
    main()