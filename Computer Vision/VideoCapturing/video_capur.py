

import cv2
from datetime import datetime
import pandas
from  bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df=pandas.DataFrame(columns=["Start", "End"])
refresh=int(input("Ingrese velocidad de Actualización (Frames): "))
first_frame = None
video=cv2.VideoCapture(0)
count=0
times=[]
while count <30:
    count=count+1
    print("\r[+]Timer: " + str(count), end="")
    check, frame=video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    first_frame=gray
times=[]
timer=0
status_list=[None, None]
while True:
    timer=timer+1
    check, frame=video.read()
    status=0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if timer == refresh:
        first_frame = gray
        print(first_frame)
        timer=0
        continue

    delta_frame=None
    delta_frame=cv2.absdiff(first_frame,gray,delta_frame)

    threshold=cv2.threshold(delta_frame, 30, 225, cv2.THRESH_BINARY)[1]
    threshold=cv2.dilate(threshold,None, iterations=2)

    (cnts,_)=cv2.findContours(threshold.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y),(x+w, y+h),(0,255,0), 3)

    status_list.append(status)
    status_list=status_list[-2:]

    if status_list[-1]==1 and status_list[-2] ==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    #cv2.imshow("Baseline",first_frame)
    #cv2.imshow("Captured", gray)
    #cv2.imshow("Delta",delta_frame)
    #cv2.imshow("Threshold Frame", threshold)
    cv2.imshow("ColorFrame",frame)
    key=cv2.waitKey(1)
    if key == ord('q'):
        if status==1:
            times.append(datetime.now())
        break
    print("\r[+]Frames: " + str(timer)+ " [+]Status: " + str(status), end="")
    #print (status_list)
    #print (times)

for i in range(0, len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]}, ignore_index=True)

df.to_csv("times.csv")

df["Start_String"]=df["Start"].dt.strftime("%Y-%m-%d %H-%M-%S")
df["End_String"]=df["End"].dt.strftime("%Y-%m-%d %H-%M-%S")
cds=ColumnDataSource(df)
p=figure(x_axis_type='datetime', height=100, width=500, sizing_mode="scale_width", title="Grafica de Movimientos")
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start ","@Start_String"),("End ","@End_String")])
p.add_tools(hover)
q=p.quad(left="Start",right="End",bottom=0,top=1, color="red", source=cds)

output_file("graph.html")

show(p)
#print(status_list)
video.release()
cv2.destroyAllWindows()
