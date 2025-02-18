from packages.triangles import MultipleTriangles

newTriangle = MultipleTriangles("tri_sides.csv")
newTriangle.writeCsvData("csv/")
newTriangle.printCsvData()