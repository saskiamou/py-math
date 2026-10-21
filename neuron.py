x = 3 # input
target = 15 # desired answer
w = 0.5 # weight

for step in range(50):
    y = w * x
    error = (y - target) ** 2 # whatever y is, see how far off from target
    slope = 2 * (y - target) * x # derivative of error WRT to w
    w = w - 0.1 * slope # step downhill

    print(step, round(w, 4), round(error, 8))