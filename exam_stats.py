grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

#prints all of the grades in the list
def print_grades(grades_input):
  for grade in grades_input:
    print grade

#sums a list of grades
def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
#averages the grades 
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

#finds the variance of the grades 
def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score) ** 2
  return variance / len(scores)

#finds standard deviation based on variance
def grades_std_deviation(variance):
  return variance ** 0.5

#use cases
print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
variance = grades_variance(grades)
print grades_std_deviation(variance)
  