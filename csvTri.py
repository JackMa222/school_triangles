from packages.triangles import MultipleTriangles
import csv
from datetime import datetime

newTriangle = MultipleTriangles("tri_sides.csv")
newTriangle.writeCsvData("csv/")
newTriangle.printCsvData()