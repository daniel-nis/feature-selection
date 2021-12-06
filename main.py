import random
import math
#import numpy as np
#from scipy.spatial import distance
import copy
import time

def read_file():
    #file = open("Ver_2_CS170_Fall_2021_LARGE_data__24.txt", "r")
    #file = open("Ver_2_CS170_Fall_2021_Small_data__41.txt", "r")
    #file = open("Ver_2_CS170_Fall_2021_Small_data__86.txt", "r")     # EA dataset small
    #file = open("Ver_2_CS170_Fall_2021_LARGE_data__27.txt", "r")     # EA dataset large
    #file = open("Ver_2_CS170_Fall_2021_Small_data__61.txt", "r")     # AT dataset small

    data = []
    for line in file.readlines():
        data.append([float(i) for i in line.split()])

    return data

"""def leave_one_out_cross_validation(data, current_set_of_features, feature_to_add):
    return random.randint(1,10)"""

def feature_search():
    data = read_file()
    features_in_data = len(data[0])

    current_set_of_features = []

    best_subset = []
    top_accuracy = 0
    decreasing_accuracy_count = 0

    for i in range(1, features_in_data):           # dont count first column
        print("On level " + str(i) + " of the search tree")
        feature_to_add_at_this_level = []
        best_so_far_accuracy = 0

        for j in range(1, features_in_data):
            if j not in current_set_of_features:
                print("--Considering adding the " + str(j) + " feature")
                accuracy = leave_one_out_cross_validation(data, current_set_of_features, j)

                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = j
        
        current_set_of_features.append(feature_to_add_at_this_level)
        print("On level " + str(i) + " I added feature " + str(feature_to_add_at_this_level) +  " to current set\n")

        if top_accuracy < best_so_far_accuracy:
            top_accuracy = best_so_far_accuracy
            best_subset = copy.deepcopy(current_set_of_features)
        else:
            decreasing_accuracy_count += 1

        if decreasing_accuracy_count > 4:
            break

    print("The best subset is: ")
    print(best_subset)
    print("Which returns an accuracy of: " + str(top_accuracy))
    #for k in range(len(best_subset)):
    #    print(str(best_subset[k]))
    #print("Which returns an accuracy of: " + top_accuracy)

def leave_one_out_cross_validation(data, current_set, feature_to_add):
#def leave_one_out_cross_validation(current_set, feature_to_add):
    data = read_file()

    feature_list = copy.deepcopy(current_set)
    feature_list.append(feature_to_add)

    number_correctly_classfied = 0

    for i in range(len(data)):
        object_to_classify = data[i]
        label_object_to_classify = data[i][0]       # labels from first column

        nearest_neighbor_distance = math.inf
        nearest_neighbor_location = math.inf

        for j in range(len(data)):
            if j != i:
                lp = copy.deepcopy(data[j])
                this_distance = 0
                for a in range(len(feature_list)):
                    feats = feature_list[a]
                    this_distance += math.sqrt((object_to_classify[feats] - lp[feats]) ** 2)

                if this_distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = this_distance
                    nearest_neighbor_location = j
                    nearest_neighbor_label = data[nearest_neighbor_location][0]

        #print("Object " + str(i) + " is class " + str(label_object_to_classify))
        #print("Its nearest neighbor is " + str(nearest_neighbor_location) + " which is class " + str(nearest_neighbor_label))

        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classfied = number_correctly_classfied + 1

    accuracy = number_correctly_classfied / len(data)
    print(accuracy)
    return accuracy


def main():
    start_time = time.time()

    feature_search()
    #leave_one_out_cross_validation([26, 27], 31)   # EA large

    end_time = time.time()
    print(f"It took {end_time-start_time:.2f} seconds to compute")

main()

#leave_one_out_cross_validation([7, 4], 9)  # AT small
#leave_one_out_cross_validation([3, 8], 2)   # EA small
#leave_one_out_cross_validation([26, 27], 31)   EA large