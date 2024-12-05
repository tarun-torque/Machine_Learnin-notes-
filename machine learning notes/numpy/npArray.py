import numpy as np

num_arr = np.array([1,2,3,4])
print(num_arr) #[1 2 3 4]
print(type(num_arr)) #<class 'numpy.ndarray'>


# creating 1D array
a= np.array([1,2,3,4,5])
print(a)
print(a.shape) #(5,) --->5 columns

#creating 2D array
# b = np.array([(1,23,3,4),(5,6,7,8)])
# print(b)
# print(b.shape)  #(2,4) -->2 row and 4 col

b = np.array([(1,23,3,4),(5,6,7,8)],dtype=float)
print(b)


#initial placeholder in array
# 1.creating a numpy array as zeros
x = np.zeros((4,1))
print(x)

# 2.creating a numpy array as ones
y = np.ones((3,3))
print(y)

# 3.creating array of a particular value
z = np.full((3,3),5)
print(z)

# 4. identity matrix
w  = np.eye((5))
print(w)

# 5.create numpy array with random values
y = np.random.random((2,2))  # values between 0 and 1
print(y)

# 6.integer random values
s = np.random.randint(1, 10,(3,4))
print(s)

#7.array of evenly spaced values -->specifying number of values required
t = np.linspace(10,30,5)
print(t)

# 8.array of evenly spaced values -->specifying step
e =np.arange(2,22,2)
print(e)

# 9.convert list into np array
myList= [1,2,3,4]
np_arr = np.asarray(myList)
print(type(np_arr))



# Analyzing numpy array

c = np.random.randint(10,50,(5,5))
print(c)

print(c.shape) #shape
print(c.ndim)  #array dimensions
print(c.size)  #number of element in array
print(c.dtype) #data type of element in array



# Mathematical operations
np1  = np.random.randint(0,10,(3,3))
np2 = np.random.randint(10,20,(3,3))
print(np1)
print(np2)
print(np1+np2)
print(np1-np2)
print(np1*np2)
print(np1/np2)

print(np.add(np1,np2))
print(np.subtract(np1,np2))
print(np.multiply(np1,np2))
print(np.divide(np1,np2))

# Array manipulation
trans = np.random.randint(10,20,(4,5))
print(trans.shape)

# 1.transpose 
print(np.transpose(trans).shape)
# => 
print(trans.T.shape)


# reshape array
a = np.random.randint(10, 20,(4,3))
print(a.shape) #(4,3)
print(a.reshape(a))



