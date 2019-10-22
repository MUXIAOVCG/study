from pyecharts.charts import Line

X = [28.9]*10
n = len(X)
y = []
for i in range(n):
    y.append(i+1)

bar = Line()
bar.add_xaxis(y)
bar.add_yaxis("thickness", X)
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")

bar.render()