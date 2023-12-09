file = input("File name: ")
file = file.lower()
file = file.strip()
ext = file[-3:]

if ext == "peg":
    ext = "jpeg"

if ext == "gif":
    print("image/gif")
elif ext == "jpg":
    print("image/jpeg")
elif ext == "jpeg":
    print("image/jpeg")
elif ext == "png":
    print("image/png")
elif ext == "pdf":
    print("application/pdf")
elif ext == "txt":
    print("text/plain")
elif ext == "zip":
    print("application/zip")
else:
    print("application/octet-stream")


