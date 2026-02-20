hh,mm,ss=map(int,input().split(':'))
gh,gm,gs=map(int,input().split(':'))

sec = (hh*60 + mm)*60 + ss
g_sec = (gh*60 + gm)*60 + gs

wait_sec = g_sec - sec
if sec > g_sec or wait_sec==0:
    wait_sec += 24*60*60
print(str(wait_sec//60//60).zfill(2)+':'+str(wait_sec//60%60).zfill(2)+':'+str(wait_sec%60).zfill(2))