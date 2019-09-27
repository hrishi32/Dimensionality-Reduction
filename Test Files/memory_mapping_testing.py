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


def get_adversarial_positions(demo_operator, batch_feature_size):
	feature_counter = demo_operator.get_feature_counter()
	# print ("Originl feature counter:",feature_counter)
	batch_positions = []

	while len(batch_positions) < batch_feature_size:
		alpha = random.randint(0, len(feature_counter)-1)

		for i in feature_counter[alpha]:
			if len(batch_positions) < batch_feature_size:
				batch_positions.append(i)
			else:
				break
		
	batch_positions.sort()
	# print ("batch positions:",batch_positions)
	return batch_positions

		


def get_feature_deletion_results(Input_dimension ,Output_dimension ,array1,array2,mapping_scheme=1,max_value=0):

	batch_error = []
	sample_size = Input_dimension/100
	reduced_input_dim = Input_dimension/4
	demo_operator = operator(input_dim=Input_dimension, output_dim=Output_dimension, mapping_scheme=mapping_scheme)
	batch_inner_product1 = []
	batch_inner_product2 = []
	while Input_dimension >= reduced_input_dim:
		# print ("epoch1:::Input Dimenson::",Input_dimension)
		batch_feature_size = int(sample_size)
		batch_positions = get_adversarial_positions(demo_operator,batch_feature_size)
		Input_dimension-=batch_feature_size

		array1,array2 = demo_operator.batch_delete_feature(batch_positions,array1,array2)
        # print("batch feature deletion done....")
        # print("arr1:",array1)
        # print("arr2:",array2)
		inner_product1, inner_product2 = demo_operator.inner_product(array1, array2)
		error = abs(inner_product1-inner_product2)
		# print ("inners products:",inner_product1,inner_product2)
		# print("error:", error)
		batch_error.append(error)
		batch_inner_product1.append(inner_product1)
		batch_inner_product2.append(inner_product2)
		# print ("Mapping scheme :",mapping_scheme,"::")
		# print (demo_operator.get_feature_counter())
		

	return batch_error,batch_inner_product1,batch_inner_product2,array1,array2

def main():
	alpha = random.randint(10,100)
	print ("* Alpha (Max value of any attribute) of dataset:",alpha)
	N = 2000
	M = 100
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

	batch_error,batch_inner_product1,batch_inner_product2,_,_ = get_feature_deletion_results(Input_dimension = N,Output_dimension = M,array1=norm_arr_1,array2=norm_arr_2,mapping_scheme=3,max_value=alpha)

	plt.plot(range(len(batch_error)), batch_error, label = "Error Without Compensation")
	plt.plot(range(len(batch_inner_product1)), batch_inner_product1, label = "IP1 Without Compensation")
	plt.plot(range(len(batch_inner_product2)), batch_inner_product2, label = "IP2 Without Compensation")

	batch_error,batch_inner_product1,batch_inner_product2,_,_ = get_feature_deletion_results(Input_dimension = N,Output_dimension = M,array1=norm_arr_1,array2=norm_arr_2,mapping_scheme=4,max_value=alpha)

	# print(batch_error,batch_inner_product1,batch_inner_product2,array1,array2)

	plt.plot(range(len(batch_error)), batch_error, label = "Error With Compensation")
	plt.plot(range(len(batch_inner_product1)), batch_inner_product1, label = "IP1 With Compensation")
	plt.plot(range(len(batch_inner_product2)), batch_inner_product2, label = "IP2 With Compensation")
	plt.legend()
	plt.show()


if __name__ == '__main__':
	main()