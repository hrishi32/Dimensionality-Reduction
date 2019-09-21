from .mapper import mapper, np
from basic_operator import operator
# import random

class batch_operator:
    def __init__(self, input_dim=50, output_dim = 15):
        self.operator = operator(input_dim=input_dim, output_dim=output_dim)
       


    def insert_feature(self, batch_position=[], batch_array1 = [], batch_array2 = [], batch_value1 = [], batch_value2 = []):
        for i in range(batch_position.size):
            self.operator.insert_feature(position=batch_position[i], array1 = batch_array1[i], array2 = batch_array2[i], value1 = batch_value1[i], value2 = batch_value2[i])



    def delete_feature(self, batch_position=[], batch_array1 = [], batch_array2 = []):
        for i in range(batch_position.size):
            self.operator.delete_feature(position=batch_position[i], array1 = batch_array1[i], array2 = batch_array2[i])


    def array_normalization(self, input_array):
        array_norm = np.linalg.norm(input_array)
        result = np.zeros(input_array.size, dtype=float)
        for i in range(input_array.size):
            result[i] = (1.0*input_array[i])/array_norm

        return result

    def batch_inner_product(self, input_array1, input_array2):

        for i in range(batch_array1.)


        input_array1 = self.array_normalization(input_array1)
        input_array2 = self.array_normalization(input_array2)

        output_array1 = self.mapping.dimension_reduction(input_array1)
        output_array2 = self.mapping.dimension_reduction(input_array2)

        #print("Output1", output_array1)
        #print("Output2", output_array2)

        result1, result2 = 0, 0
        
        for i, j in zip(input_array1, input_array2):
            result1+=(i*j)

        for i, j in zip(output_array1, output_array2):
            result2+=(i*j)

        #print("Input Inner Product:", result1)
        #print("Output Inner Product:", result2)

        return result1, result2