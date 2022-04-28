import operator
d={1:2,3:4,4:3,2:1,0:0}
print('original dictionary:',d)
sorted_d=sorted(d.items(),key=operator.itemgetter(1))
print('dictionary in ascending order by value:',sorted_d)
sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
print('dictionary in decending order by value:',sorted_d)

def sort_dict_by_value(d,reverse=False):
    return dict(sorted(d.items(),key=lambda x:x[1],reverse=reverse))
print("[original dictionary elements:")
colors={'red':1,'green':3,'black':5,'white':2,'pink':4}
print(colors)
print("\nsort(ascending) the said dictionary elements by value:")
print(sort_dict_by_value(colors))
print("\nsort(descending) the said dictionary elements by value:")
print(sort_dict_by_value(colors,True))

# python program to add a key to a dictionary.

d={0:10,1:20}
print(d)
d.update({2:30})
print(d)

# python program to concatenate following dictionaries to create a new one.

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1,dic2,dic3):dic4.update(d)
print(dic4)

# python program to check if a given key already exists in a dictionary.

d={1:10,2:20,3:30,4:40,5:50,6:60}
def is_key_present(x):
    if x in d:
        print('key is present in the dictionary')
    else:
        print('key is not present in the dictionary')
    is_key_present(5)
    is_key_present(9)

def key_in_dict(d,key):
    return(key in d)
students={
    'theodore':19,
    'roxanne':22,
    'mathew':21,
    'betty':20
}
print("\noriginal dictionary elements:")
print(students)
print(key_in_dict(students,'roxanne'))
print(key_in_dict(students,'gina'))