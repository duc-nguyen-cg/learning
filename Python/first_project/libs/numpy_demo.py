import numpy as np;

#Example 1
base = [1,2,3,4,5]
np_base = np.array(base)
np_power = np_base ** 2
print(np_power)

print(type(base))        #list
print(type(np_power))    #numpy.ndarray


#Example 2
opr1 = [2,3,4,5]
np_opr1 = np.array(opr1)

opr2 = [6,7,8,9]
np_opr2 = np.array(opr2)

print(opr1 + opr2)         # [2, 3, 4, 5, 6, 7, 8, 9]
print(np_opr1 + np_opr2)   # [ 8 10 12 14]


#Example 3
np_result = np.array([True, 1, 2]) + np.array([3, 4, False])   #True = 1; False = 0
print(np_result)



#2D Numpy arrays
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
np_baseball = np.array(baseball)
print(np_baseball.shape)      #(4,2)


non_base = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2, 10.5]]
np_non_base = np.array(non_base)
print(np_non_base.shape)      #(4,) -- not support ragged sequences


#Methods
data = [[10, 20, 30],
        [12,14,16],
        [125, 200, 275],
        [-37, -74, -111]]
np_data = np.array(data)

# Take a rows
row = np_data[2,:]
print(row)

# Take a columns
col = np_data[:,1]
print(col)

#Mean
print(np.mean(col))

#Median
print(np.median(col))

#Correlation coefficient
print(np.corrcoef(
    np_data[:,1],
    np_data[:,2]
))










