#!/usr/bin/env python
# coding: utf-8

# # Python Task 1

# # Question-1 (Car Matix Generation)

# In[30]:


import pandas as pd

def generate_car_matrix(matrix):
    """
    Creates a DataFrame for id combinations.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
# Write your logic here
matrix = matrix.pivot(index='id_1', columns='id_2', values='car').fillna(0)
for idx in matrix.index:
    matrix.at[idx, idx] = 0
    return matrix

file_path = 'dataset-1.csv'
result_matrix = generate_car_matrix(pd.read_csv(file_path))
matrix


# # Question 2: Car Type Count Calculation
# 

# In[27]:


import pandas as pd

def get_type_count(df):
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
# Write your logic here
df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                        labels=['low', 'medium', 'high'], right=False)
type_counts = df['car_type'].value_counts().to_dict()
sorted_type_counts = dict(sorted(type_counts.items()))
return sorted_type_counts

file_path = 'dataset-1.csv'
df = pd.read_csv(file_path)
type_counts = get_type_count(df)
print(type_counts)
df


# # Question 3: Bus Count Index Retrieval

# In[28]:


import pandas as pd

def get_bus_indexes(df):
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
# Write your logic here
bus_mean = df['bus'].mean()
bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()
sorted_bus_indexes = sorted(bus_indexes)
return sorted_bus_indexes

file_path = 'dataset-1.csv'
df = pd.read_csv(file_path)
bus_indexes = get_bus_indexes(df)
print(bus_indexes)
df


# # Question 4: Route Filtering

# In[32]:


import pandas as pd

def filter_routes(df):
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
# Write your logic here
# Calculate the average 'truck' values for each route
avg_truck_per_route = df.groupby('route')['truck'].mean()
# Filter routes where the average 'truck' value is greater than 7
selected_routes = avg_truck_per_route[avg_truck_per_route > 7].index.tolist()
# Sort the list of selected routes
sorted_selected_routes = sorted(selected_routes)
return sorted_selected_routes

# Assuming you have a DataFrame called 'your_dataframe' with columns 'route' and 'truck'
file_path = 'dataset-1.csv'
df = pd.read_csv(file_path)
selected_routes = filter_routes(df)
print(selected_routes)
df


# # Question 5: Matrix Value Modification

# In[51]:


def multiply_matrix(matrix):
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Apply custom conditions and round the values to 1 decimal place
    modified_matrix = matrix.applymap(lambda x: 0.75 * x if x > 20 else 1.25 * x).round(1)

    return modified_matrix
# Write your logic here

file_path = 'dataset-1.csv'
df = pd.read_csv(file_path)

# Generating car matrix
car_matrix = generate_car_matrix(df)

# Applying custom conditions and rounding values
modified_car_matrix = multiply_matrix(car_matrix)

print("Original Car Matrix:")
print(car_matrix)
print("\nModified Car Matrix:")
modified_car_matrix


# In[ ]:




