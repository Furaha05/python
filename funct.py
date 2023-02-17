def hello():
    print("Today is a Monday")
hello()
def calculate():
    x=45
    y=90
    print(x+y)
calculate()
def majina(fname,lname):
    print(fname+""+lname)
majina("Temina", "Kadenyi")
majina("Karani","Muthami")
majina("Sandra","Baraka")
majina("Furaha","Saida")

def greetings(name, greeting= "Hello"):
    print(greeting +""+ name)
greetings( "Temina" )

def loginfirst (username, display="Welcome"):
    print(display +""+ username)
loginfirst("Joanna")

def maxvalue(a,b,c,d,e,f,g):
    return max(a,b,c,d,e,f,g)
result=maxvalue(12,4,68,21,11,3,9)
print(result)
def minvalue(e,f,g,h,i,j,k,l):
    return min(e,f,g,h,i,j,k,l)
result=minvalue(80,4,2,34,20,11,77,2)
print(result)
def sort_list(lst):
    return sorted(lst)
answer=sort_list([3,9,6,2,7,4,1,5])
print(answer)
def print_numbers(n):
    for i in range(n):
        print(i)
print_numbers(5)