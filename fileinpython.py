# Writing a string to a file
with open("file.txt", "w") as file:
    text = "Hello, World!"
    file.write(text)

# Writing bytes to a file
with open("file.bin", "wb") as file:
    data = bytes([0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x2c, 0x20, 0x57, 0x6f, 0x72, 0x6c, 0x64, 0x21])
    file.write(data)
