#forloop1

for i in range(5):
	print('Hello',i)

print('------Loop in List------')
friend = ['A','B','C','D','E','F']

for f in friend:
	print(f)
	if (f) == 'A':
		print('Hello A')
	else:
		print('Hello customer') 

print('------Loop in Dictionary------')

friend2 = {'A':'เอ', 'B':'บี', 'C':'ซี'}

# show key
for f in friend2:
	print(f)

# show item
for k,v in friend2.items():
	print('Key:', k)
	print('Value:', v)

# show key only
for f in friend2.keys():
	print(f)

# show value only
for f in friend2.values():
	print(f)

# Need order for lists
for i,f, in enumerate(friend, start=1000): 
	print(i,f)

# Need oder for dictionary 
for i,(k,v) in enumerate(friend2.items()): 
	print(i,k,v)