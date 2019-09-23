from Object_Files.mapper import mapper, np
from Object_Files.mapper2 import mapper as mapper2
# import random

class operator:
    def __init__(self, input_dim=50, output_dim = 15,mapping_scheme=1):
        if mapping_scheme == 1:
            self.mapping = mapper(input_dim=input_dim, out_dim=output_dim)
        elif mapping_scheme == 2:
            self.mapping = mapper2(input_dim=input_dim, out_dim=output_dim)


    def insert_feature(self, position=0, array1 = [], array2 = [], value1 = 0, value2 = 0):
        self.mapping.insert_feature(position=position)
        array1 = np.insert(array1, position, value1)
        array2 = np.insert(array2, position, value2)
        return array1,array2

    def delete_feature(self, position=0, array1 = [], array2 = []):
        self.mapping.delete_feature(position=position)
        array1 = np.delete(array1, position)
        array2 = np.delete(array2, position)
        return array1, array2

    def batch_insert_feature(self,batch_positions=[],array1=[],array2=[],batch_value1=0,batch_value2=0):
        self.mapping.batch_insert_feature(batch_positions=batch_positions)
        for i in range(len(batch_positions)):
            array1 = np.insert(array1, batch_positions[i], batch_value1[i])
            array2 = np.insert(array2, batch_positions[i],batch_value2[i])
        return array1,array2

    def batch_delete_feature(self,batch_positions=[],array1=[],array2=[]):
        self.mapping.batch_delete_feature(batch_positions=batch_positions)
        for i in range(len(batch_positions)):
            array1 = np.delete(array1, batch_positions[i])
            array2 = np.delete(array2, batch_positions[i])
        return array1,array2

    def array_normalization(self, input_array):
        array_norm = np.linalg.norm(input_array)
        result = np.zeros(input_array.size, dtype=float)
        for i in range(input_array.size):
            result[i] = (1.0*input_array[i])/array_norm

        return result

    def inner_product(self, input_array1, input_array2):
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