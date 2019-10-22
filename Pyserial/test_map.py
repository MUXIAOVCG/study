from pyecharts.charts import Line

def make_chart(yaxis):
    line = Line ()
    xaxis = []
    for i in range(len(yaxis)):
        xaxis.append(i+1)
    line.add_xaxis(xaxis)
    line.add_yaxis("thickness",yaxis, is_symbol_show=False
                   ,is_connect_nones=True)
    # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
    # 也可以传入路径参数，如 bar.render("mycharts.html")

    line.render()
    
ya = [1,2,3,4,None,5,6]
make_chart(ya)
