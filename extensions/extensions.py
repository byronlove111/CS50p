MIMES_TYPE = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

u_i = input("File name: ").strip().lower()

if '.' in u_i:
    extension = u_i.rsplit(".", 1)
    if extension[1] in MIMES_TYPE:
        print(MIMES_TYPE[extension[1]])
    else:
        print("application/octet-stream")
else:
    print("application/octet-stream")
