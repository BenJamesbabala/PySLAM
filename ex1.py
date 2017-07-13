from rplidar import RPLidar
import math

lidar = RPLidar('/dev/ttyUSB0')

try:
    for i, scan in enumerate(lidar.iter_scans()):
        for s in scan:
            print("角度：",s[1],"向量長度：",s[2],"x:",s[2]*math.sin(math.pi*s[1]/180),"y:",s[2]*math.cos(math.pi*s[1]/180))

        if i > 50:
            break
except:
    for i, scan in enumerate(lidar.iter_scans()):
        for s in scan:
            print("角度：",s[1],"向量長度：",s[2],"x:",s[2]*math.sin(math.pi*s[1]/180)/10,"y:",s[2]*math.cos(math.pi*s[1]/180)/10)

        if i > 50:
            break
lidar.stop()
lidar.stop_motor()
lidar.disconnect()