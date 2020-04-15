from kanren import run, var, fact
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import commutative, associative

add = 'add'
mul = 'mul'

fact(commutative, mul)
fact(commutative, add)
fact(associative, mul)
fact(associative, add)

a, b = var('a'), var('b')

original_pattern = (mul, (add, 5, a), b)

exp1 = (mul, 2, (add, 3, 1))
exp2 = (add,5,(mul,8,1))

print(run(0, (a,b), eq(original_pattern, exp1)))
print(run(0, (a,b), eq(original_pattern, exp2)))