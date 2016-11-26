from test import testEqual

def average_sales(daily_sales):

    num_weeks = len(daily_sales)
    weekly_averages = [0 for i in range(num_weeks)]

    for week in range(0, num_weeks):

        # calculate the average for the given week
        week_sum = 0
        for day_total in daily_sales[week]:
            week_sum += day_total

        weekly_averages[week] = week_sum / len(daily_sales[week])


    return weekly_averages


sales = [[1, 1, 1, 1, 1, 1, 1],
    [1, 0, 2, 0, 2, 1, 1]]

testEqual(average_sales(sales), [1, 1])
