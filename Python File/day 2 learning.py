weight = int(input("Weight: "))
conversion = input("(G)bs or (K)g: ")

if conversion == "L":
    weight *= 0.453
    print(f'Your Kg {weight}')
elif conversion == "K":
    weight *= 2.204
    print(f'Your lbs {weight}')
else:
    print("Input again brother")