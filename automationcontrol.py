
time = int(input()) 
vi = 3.306
vf = 0.0
ve = 0.0
pos = 0.0
g1 = 7.17
g2 = 5.97
g3 = 4.97 / 60
g4 = 0.003

for t in range(1, time+1):
    vf = pos / 800 * 5
    ve = vi - vf
    p = ve * g1 * g2 * g3 * g4 * 0.1*1000
    pos = pos + p
    print(f"t = {t}, vi = {vi:.3f}, vf = {vf:.4f}, ve = {ve:.3f}, p = {p:.3f}, pos = {pos:.3f}")
