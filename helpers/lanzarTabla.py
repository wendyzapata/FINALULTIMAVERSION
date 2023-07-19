def lanzarTablaHTML(Dataframe,nombreTabla):
    fileHTML=Dataframe.to_html()
    file=open(f"./tablas/{nombreTabla}.html","w",encoding='utf-8')
    file.write(fileHTML)
    file.close()