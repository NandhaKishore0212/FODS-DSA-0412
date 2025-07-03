import numpy as np

fuel_efficiency = np.array([22, 25, 30, 28, 35, 40])  
average_efficiency = np.mean(fuel_efficiency)


model_1 = fuel_efficiency[1]  
model_2 = fuel_efficiency[5]  

percentage_improvement = ((model_2 - model_1) / model_1) * 100
print("Average Fuel Efficiency:", average_efficiency, "mpg")
print("Percentage Improvement from Model 1 to Model 2: {:.2f}%".format(percentage_improvement))
