def summation(*args):
     summ = 0;
     for el in args:
          summ += el;
     print(summ);

summation(1,2,3,4,5,6)
# summation([1,2,3,4,5,6]); Error
summation(*[1,2,3,4,5,6]);

def test(*args):
     print(args, type(args))

test(1,2,3,4,5,6,7,8);
test([1,2,3,4,5,6,7,8]);

