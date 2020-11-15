xposlist = []
yposlist = []
xaverage = yaverage = xyproductsum = xsquaresum = a = b = 0.0
length = 0

while True:
    inp = input("Input the position(split with a space, end with the word\"End\"):").split(' ')
    if inp[0] == 'End':    break
    xposlist.append(float(inp[0]))
    yposlist.append(float(inp[1]))
    length += 1

for i in range(0, length):
    xaverage += xposlist[i]
    yaverage += yposlist[i]
    xyproductsum += (xposlist[i] * yposlist[i])
    xsquaresum += xposlist[i] * xposlist[i]

xaverage /= length
yaverage /= length

b = (xyproductsum - length * xaverage * yaverage) / (xsquaresum - length * xaverage * xaverage)
a = yaverage - b * xaverage

if a > 0.0:
    print("The linear regression equation is:y = {:.2f}x + {:.2f}".format(b, a))
else:
    print("The linear regression equation is:y = {:.2f}x - {:.2f}".format(b, abs(a)))