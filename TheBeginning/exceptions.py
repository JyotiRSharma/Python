while True:
    try:
        number = int(input("Enter your fav number hoss:"))
        print(20/number)
        break

    except ValueError:
        print("Enter a number")

    except ZeroDivisionError:
        print("0 is not allowed")

    finally:
        print("loop end")
