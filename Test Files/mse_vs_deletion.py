from Object_Files.mapper import mapper, np
from Object_Files.basic_operator import operator
import matplotlib.pyplot as plt
import random

def batch_feature_deletion_error(Input_dim=500,Output_dim=30,rate=10,array1=[],array2=[],mapping_scheme=1):
    batch_error = []
    sample_size = Input_dim/100
    reduced_input_dim = Input_dim/2
    demo_operator = operator(input_dim=Input_dim, output_dim=Output_dim, mapping_scheme=mapping_scheme)
    batch_inner_product1 = []
    batch_inner_product2 = []
    while Input_dim >= reduced_input_dim:
        print ("epoch1:::Input Dimenson::",Input_dim)
        batch_feature_size = int(sample_size)
        batch_positions = []
        batch_value1 = []
        batch_value2 = []
        for i in range(batch_feature_size):
            batch_positions.append(random.randint(0,Input_dim-1))
            batch_value1.append(random.uniform(0,1))
            batch_value2.append(random.uniform(0,1))
            Input_dim -= 1

        array1,array2 = demo_operator.batch_delete_feature(batch_positions,array1,array2)
        inner_product1, inner_product2 = demo_operator.inner_product(array1, array2)
        error = abs(inner_product1-inner_product2)
        print ("inners products:",inner_product1,inner_product2)
        print("error:", error)
        batch_error.append(error)
        batch_inner_product1.append(inner_product1)
        batch_inner_product2.append(inner_product2)

    return batch_error,batch_inner_product1,batch_inner_product2,array1,array2

def main():
    # epochs = 500
    counter = 1
    while counter < 10:
        N = 50000
        print("N: ", N)
        arr1 = np.random.uniform(0, high=1, size= N)
        arr2 = np.random.uniform(0, high=1, size= N)
        M = 3000
        batch_error_a,batch_inner_product1_a,batch_inner_product2_a,_,_ = batch_feature_deletion_error(Input_dim=N,Output_dim=M,rate = 10,array1=arr1,array2=arr2,mapping_scheme=1)
        print(batch_error_a)
        plt.plot(range(len(batch_error_a)), batch_error_a,color='green')
        plt.plot(range(len(batch_inner_product1_a)), batch_inner_product1_a,color='yellow')
        plt.plot(range(len(batch_inner_product2_a)), batch_inner_product2_a,color='orange')

        batch_error_b,batch_inner_product1_b,batch_inner_product2_b,_,_ = batch_feature_deletion_error(Input_dim=N,Output_dim=M,rate = 10,array1=arr1,array2=arr2,mapping_scheme=2)
        print(batch_error_b)
        plt.plot(range(len(batch_error_b)), batch_error_b,color='red')
        plt.plot(range(len(batch_inner_product1_b)), batch_inner_product1_b,color='blue')
        plt.plot(range(len(batch_inner_product2_b)), batch_inner_product2_b,color='grey')
        plt.show()
        counter += 1

if __name__ == "__main__":
    main()