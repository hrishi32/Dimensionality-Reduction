from mapper import mapper
import numpy as np
from mapper2 import mapper as mapper2
from mapper3 import mapper as mapper3
# import random

class operator:
    def __init__(self, input_dim=50, output_dim = 15,mapping_scheme=1):
        if mapping_scheme == 1:
            self.mapping = mapper(input_dim=input_dim, out_dim=output_dim)
        elif mapping_scheme == 2:
            self.mapping = mapper2(input_dim=input_dim, out_dim=output_dim)
        elif mapping_scheme == 3:
            self.mapping = mapper3(input_dim=input_dim, out_dim=output_dim)


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

        flags = []
        for i in range(self.mapping.input_dimension):
            flags.append([])

        for i in range(len(batch_positions)):
            flags[batch_positions[i]] = [batch_value1[i],batch_value2[i]]


        i = 0
        factor = 0
        old_dim = self.input_dimension
        last_insertion = 0
        # print ("start")
        while i < old_dim:

            print (i,flags[i])
            if flags[i] == 1 and last_insertion == 0 :
                self.insert_feature(i+factor)
                factor+=1
                last_insertion +=1
                # flags = np.insert(flags, i, 0)
                # i += 1
            elif flags[i] == 1:
                self.insert_feature(i+factor-last_insertion)
                factor+=1
                last_insertion+=1
            else:
                last_insertion = 0
            
            i+=1
        
            # self.insert_feature(position=batch_positions[i])

        i = 0
        # print ("start")
        while i < self.input_dimension:

            print (i,flags[i])
            if len(flags[i])!=0:
                flags.insert(i, [])
                array1 = np.insert(array1, i, flags[i][0] )
                array2 = np.insert(array2, i, flags[i][1])

    
                i += 1
            i+=1
        return array1,array2

    def batch_delete_feature(self,batch_positions=[],array1=[],array2=[]):
        self.mapping.batch_delete_feature(batch_positions=batch_positions)
        for i in range(len(batch_positions)):
            array1 = np.delete(array1, batch_positions[i])
            array2 = np.delete(array2, batch_positions[i])
        return array1,array2

    def array_normalization(self, input_array):
        array_norm = np.linalg.norm(input_array)
        print ("array norm:",array_norm)
        result = np.zeros(input_array.size, dtype=float)
        for i in range(input_array.size):
            result[i] = (1.0*input_array[i])/array_norm

        return result

    def inner_product(self, input_array1, input_array2):
        # input_array1 = self.array_normalization(input_array1)
        # input_array2 = self.array_normalization(input_array2)

        # print ("norm array1 :",input_array1)
        # print ("norm array2 :",input_array2)

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