import numpy as np

def calFloat32(ee,mm):
    #小数的权重
    mesamulti = 2**np.float64((np.arange(-1,-24,-1)))
    
    if ee==0:
        E = 2**(-126)
        # 此处填入一行
        
    else:
        E = 2**(np.float64(ee)-127)
        #小数部分
        # 此处填入一行
        #加上整数部分
        # 此处填入一行
    return F32

#正算32位浮点
#忽略符号位
#指数部分
ee=np.float64(127)
#小数部分
mm1 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
mm2 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0])

F32_1 = calFloat32(ee,mm1)
F32_2 = calFloat32(ee,mm2)
delta = F32_2-F32_1

    