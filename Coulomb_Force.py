q1=-2.0
q2=1.0
k=1
r1=[-2.0, 1.2, -3.1]
r2=[0.6, -2.0, 4.1]
r1x,r1y,r1z=r1[0],r1[1],r1[2]
r2x,r2y,r2z=r2[0],r2[1],r2[2]
R=((r1x-r2x)**2+(r1y-r2y)**2+(r1z-r2z)**2)**0.5
force=k*(q1*q2)/R
print(force)