courses =['History', 'Math', 'Physics', 'CompSci']

courses.sort()
nums = [1, 5, 4, 3, 2]
nums.sort()
print(courses)
print(nums)

#                **OUTPUT**
# ['CompSci', 'History', 'Math', 'Physics']
# [1, 2, 3, 4, 5]

#1.min and max
print(min(nums))
print(max(nums))
#                **OUTPUT**
# 1
# 5

#2. reverse
nums.reverse()
print(nums)

#                **OUTPUT**
# [5, 4, 3, 2, 1]

#3. sort in reverse
courses.sort(reverse=True)
print(courses)

#                **OUTPUT**
# ['Physics', 'Math', 'History', 'CompSci']
#4. sorted function
sorted_courses = sorted(courses)
print(sorted_courses)

#                **OUTPUT**
# ['CompSci', 'History', 'Math', 'Physics'] (original list)
# ['CompSci', 'History', 'Math', 'Physics'] (sorted list)
#5. sort in reverse
sorted_courses = sorted(courses, reverse=True)
print(sorted_courses)

#                **OUTPUT**
# ['CompSci', 'History', 'Math', 'Physics'] (original list)
# ['Physics', 'Math', 'History', 'CompSci'] (sorted list)
#6. sort in reverse
sorted_courses = sorted(courses, reverse=False)
print(sorted_courses)

#                **OUTPUT**
# ['CompSci', 'History', 'Math', 'Physics'] (original list)
# ['CompSci', 'History', 'Math', 'Physics'] (sorted list)

#7. sort in reverse
sorted_courses = sorted(courses, reverse=False)
print(sorted_courses)

#                **OUTPUT**
# ['CompSci', 'History', 'Math', 'Physics'] (original list)
# ['CompSci', 'History', 'Math', 'Physics'] (sorted list)