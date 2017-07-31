import csv
from session.models import Session
file=open('activity_1.csv','rb') #argv[1]
file_reader=csv.reader(file,delimiter=',')
for row in file_reader:
    Session.objects.create(pace=row[2], avg_hr=row[12])
