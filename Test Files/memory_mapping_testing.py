from Object_Files.mapper3 import mapper,np
from Object_Files.basic_operator import operator
import matplotlib.pyplot as plt
import random


def array_normalization(input_array):
    array_norm = np.linalg.norm(input_array)
    # print ("array norm:",array_norm)
    result = np.zeros(input_array.size, dtype=float)
    for i in range(input_array.size):
        result[i] = (1.0*input_array[i])/array_norm

    return result


def main():
	alpha = random.randint(0,10)
	print ("* Alpha (Max value of any attribute) of dataset:",alpha)
	N = 50000
	M = 3000
	print ("* Input Dimension of Dataset:",N)
	print ("* Output (compressed) Dimension of Dataset:",M)

	arr1 = np.random.randint(0,alpha,size=N)
	arr2 = np.random.randint(0,alpha,size=N)

	print ("* Selected array (1) from Dataset:",arr1)
	print ("* Selected array (2) from Dataset:",arr2)

	norm_arr_1 = array_normalization(arr1)
	norm_arr_2 = array_normalization(arr2)

	print ("* Normalized array (1):",norm_arr_1)
	print ("* Normalized array (2):",norm_arr_2)

	result = get_feature_deletion_results(Input_dimension = N,Output_dimension = M,array1=norm_arr_1,array2=norm_arr_2,mapping_scheme=1,max_value=alpha)


if __name__ == '__main__':
	main()