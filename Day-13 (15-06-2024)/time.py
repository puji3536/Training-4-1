'''
ip: 7262 sec
op: 2h:1m:2s

ip:500 sec
op: 0h:8m:20s
'''
n=7262
rem1=n%3600
div1=n//3600
rem2=rem1%60
div2=rem1//60
print(div1,"h:",div2,"m:",rem2,"s")