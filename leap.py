#hari
year=int(input())
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Yes")
        else:
            print("no")
    else:
        print("Yes")
else:
    print("no")
