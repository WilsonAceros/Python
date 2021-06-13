seguir = True

def range_con_stop(n):
    for i in range(n):
        if seguir==False:
            return
        yield i

for i in range_con_stop(1000):
    print(i)
    if i==10:
        seguir = False