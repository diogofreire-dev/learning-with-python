def main():
    # Prompt the user for a file name
    filename = input("File name: ").strip().lower()
    
    # Dictionary mapping file extensions to media types
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    
    # Extract the file extension (everything after the last period)
    # If there's no period, ext will be an empty string
    ext = ""
    if "." in filename:
        ext = filename[filename.rfind("."):]
    
    # Output the media type based on the extension
    if ext in media_types:
        print(media_types[ext])
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()