#WAP to find the total number of people above the age of 18
d={ "keerti":20,
    "aishuu":17,
    "nagu":16,
    "karthikk":24,
    "chandru":21,
    "guru":23,
    "jyothi":22,
    "chandana":17,}
print(d)
l=d.values()
e=[]
for i in l:
    if i>18:
        e.append(i)
n=len(e)
print('number of peoples,age above 18:-',n)