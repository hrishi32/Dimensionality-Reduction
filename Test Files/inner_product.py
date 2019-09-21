from mapper import mapper, np
# import random

class operator:
    def __init__(self, input_dim=50, output_dim = 15):
        self.mapping = mapper(input_dim=input_dim, out_dim=output_dim)

    def insert_feature(self, position=0):
        self.mapping.insert_feature(position=position)

    def delete_feature(self, position=0):
        self.mapping.delete_feature(position=position)

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

def main():
    input_size, output_size = 50000, 2000
    demo_operator = operator(input_dim=input_size, output_dim=output_size)

    arr1 = np.random.randint(0, high=50, size=input_size)
    arr2 = np.random.randint(0, high=50, size=input_size)

    #print("Array1:", arr1)
    #print("Array2:", arr2)

    demo_operator.inner_product(arr1, arr2)

    arr1 = np.insert(arr1, 1, 2)
    arr2 = np.insert(arr2, 1, 3)

    demo_operator.insert_feature(1)

    demo_operator.inner_product(arr1, arr2)

    arr1 = np.delete(arr1, 0)
    arr2 = np.delete(arr2, 0)

    demo_operator.delete_feature(0)

    demo_operator.inner_product(arr1, arr2)

if __name__ == "__main__":
    main()
