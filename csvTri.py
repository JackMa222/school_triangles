from packages.triangles import Triangle
import csv
from datetime import datetime

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

with open(f"csv/tri_sides_{datetime.today().isoformat()}.csv", "w") as nf:
    fieldnames = ['side_a', 'side_b', 'side_c', 'validity', 'triangle_type']
    writer = csv.DictWriter(nf, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in newCsvData:
        writer.writerow(row)
    