def is_prime():
    chislo = int(input("Chislo: "))
    if chislo > 1000:
        print("Chislo velike")
        quit()
    if chislo % 2 == 0:
        return True
    else: 
        return False

print(is_prime())
