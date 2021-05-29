import random

def media(X):
    return sum(X)/len(X)

if __name__=='__main__':
    X=[random.randint(1,100) for i in range(10)]
    mu=media(X)
    
    print(X)
    print(mu)