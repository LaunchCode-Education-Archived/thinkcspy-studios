# Studio: Yahtzee

## Concepts Used

- Working with nested lists

## Walkthrough

Imagine that you work for a large retailer, writing software for its internal accounting system. You've been asked to write a function `average_sales` that can take a set of data representing daily sales at a given store, and calculate the average sales for each week represented by the data.

The data is represented as follows:

A single week of daily sales is a list with 7 entries, one for each day of the week (0 = Monday, 6 = Sunday): `[1512.30, 1555.72, 1989.77, 2101.33, 1884.45, 1333.33, 1456.23]`

You are given data for several weeks at once, itself collected into another list:

```python
sales = [[1512.30, 1555.72, 1989.77, 2101.33, 1884.45, 1333.33, 1456.23],
[1215.340, 1565.99, 2989.34, 2301.77, 1234.81, 1923.44, 2282.39],
...]
```

Here, ``sales[0]`` is a list of sales totals for each day of the first week, ``sales[1]`` a list of sales totals for each day of the second week, and so on. We will implement ``average_sales`` so that it returns a list of the averages for each week.

So if `sales` is the list above and we call `weekly_averages = average_sales(sales)`, then `weekly_averages[0]` is the average for week 0, and so on.

## Studio

[Book Page Link](https://runestone.launchcode.org/runestone/static/thinkcspy/Studios/yahtzee.html)
