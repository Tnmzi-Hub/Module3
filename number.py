while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Enter valid integer!")
        continue
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
    break