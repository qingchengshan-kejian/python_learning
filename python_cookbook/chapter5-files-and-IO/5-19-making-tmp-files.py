from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    # read and write to the file
    f.write('hello world\n')
    f.write('testing\n')

    # seek back to begining and read the data
    f.seek(0)
    data = f.read()
    print(data)