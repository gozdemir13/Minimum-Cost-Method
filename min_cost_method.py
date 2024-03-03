import numpy as np 

# Function to assign costs to cells in the matrix
def CellAssignment(source_rows, destination_columns, matrix_one_dim):
    for i in range(0, source_rows):
        r = i
        for j in range(0, destination_columns): 
             # While loop for error handling, ensures the user enters a valid cost value
             while True:
                try:
                    cell_value = int(input("Please enter the cost of cell [{},{}] :".format(r, j)))
                    if cell_value < 0:
                        print("Error: Cost value cannot be negative. Please enter a positive value.")
                    else:
                        matrix[r, j] = cell_value
                        matrix_one_dim.append(cell_value)
                        break
                except ValueError:
                    print("Error: Please enter a valid number.")

# Function to assign supply and demand quantities         
def SupplyDemandAssignment(source_rows, destination_columns):
    """
    This function takes the number of rows and columns as input.
    It then iterates through each supplier and demander, taking user input for their respective quantities.
    """
    for i in range(0, source_rows):
        supply_value_column[i, 0] = int(input("Please enter the quantity of supply from the {}. supplier: ".format(i + 1)))


    for i in range(0, destination_columns):
        demand_value_row[0, i] = int(input("Please enter the demand quantity for the {}. demander: ".format(i + 1)))

# Initialize the lists and matrices
        
# List to store one-dimensional representation of the matrix
matrix_one_dim = []
source_rows = int(input("Enter the number of suppliers: "))
destination_columns = int(input("Enter the number of demanders: "))

# 2D matrix to store costs
matrix = np.zeros((source_rows, destination_columns)) 

# Column vector for supply values
supply_value_column = np.zeros((destination_columns + 1, 1))

# Row vector for demand values
demand_value_row = np.zeros((1, source_rows + 1))

print("____ASSIGNMENT OF CELLS____")
# Call the function to assign costs to cells in the matrix
CellAssignment(source_rows, destination_columns, matrix_one_dim)

print("____ASSIGNMENT OF SUPPLY AND DEMAND QUANTITIES____")
# Call the function to assign supply and demand quantities
SupplyDemandAssignment(source_rows, destination_columns)

# Initialize variables for the main algorithm
total_cost = 0
assignments_made = []
starting_row = 0
starting_column = 0
i = 0
remaining_total_supply = int(supply_value_column.sum())
remaining_total_demand = int(demand_value_row.sum())
matrix_one_dim.sort()
sizeArray = len(matrix_one_dim)
offsetX = 0
offsetY = 0

a1 = np.array([])
a2 = np.array([])

# Main algorithm to find optimal assignments
while remaining_total_demand != 0 and remaining_total_supply != 0 and i < sizeArray:
    z = np.where(matrix == matrix_one_dim[i])

    # Update offset values by checking coordinates
    if len(z[0]) > 0 and np.array_equal(z[0], a1):
        offsetX += 1
    else:
        offsetX = 0

    if len(z[1]) > 0 and np.array_equal(z[1], a2):
        offsetY += 1
    else:
        offsetY = 0

    # Storing updated coordinates
    a1 = z[0]
    a2 = z[1]

    
    # Update coordinates with offset values
    if 0 + offsetX < len(z[0]):
        a = z[0][0 + offsetX]
    else:
        a = 0

    if 0 + offsetY < len(z[1]):
        b = z[1][0 + offsetY]
    else:
        b = 0

    # Check supply and demand conditions for cost assignment
    if supply_value_column[a, 0] >= demand_value_row[0, b]:

        # If demand and supply quantities are zero, proceed to the next iteration
        if demand_value_row[0, b] == 0 and supply_value_column[a, 0] == 0:
            i += 1
            continue
        # Calculate transportation cost and add it to the total cost
        total_cost += matrix[a, b] * demand_value_row[0, b]
        assignments_made.append("matrix[{},{}] -> {}".format(a, b, demand_value_row[0, b]))

        # Update demand and supply quantities
        supply_value_column[a, 0] -= demand_value_row[0, b]
        demand_value_row[0, b] -= demand_value_row[0, b]

        # Update total demand and supply quantities
        remaining_total_demand -= demand_value_row[0, b]
        remaining_total_supply -= demand_value_row[0, b]

    else:
        # If supply quantity is zero, proceed to the next iteration
        if supply_value_column[a, 0] == 0:
            i += 1
            continue

        # Calculate transportation cost and add it to the total cost   
        total_cost += matrix[a, b] * supply_value_column[a, 0]
        assignments_made.append("matrix[{},{}] -> {}".format(a, b, supply_value_column[a, 0]))
       
        # Update demand and supply quantities
        demand_value_row[0, b] -= supply_value_column[a, 0]
        supply_value_column[a, 0] -= supply_value_column[a, 0]
         
        # Update total demand and supply quantities
        remaining_total_demand -= supply_value_column[a, 0]
        remaining_total_supply -= supply_value_column[a, 0]

    i += 1

# Print the assignments
print("---------ASSIGNMENTS MADE-------- ")
for i in range(len(assignments_made)):
    print(assignments_made[i])

# print the initial feasible solution.
print("------------TOTAL COST-----------")
print(total_cost)
