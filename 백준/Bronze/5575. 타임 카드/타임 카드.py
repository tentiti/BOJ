for i in range(3):
    ch, cm, cs, th, tm, ts = map(int, input().split())
    workSec = ts-cs + (tm-cm) * 60 + (th - ch) * 3600
    print(workSec//3600, (workSec%3600)//60, workSec%60)