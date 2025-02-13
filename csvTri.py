from packages.triangles import Triangle
import csv

with open("tri_sides.csv", "r", encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    newCsvData = []
    for row in reader:
        tri = Triangle(row['side_a'], row['side_b'], row['side_c'])
        print(tri.validtyStatement)
        print(tri.triangleTypeStatement)
        
        newCsvData.append({
            'side_a': row['side_a'],
            'side_b': row['side_b'],
            'side_c': row['side_c'],
            'validity': tri.validtyWord,
            'triangle_type': tri.triangleType
        })
