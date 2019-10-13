import pygal, random

xs = [2*random.random() for i in range(100)]
ys = [x**2 + 2*random.random() - 1 for x in xs]

xys = zip(xs, ys)

xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Andy Scatterplot'
xy_chart.add('Zippin', xys)
xy_chart.render()