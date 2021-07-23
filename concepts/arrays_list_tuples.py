import array
my_tuple = ('sara', 6, 5, 0.97) #-->Immutable

my_list = ['sara', 6, 5, 0.97] #-->Mutable

my_array = array.array('i', [1,2,3,4])

#
try:
  my_tuple[0]="change"
except Exception as exp:
  print(exp)

#
my_list[0]="change"

print("Tuple: ",my_tuple)
print("List ",my_list)
#

for i in my_array:
  print(i, end='')
