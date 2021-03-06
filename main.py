import math
import copy
import time
import multiprocessing as mp

# asks user to select a search algorithm
def search_selection():
    print("Enter the number associated with an algorithm to select it:\n"
                + "1. Forward Selection\n"
                + "2. Backward Elimination")
    selection = input("Enter number: ")
    print()
    return selection

# reads in the file and returns the data within it
def read_file():
    #file = open("Ver_2_CS170_Fall_2021_LARGE_data__24.txt", "r")
    file = open("Ver_2_CS170_Fall_2021_Small_data__41.txt", "r")
    #file = open("Ver_2_CS170_Fall_2021_Small_data__86.txt", "r")     # EA dataset small
    #file = open("Ver_2_CS170_Fall_2021_LARGE_data__27.txt", "r")     # EA dataset large
    #file = open("Ver_2_CS170_Fall_2021_Small_data__61.txt", "r")     # AT dataset small

    data = []
    for line in file.readlines():
        data.append([float(i) for i in line.split()])

    return data

# feature search algorithm - contains forward selection (as provided by professor) and backward eliminination
# forward selection starts with an empty feature list and adds the feature that yields the greatest accuracy at each level
# backward elimination starts with every feature and removes the one that allows the list to have a higher accuracy at each level
def feature_search(selection):
    data = read_file()
    features_in_data = len(data[0])

    current_set_of_features = []

    best_subset = []
    top_accuracy = 0
    decreasing_accuracy_count = 0

    if selection == "1":      # forward selection
        for i in range(1, features_in_data):           # dont count first column
            print("On level " + str(i) + " of the search tree")
            feature_to_add_at_this_level = []
            best_so_far_accuracy = 0

            for j in range(1, features_in_data):
                if j not in current_set_of_features:
                    print("--Considering adding the " + str(j) + " feature")
                    accuracy = leave_one_out_cross_validation(data, current_set_of_features, j, selection)

                    if accuracy > best_so_far_accuracy:
                        best_so_far_accuracy = accuracy
                        feature_to_add_at_this_level = j
        
            current_set_of_features.append(feature_to_add_at_this_level)
            print("On level " + str(i) + " I added feature " + str(feature_to_add_at_this_level) +  " to current set\n")

            print("The current set is: ")
            print(current_set_of_features)
            print("and has accuracy " + str(best_so_far_accuracy) + "\n")
            
            # find the subset that had the best accuracy
            if top_accuracy < best_so_far_accuracy:
                top_accuracy = best_so_far_accuracy
                best_subset = copy.deepcopy(current_set_of_features)
            else:
                decreasing_accuracy_count += 1
            
            # algorithm takes too long to run, so I made a greedy choice, 
            # as the accuracy ends up always dropping off for every extra feature after 2-3 features
            if features_in_data > 15:
                if decreasing_accuracy_count > 4:
                    break

    if selection == "2":
        for i in range(1, features_in_data):        # dont count first column
            current_set_of_features.append(i)

        for i in range(1, features_in_data):           # dont count first column
            print("On level " + str(i) + " of the search tree")
            features_removed = []
            feature_to_remove_at_this_level = []
            best_so_far_accuracy = 0


            for j in range(1, features_in_data):
                if j in current_set_of_features:
                    print("--Considering removing the " + str(j) + " feature")
                    accuracy = leave_one_out_cross_validation(data, current_set_of_features, j, selection)

                    if accuracy > best_so_far_accuracy:
                        best_so_far_accuracy = accuracy
                        feature_to_remove_at_this_level = j
        
            current_set_of_features.remove(feature_to_remove_at_this_level)
            features_removed.append(feature_to_remove_at_this_level)
            print("On level " + str(i) + " I removed feature " + str(feature_to_remove_at_this_level) +  " from current set\n")

            # find the subset that had the best accuracy
            if top_accuracy < best_so_far_accuracy:
                top_accuracy = best_so_far_accuracy
                best_subset = copy.deepcopy(current_set_of_features)
            else:
                decreasing_accuracy_count += 1

            print("The current set is: ")
            print(current_set_of_features)
            print("and has accuracy " + str(best_so_far_accuracy) + "\n")

    print("The best subset is: ")
    print(best_subset)
    print("Which returns an accuracy of: " + str(top_accuracy))

# leave one out cross validation function, as provided by professor
def leave_one_out_cross_validation(data, current_set, feature_to_modify, selection):

    feature_list = copy.deepcopy(current_set)

    selection = "1"
    if selection == "1":
        feature_list.append(feature_to_modify)

    if selection == "2":
        feature_list.remove(feature_to_modify)

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
    print("Accuracy would be: " + str(accuracy))
    return accuracy


def main():
    start_time = time.time()

    selection = search_selection()
    feature_search(selection)

    end_time = time.time()
    print(f"It took {end_time-start_time:.2f} seconds to compute")

main()