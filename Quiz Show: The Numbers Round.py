import random
import itertools

# Generate our target and our ingredients 

target = random.randint(100,1000)
print(f'Target: {target}')

large_nums = [25,50,75,100]
small_nums = [1,2,3,4,5,6,7,8,9,10]

n_large = random.randint(0,4)
n_small = 6-n_large

large_ings = []
small_ings = []

i = 0
while i < n_large:
    pick = random.choice(large_nums)
    large_nums.remove(pick)
    large_ings.append(pick)
    i+=1

i = 0
while i < n_small:
    pick = random.choice(small_nums)
    small_nums.remove(pick)
    small_ings.append(pick)
    i+=1

ings = tuple(large_ings + small_ings)
print(f'Ingredients: {ings}')

# Gather operation permutations with repitition

operations = ('*','+','/','-')

j = 1
op_perms = []
while j < 6:
    for i in itertools.product(operations, repeat = j):
        op_perms.append(i)
    j += 1

# Gather ingredients permutations without repitition

j = 2
num_perms = []
while j <= 6:
    for i in itertools.permutations(ings, j):
        num_perms.append(i)
    j += 1

# Weave together ingredients and operations permutations

perms = []
for nums in num_perms:
    for ops in op_perms:
        if len(nums) == len(ops)+1:
            nums = list(nums)
            ops = list(ops)
            ops.extend("E")
            lst = list(itertools.chain.from_iterable(zip(nums, ops)))[:-1] 
            perms.append(lst)

# Convert permutation lists to expression strings

expressions = []
for perm in perms:
    expressions.append(' '.join(str(item) for item in perm))

# Evaluate each expression and compare to the target

solutions = 0
for exp in expressions: 
    if eval(exp) == target:
        solutions += 1
        print(f"Possible answer: {exp} = {target}")
print(f"\n{solutions} answers found\n")

