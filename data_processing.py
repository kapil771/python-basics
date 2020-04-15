import numpy as np
import sklearn.preprocessing


Input_data = np.array([2.1, -1.9, 5.5],
					  [-1.5, 2.4, 3.5])

data_binarized = preprocessing.Binarizer(threshold = 0.5).transform(Input_data)
print("\nBinarized data:\n", data_binarized)