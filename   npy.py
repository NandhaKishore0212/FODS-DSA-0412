import numpy as np

# Step 1: Create a sample 4x4 NumPy array for demonstration
# Each row = one student, each column = subject: Math, Science, English, History
student_scores = np.array([
    [85, 90, 78, 92],
    [88, 76, 85, 80],
    [90, 85, 82, 88],
    [75, 80, 79, 84]
])

# Step 2: Calculate average score for each subject (column-wise mean)
average_scores = np.mean(student_scores, axis=0)

# Step 3: Determine the index of the highest average score
highest_avg_index = np.argmax(average_scores)

# Step 4: List of subjects for reference
subjects = ['Math', 'Science', 'English', 'History']

# Step 5: Print the results
print("Average scores per subject:")
for subject, avg in zip(subjects, average_scores):
    print(f"{subject}: {avg:.2f}")

print(f"\nSubject with the highest average score: {subjects[highest_avg_index]}")
