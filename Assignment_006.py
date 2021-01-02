# ---------------------------------------------------------
# ------------  Assignment For Lessons 26 - 32  -----------
# ---------------------------------------------------------

# https: // elzero.org/python-assignments-lesson-from-26-to-32/

# [01]
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = set(my_list)          # Change to set 
unique_list = list(unique_list)     # Change again to back to list
print(unique_list)                  # [1, 2, 3, 4, 5]
print(type(unique_list))            # <class 'list'>
print(unique_list[:-1])             # [1, 2, 3, 4]
print("\n##### End Of Assignment 1 #####\n")

# [002]
nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums | letters)               # {1, 2, 3, 'A', 'B', 'C'}                       
nums.union(letters)
print(nums.union(letters))          # {1, 2, 3, 'A', 'B', 'C'}
nums.update(letters)
print(nums)                         # {1, 2, 3, 'A', 'B', 'C'}      
print("\n##### End Of Assignment 2 #####\n")

# [003
a = {1, 2, 3}
print(a)                            # {1, 2, 3}
a.clear()
print(a)                            # set()
a.update('A', 'B')                  # {'B', 'A'}
a.discard('C')
print(a)
print("\n##### End Of Assignment 3 #####\n")

# [004]
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))   # True
print("\n##### End Of Assignment 4 #####\n")

# [005]
programming_skills = {
  'HTML': '90%',
  'CSS': '80%',
  'JavaScript': '40%',
  'Python': '30%',
}
print(f'{list(programming_skills)[0]} Progress Is {list(programming_skills.values())[0]}') # HTML Progress Is 90% 
print(f'{list(programming_skills)[1]} Progress Is {list(programming_skills.values())[1]}') # CSS Progress Is 80%
print(f'{list(programming_skills)[2]} Progress Is {list(programming_skills.values())[2]}') # JavaScript Progress Is 40%
print(f'{list(programming_skills)[3]} Progress Is {list(programming_skills.values())[3]}') # Python Progress Is 30%

programming_skills.update({'AI': '20%'})
print(f'{list(programming_skills)[4]} Progress Is {list(programming_skills.values())[4]}') # AI Progress Is 20%
