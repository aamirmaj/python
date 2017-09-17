if __name__ == '__main__':
    n = int(raw_input())
    if(n % 2 == 0):
        if(n < 6):
            print("Not Weird")
        elif(n < 21):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")
