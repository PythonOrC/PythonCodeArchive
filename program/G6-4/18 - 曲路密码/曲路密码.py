from numpy import array, nditer

plaintext = "One inch of time, one inch of gold"
ciphertext = ""


def RowNumber(lens):
    col = 5
    row = lens % col
    if row != 0:
        lens = lens + (col - row)
    row = lens // col
    return lens, row, col


def FillTable(content):
    length = len(content)
    lens, row, col = RowNumber(length)
    if lens - length != 0:
        content += (lens - length) * " "
    plain_arr = array(list(content)).reshape(row, col)

    return plain_arr


def Curvedpath(content):
    n = 1
    ciphertext = []
    for sub in content:
        ciphertext.append(sub[:: 1 if n % 2 == 0 else -1])
        n += 1
    return array(ciphertext)


cipher_arr = Curvedpath(FillTable(plaintext))
ciphertext = ""
for i in nditer(cipher_arr):
    ciphertext += str(i)
print(ciphertext)
