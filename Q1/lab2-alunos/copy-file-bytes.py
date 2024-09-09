def copy_binary_file(input_file, output_file, start_byte, end_byte=None):
    with open(input_file, 'rb') as f1, open(output_file, 'wb') as f2:
        if end_byte is None:
            f1.seek(start_byte)
            f2.write(f1.read())
        else:
            length = end_byte - start_byte
            f1.seek(start_byte)
            f2.write(f1.read(length))

def join_binary_files(file1, file2, output_file):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2, open(output_file, 'wb') as out:
        out.write(f1.read())
        out.write(f2.read())

# Example usage:
# copy_binary_file('input.bin', 'output.bin', 0, 30) # Copy bytes 0-30 to output.bin
# copy_binary_file('input.bin', 'output.bin', 54) # Copy bytes 54 to the end to output.bin

copy_binary_file('c-academy.bmp', 'head', 0, 54)
copy_binary_file('c-academy.bmp', 'body', 55)
join_binary_files('head', 'body', 'c-academy-original.bmp')
