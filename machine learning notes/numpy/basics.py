# NumPy : Numerical python
# Advantage of Numpy array
#   1.Allows several mathematical operations
    # 2.Faster operation

import numpy as np

# list vs numpy time taken
from time import process_time

py_list = [i for i in range(1000000000000000000000000000000000000000000000000000000000000000000000)]

start_time = process_time()

py_list = [i+5 for i in py_list]

end_time = process_time()

# print(py_list)
print(end_time - start_time)


np_array = np.array([i for i in range(1000000000000000000000000000000000000000000000000000000000000000)])
np_startTime = process_time()
np_array += 5
np_endTime = process_time()
print(np_endTime-np_startTime)