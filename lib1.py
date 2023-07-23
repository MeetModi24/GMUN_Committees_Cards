import numpy as np
# a = np.array([1,2,3],dtype='int16')
# print(a)
# b = np.array([[2.2,3.4,3.3],[3.4,5.5,44.4]])
# print(b)
# print(b.ndim)
# print(b.shape)
# print(b.dtype)
# print(a.itemsize)
# print(a.nbytes,a.size*a.itemsize)


# a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(a)
# print(a[1,5],a[1,-2])
# print(a[0,:],a[:,2])
# print(a[0,1:6:2])
# a[1,5] = 20
# a[:,2] = 5 
# print(a)
# a[:,2] = [9,2]



# b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(b)
# print(b[0,1,1])
# print(b[:,1,:])
# b[1,0,0] = 9
# print(b)
# b[:,1,:] = [[10,11],[12,13]]
# print(b)


# a = np.zeros(5)
# print(a)
# a = np.zeros((2,3))
# b = np.ones((4,2,2),dtype='int32')
# print(b)
# c = np.full((2,2),99,dtype='float32')
# print(c)
# d = np.full_like(b,4)
# print(d,np.full(b.shape,4))

# a = np.random.rand(4,2)
# print(a)
# b = np.random.random_sample(a.shape)
# print(b)
# c = np.random.randint(-4,7,size=(3,3))
# print(c)
# d = identity(3)
# print(d)

# a = np.array[[1,2,3]]
# b = np.repeat(a,3,axis=0)
# print(a,b)


# output = np.ones((5,5))
# print(output)
# z = np.zeros
# a[1,1] = 9
# print(z)
# output[1:4,1:4] = z
# print(output)


# a = np.array([1,2,3])
# b = a
# print(b)
# b[0] = 100
# print(a,b)

# a = np.array([1,2,3])
# b = a.copy()
# print(b)
# b[0] = 100
# print(a,b)

# a = np.array([1,2,3,4])
# b = a+2
# print(a,b,a*2,a/2,a+b,a**2)
# c = np.sin(a)
# print(c)

# LINEAR ALGEBRA
# a = np.ones(2,3)
# print(a)
# b = np.full((3,2),2)
# print(b)
# c = np.matmul(a,b)
# print(c)
# d = np.identity((3))
# e = np.linalg.det(d)
# print(e)

# Statistics
# stats = np.array([[1,2,3],[4,5,6]])
# a = np.min(stats)
# b = np.max(stats)
# c = np.min(stats,axis=1)
# d = np.min(stats,axis=0)
# e = np.sum(stats)
# f = np.sum(stats,axis=1)
# print(a,b)
# print(c,d)

# Reorganizing
# before = np.array([[1,2,3,4],[5,6,7,8]])
# print(before)
# after = before.reshape((8,1))
# print(after)
# c = before.reshape((2,2,2))

# Stacking vectors vertically
# v1 = np.array([1,2,3,4])            # ERROR IF SIZES ARE NOT SAME
# v2 = np.array([5,6,7,8])
# c = np.vstack([v1,v2])
# print(c)
# d = np.vstack([v1,v2,v1,v2])
# print(d)

# Horizontal stack
# a = np.ones((2,4))
# b = np.zeros((2,2))
# c = np.hstack((a,b))
# print(a)
# print(b)
# print(c)

# Load data from file
# filedata = np.genfromtxt('data.txt',delimiter=',')
# print(filedata)
# a = filedata.astype('int32')

# Boolean Masking and Advanced Indexing
# b = filedata>50
# c = filedata[filedata>50]
# d = np.array([1,2,3,4,5,6,7,8,9])     
# e = d[[1,2,8]]                        # IMPORTANT
# f = np.any(filedata>50, axis=0)
# g = np.all(filedata>50,axis=0)
# h = ((filedata)>50 & (filedata)<100)
# i =(~((filedata)>50 & (filedata)<100))
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)


# a = np.array[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
# print(a)
# print(a[2:4,0:2])
# print(a[[0,4,5],3:])
# print(a[[0,1,2,3],[1,2,3,4]])



