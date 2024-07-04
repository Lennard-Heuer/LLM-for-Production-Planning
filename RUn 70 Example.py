
import numpy as np
import pulp

def aggregate_production_planning(demand, capacity, yield_losses, workforce, raw_materials_cost, short_term_labor_cost):
    # Define the variables
    n_products = len(demand)
    n_time_periods = 12
    production_plan = np.zeros((n_products, n_time_periods))
    workforce_plan = np.zeros((n_time_periods,))
    raw_materials_consumption = np.zeros((n_products, n_time_periods))
    short_term_labor_consumption = np.zeros((n_products, n_time_periods))
    # Define the objective function
    objective_function = np.sum(np.multiply(production_plan, raw_materials_cost) + np.multiply(short_term_labor_consumption, short_term_labor_cost))
    # Define the constraints
    constraints = [
    np.sum(production_plan) <= capacity, # Capacity constraint
    np.sum(production_plan, axis=1) >= demand, # Demand constraint
    np.sum(raw_materials_consumption, axis=1) <= yield_losses, # Yield loss constraint
    np.sum(short_term_labor_consumption, axis=1) <= workforce, # Workforce constraint
    production_plan >= 0, # Non-negativity constraint
    workforce_plan >= 0 # Non-negativity constraint
    ]
    # Solve the linear program
    solver = pulp.SolverFactory('glpk')
    prob = pulp.LpProblem("Aggregate Production Planning", pulp.LpMaximize)
    prob += objective_function
    prob += constraints
    solver.solve(prob)
    # Print the results
    print("Optimal Production Plan:")
    print(production_plan)
    print("Optimal Workforce Plan:")
    print(workforce_plan)
# Example usage
demand = [100, 150, 200, 250, 300]
capacity = 1000
yield_losses = [5, 10, 15, 20, 25]
workforce = 100
raw_materials_cost = [10, 15, 20, 25, 30]
short_term_labor_cost = [5, 10, 15, 20, 25]



raw_materials_cost = np.array(raw_materials_cost)[:, np.newaxis]  # Reshape to (5, 1)
short_term_labor_cost = np.array(short_term_labor_cost)[:, np.newaxis]  # Reshape to (5, 1)


aggregate_production_planning(demand, capacity, yield_losses, workforce, raw_materials_cost, short_term_labor_cost)

