hh1 = int(input())
mm1 = int(input())
ss1 = int(input())
hh2 = int(input())
mm2 = int(input())
ss2 = int(input())
ssH = (hh1 * 60) * 60
ssM = mm1 * 60
ssS = ss1 + ssH + ssM
ssH2 = (hh2 * 60) * 60
ssM2 = mm2 * 60
ssS2 = ss2 + ssH2 + ssM2
ssDiff = ssS2 - ssS
print(ssDiff)
