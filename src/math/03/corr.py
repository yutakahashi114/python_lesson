def find_corr_x_y(x, y):
    n = len(x)

    if n != len(y):
        print('Bad length')
    else:
        prod = []
        for xi, yi in zip(x, y):
            prod.append(xi * yi)
        sum_prod_x_y = sum(prod)

        sum_x = sum(x)
        sum_y = sum(y)
        squared_sum_x = sum_x ** 2
        squared_sum_y = sum_y ** 2

        x_square = []
        for xi in x:
            x_square.append(xi ** 2)
        x_square_sum = sum(x_square)

        y_square = []
        for yi in y:
            y_square.append(yi ** 2)
        y_square_sum = sum(y_square)

        numerator = n * sum_prod_x_y - sum_x * sum_y
        denominator = ((n * x_square_sum - squared_sum_x) * (n * y_square_sum - squared_sum_y))** 0.5
        correlation = numerator / denominator

        return correlation
