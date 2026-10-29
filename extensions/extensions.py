fn = input("File Name: ")

if fn.endswith(".gif"):
    print("image/gif")
elif fn.endswith(".jpg"):
    print("image/jpeg")
elif fn.endswith(".jpeg"):
    print("image/jpeg")
elif fn.endswith(".png"):
    print("image/png")
elif fn.endswith(".pdf"):
    print("application/pdf")
elif fn.endswith(".text"):
    print("text/plain")
elif fn.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")