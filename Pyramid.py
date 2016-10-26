def pyramid(rows=8):
    for i in range(0,rows):
        print (' ' * (rows-i-1) +  '*' * (2*i+1))
    return

num = int(input("Number of rows: "))
pyramid(num)
