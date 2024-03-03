## Minimum Cost Method for Transportation Problems
This Python project implements the Minimum Cost Method to solve transportation problems. It utilizes the NumPy library for efficient matrix operations.

The Minimum Cost Method is a technique employed in optimization problems, specifically in the field of operations research, to determine the most cost-effective allocation of resources. This method is commonly used in transportation and assignment problems.
The primary goal of the Minimum Cost Method is to find an initial feasible solution by iteratively selecting the lowest cost cells in a cost matrix. These cells represent the optimal assignments between suppliers and demanders in a transportation or assignment problem.

## Features
-Cell Assignments: Assigns costs to cells in the transportation matrix.
-Supply and Demand Assignment: Takes user input for supply and demand quantities.
-Optimal Assignments: Finds optimal assignments using the Minimum Cost Method.
-Error Handling: Includes error handling to ensure valid user inputs for cost values.

## Usage
1. Enter the number of suppliers and demanders.
2. Input the transportation costs for each cell.
3. Specify the supply quantities from each supplier and demand quantities from each demander.
4. The code will output the initial solution and total cost, along with a detailed list of assignments made, specifying the cells and quantities assigned.
