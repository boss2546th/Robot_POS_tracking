import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


direct_list = ['-x', 'y', 'x', '-y']

degree = 1


def return_direct(control, step, degree, length = 4):
    tl = control == 'tl'
    tr = control == 'tr'
    degree = length - (degree) if tl else degree
    step += degree
    step = step % length
    degree = step if (tl and step==0) or tr else length - step
    return degree

def return_position(control,direct,step,x,y):
    positive = int(direct == 'x' or direct == 'y')
    nagative = int(direct == '-x' or direct == '-y')
    reverse = int(control != 'bk')
    krv = -1 + (reverse*2)
    kx,ky = 0,0
    if positive:
        kx = int(direct == 'x')
        ky = int(direct == 'y')
    elif nagative:
        kx = int(direct == '-x')*-1
        ky = int(direct == '-y')*-1
    x += (kx * step * krv)
    y += (ky * step * krv)
    return [x,y]


### initialization
posit = input()
posit = posit.replace(posit[0],'')
posit = posit.replace(posit[-1],'')
xy = posit.split(',')
x = int(xy[0])
y = int(xy[1])

transit = []
infodirect = [1]
infox = [x]
infoy = [y]

### getInput
while True:
    ip = input()
    if ip == 'END':
        break
    else:
        transit.append(ip)

step = 1

### process Findout position
for i in transit:
    if i == 'fw' or i == 'bk':
        new_posit = return_position(i,direct_list[degree], step, x, y)
        x =  new_posit[0]
        y = new_posit[1]
    elif i == 'tl' or i == 'tr':
        degree = return_direct(i, step, degree)
    else:
        print('Error: unknown control')
        continue
    direct = direct_list[degree]
    infodirect.append(degree)
    infox.append(x)
    infoy.append(y)
    #opt = '| (' + str(x) + ',' + str(y) + ')'
    #print(i, end=': ')
    #print(opt, "| direct :", direct)

### animation transitiion of robot
xani = []
yani = []
fig, ax = plt.subplots()

def animate(i):
    try:
        H = 'Start' if not i else transit[i - int(i != 0)]
        xani.append(infox[i])
        yani.append(infoy[i])
        opt = H + ': | (' + str(infox[i]) + ',' + str(infoy[i]) + ')'+ " | direct : " + direct_list[infodirect[i]]
    except:
        opt = 'END'
    klim = 1
    ax.clear()
    plt.title(opt)
    print(opt)
    ax.plot(xani, yani)
    ax.scatter(xani, yani)
    mn_lim = min([min(infox),min(infoy)])
    mx_lim = max([max(infox), max(infoy)])
    ax.set_xlim([mn_lim-klim,mx_lim+klim])
    ax.set_ylim([mn_lim-klim,mx_lim+klim])


ani = FuncAnimation(fig, animate, frames=len(transit)+2, interval=1500, repeat=False)

plt.show()

# ################
# input Test case Example
# (0,2)
# fw
# bk
# tl
# tl
# tl
# fw
# tr
# fw
# fw
# tl
# fw
# bk
# tl
# tl
# END


