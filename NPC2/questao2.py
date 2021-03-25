with open("m5.txt", "w") as mult5:
    with open("m3.txt", "w") as mult3:
        for n in range(0, 200):
            if n % 5 == 0:
                mult5.write(f"{n}\n")
            elif n % 3 == 0:
                mult3.write(f"{n}\n")