import random

def read_file():
    #file = open("Ver_2_CS170_Fall_2021_LARGE_data__24.txt", "r")
    file = open("Ver_2_CS170_Fall_2021_Small_data__41.txt", "r")
    data = []
    for line in file.readlines():
        data.append([float(i) for i in line.split()])

    print(data[1][1])
    print(data[1][2])
    print(data[1][3])
    print(data[1][4])
    return data

read_file()

#data = [1,2,3,4,5,6,7,8,9,10]

def leave_one_out_cross_validation(data, current_set_of_features, feature_to_add):
    return random.randint(1,10)

def feature_search(data):
    current_set_of_features = []

    for i in range(len(data)):           # dont count first column
        print("On the " + str(i+1) + "th level of the search tree")
        feature_to_add_at_this_level = []
        best_so_far_accuracy = 0

        for j in range(len(data)):
            if data[j] not in current_set_of_features:
                print("--Considering adding the " + str(j+1) + " feature")
                accuracy = leave_one_out_cross_validation(data, current_set_of_features, j+1)

                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = j
        
        current_set_of_features.append(feature_to_add_at_this_level)
        print("On level " + str(i+1) + " I added feature " + str(feature_to_add_at_this_level) +  " to current set\n")

#feature_search(data)

"""
function feature_search_demo(data)

current_set_of_features = []; % Initialize an empty set

for i = 1 : size(data,2) - 1
    disp(['On the ',num2str(i),'the level of the search tree'])
    feature_to_add_at_this_level = [];
    best_so_far_accuracy = 0;

    for k = 1 : size(data,2)-1
        if isempty(intersect(current_set_of_features,k)) % Only consider adding, if not already added.
            disp(['--Considering adding the ', num2str(k),' feature'])
            accuracy = leave_one_out_cross_validation(data,current_set_of_features,k+1);

            if accuracy > best_so_far_accuracy
                best_so_far_accuracy = accuracy;
                feature_to_add_at_this_level = k;
            end
        end
    end

    current_set_of_features(i) = feature_to_add_at_this_level;
    disp(['On level ', num2str(i),' i added feature ', num2str(feature_to_add_at_this_level),' to current set'])
    end
end
"""

"""def leave_one_out_cross_validation(data, current_set, feature_to_add):
    number_correctly_classfied = 0

    for i in range(len(data)):
        object_to_classify = data[i]
        label_object_to_classify = data[i]

        #nearest_neighbor_distance = inf
        #nearest_neighbor_location = inf

        for j in range(len(data)):
            if j != i:
                #distance = sqrt(sum((object_to_classify - data(k,2:end)).^2))
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = j
                    nearest_neighbor_label = data(nearest_neighbor_location, 1)

        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classfied = number_correctly_classfied + 1

    accuracy = number_correctly_classfied / size(len(data))

""""""
function accuracy = leave_one_out_cross_validation(data,current_set,feature_to_add)

number_correctly_classfied = 0;

for i = 1 : size(data,1)
    object_to_classify = data(i,2:end);
    label_object_to_classify = data(i,1);

    nearest_neighbor_distance = inf;
    nearest_neighbor_location = inf;
    for k = 1 : size(data,1)
        if k ~= i
            distance = sqrt(sum((object_to_classify - data(k,2:end)).^2));
            if distance < nearest_neighbor_distance
                nearest_neighbor_distance = distance;
                nearest_neighbor_location = k;
                nearest_neighbor_label = data(nearest_neighbor_location,1);
            end
        end
    end

    if label_object_to_classify == nearest_neighbor_label;
        number_correctly_classfied = number_correctly_classfied + 1;
    end
end

accuracy = number_correctly_classfied / size(data,1);
end
"""

#read_file()