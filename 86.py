'''Please write a program to compress and decompress the string "hello world!hello world!hello world!hello
world!".
Use zlib.compress() and zlib.decompress() to compress and decompress a string.
'''
import zlib
original_string = "This is String"
compressed_data = zlib.compress(original_string.encode())
print("Compressed data:", compressed_data)
decompressed_data = zlib.decompress(compressed_data)
print("Decompressed data:", decompressed_data.decode())
