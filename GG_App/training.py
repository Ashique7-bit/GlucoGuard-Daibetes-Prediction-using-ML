import csv
x=[]
y=[]
i=0
with open(r'C:\Users\Admin\OneDrive\Desktop\Project Final\Gluco_Gaurd\GG_App\Dataset of Diabetes .csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
    if i!=0:

        r=[]
        if lines[2]=="M":
            r.append(0)
        else:
            r.append(1)
        r.append(float(lines[3]))
        r.append(float(lines[4]))
        r.append(float(lines[5]))
        r.append(float(lines[6]))
        r.append(float(lines[7]))
        r.append(float(lines[8]))
        r.append(float(lines[9]))
        r.append(float(lines[10]))
        r.append(float(lines[11]))

        r.append(float(lines[12]))
        x.append(r)
        print(r,lines[13])
        if lines[13]=='Y' or lines[13]=='Y ':
            y.append(1)
        else:
            y.append(0)
    i=i+1



from sklearn.neighbors import KNeighborsClassifier

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=1)
neigh.fit(x, y)
def predict_fn(smp):
    res=neigh.predict([smp])
    return res[0]
