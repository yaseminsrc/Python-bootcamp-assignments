num = int(input("Sayı: "))

if num < 2:
    print("Asal değil")

else:
    for i in range(2, num):
        print(f"{num} % {i} = {num % i}") 
        if num % i == 0:
            print("Asal değil")
            break
    else:
        print("Asal")
