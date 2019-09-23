import numpy as np
import random

class mapper:
    def __init__(self, input_dim = 50, out_dim = 15):
        self.input_dimension = input_dim
        self.output_dimension = out_dim
        self.bits = np.random.randint(-1, high= 1, size= input_dim)

        print ("Generating Mapping. Please wait")

        for i in range(self.bits.size):
            if self.bits[i] == 0:
                self.bits[i] = 1

        self.map = np.random.randint(input_dim)
        self.feature_counter = []
        for i in range(out_dim):
            self.feature_counter.append([])

        for i in range(input_dim):
            alpha = self.map[i]
            self.feature_counter[alpha].append(i)
        print ("Mapping generated")
        print ("Mapping :",self.map)
        print ("Feature :",self.feature_counter)

        #print("Initializing...\n", "Bits:", self.bits, "\nMap:", self.map)

    def insert_feature(self, position=0):
        print ("Inserting new feature at the ",position,"of data.")
        if position <= self.input_dimension:
            self.input_dimension += 1
            self.bits = np.insert(self.bits, position, (random.randint(0,1)-0.5)*2)
            alpha = random.randint(0,self.output_dimension-1)
            new_feature_vector = np.zeros((self.output_dimension),dtype=int)
            new_feature_vector[alpha]=1
            self.map = np.insert(self.map, position,new_feature_vector,axis=0)
            # print (self.map)
            updated_feature_counter_array = []
            for i in range(self.input_dimension):
                if self.map[i][alpha] == 1:
                    updated_feature_counter_array.append(i)
            self.feature_counter[alpha] = updated_feature_counter_array
        else :
            print("Feature position is incorrect !")
        print("Inserting New Feature at position:", position)
        print("Bits:", self.bits)
        print("Map:", self.map)
        print("feature_counter :",self.feature_counter)

    def delete_feature(self, position=0):
        if position < self.input_dimension:
            beta=0
            for i in range(len(self.map[position])):
                if self.map[position][i] == 1:
                    beta = i
                    break;
            # print ("beta:",beta)
            self.input_dimension -= 1
            self.bits = np.delete(self.bits, position)
            self.map = np.delete(self.map, position,axis=0)

            updated_feature_counter_array = []
            for i in range(self.input_dimension):
                if self.map[i][beta] == 1:
                    updated_feature_counter_array.append(i)
            self.feature_counter[beta] = updated_feature_counter_array

            # print (self.feature_counter[beta])


        else :
            print("Feature position is incorrect !")
        print("Deleted Index:", position)
        # print("Maping Changed for position:", alpha)
        print("Bits:", self.bits)
        print("Map:", self.map)
        print("feature_counter :",self.feature_counter)

    def batch_insert_feature(self,batch_positions=[]):
        for i in range(len(batch_positions)):
            self.insert_feature(position=batch_positions[i])

    def batch_delete_feature(self,batch_positions=[]):
        for i in range(len(batch_positions)):
            self.delete_feature(position=batch_positions[i])

    def dimension_reduction(self, input_array):
        output_array = np.zeros(self.output_dimension, dtype=float)

        for i in range(self.input_dimension):
            if self.map[i] != -1:
                output_array[self.map[i]] += (self.bits[i])*input_array[i]

        return output_array

    def input_dim(self):
        return self.input_dim

    def output_dim(self):
        return self.output_dim

    def get_feature_counter(self):
        return self.feature_counter

    def get_feature_count(self):
        feature_count = []
        for feature in self.feature_counter:
            feature_count.append(len(feature))
        return feature_count

    def get_mapping_info(self):
        print ("Input Features:",self.input_dimension)
        print ("Output Features:",self.output_dimension)
        print ("Features Distribution:",self.get_feature_counter())
        print ("Features Distribution Count:",self.get_feature_count())





def main():
    # #print (np.random.randint(0,high=1,size=50))
    demomap = mapper(input_dim=5,out_dim=2)
    demomap.insert_feature()
    demomap.insert_feature()
    demomap.insert_feature()
    demomap.insert_feature()
    demomap.delete_feature(position=3)
    demomap.insert_feature()
    print (demomap.get_feature_count())
    demomap.get_mapping_info()
    temp = np.random.randint(-256, 256, demomap.input_dimension)
    #print(temp)

    #print(demomap.dimension_reduction(temp))

if __name__ == "__main__":
    main()