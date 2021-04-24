def get_avg(grade):
    fist, *middle, last = grade  # Skips the first and last elements and collect the whatever you get in between

    avg = sum(middle) / len(middle)
    print(avg)


get_avg([34, 12, 11, 99, 4])
get_avg([33, 34, 45, 5])
