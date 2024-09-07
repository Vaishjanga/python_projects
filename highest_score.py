student_scores = [150, 142, 285, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 56, 78, 12, 78, 98, 150, 78, 65,
                  90, 34, 54, 65, 36, 74, 96, 87]
total_score = sum(student_scores)
print(total_score)
minimum_score = min(student_scores)
print(minimum_score)
maximum_score = max(student_scores)
print(maximum_score)

sum_of_score = 0
for totalscore_ in student_scores:
    sum_of_score = sum_of_score+ totalscore_
    #sum_of_score += totalscore_

print(sum_of_score)

for score in student_scores:
    print(score)

max_score = 0
for score in student_scores :
    if score > max_score:
        max_score = score
print(max_score)

min_score = 285
for score in student_scores :
   if score < min_score:
       min_score = score
print(min_score)