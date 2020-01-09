import sys
from operator import sub

def parsing_error(strErr):
	print("Parsing error :", strErr)
	sys.exit()

def my_is_float(val):
	try:
		float(val)
	except ValueError:
		return False
	return True

def print_too_high(val) :
	print("Polynomial degree:", val)
	print("The polynomial degree is stricly greater than 2, I can't solve.")
	sys.exit()

def parse_tab(tab) :
	coef = 1;
	ind = 0
	i = 0
	eq = [0, 0, 0]

	while i < len(tab) :

		if tab[i] in ['+', '-']:
			eq[ind] += coef
			ind = 0
			if tab[i] == '+':
				coef = 1
			elif tab[i] == '-':
				coef = -1
			else :
				parsing_error("Coefficent problem.")
		elif tab[i] == '*' :
			i = i
		elif my_is_float(tab[i]):
			coef *= float(tab[i])
		elif 'X^' in tab[i] and tab[i][0] == 'X':
			if my_is_float(tab[i].replace("X^", "")) == False:
				parsing_error("Exposant problem.")
			exp = int(float(tab[i].replace("X^", "")))
			if exp in [0, 1, 2]:
				ind = exp
			else:
				print_too_high(exp)
				return False
		else :
			parsing_error("Number Problem.")
		i += 1
	eq[ind] += coef
	return eq

def get_reduced_form(resultTab) :
	finalEq = ""
	for ind, coef in enumerate(resultTab):
		if coef == 0:
			continue
		if ind != 0:
			if coef < 0:
				finalEq += " - "
				coef *= -1
			else:
				finalEq += " + "
		finalEq += str(coef) + " * X^" + str(ind)
	if finalEq == "":
		finalEq = "0"
	finalEq += " = 0"
	return finalEq

def any_solution():
	print("This equation has no solution")
	pass

def all_solution():
	print("All values of X are solutions")
	pass

#Babylonian method
def my_sqrt(value):
	precision = 0.000001
	s = value
	while (s - (value / s) > precision) :
		s = (s + (value / s)) / 2
	return s
	
def resolve_first_degree(arr):
	sol = -1 * arr[0] / arr[1]
	print("The solution is:")
	print(sol)
	pass

def resolve_second_degree(arr):
	discr = (arr[1] * arr[1]) - (4 * arr[0] * arr[2])
	if (discr < 0) :
		print("The discriminent is negative so :")
		any_solution()
	elif (discr == 0) :
		sol = -arr[1] / (2 * arr[0])
		print("The discriminent if equal to 0, the solution is:")
		print(sol)
	else :
		print("Discriminant is strictly positive, the two solutions are:")
		sol = ( -arr[1] - my_sqrt(discr) ) / (2 * arr[2])
		print(sol)
		sol = ( -arr[1] + my_sqrt(discr) ) / (2 * arr[2])
		print(sol)
	pass

# Parsing
splited = sys.argv[1]
splited = splited.split("=")
if len(splited) != 2 :
	parsing_error("Not an equation.")

tab1 = splited[0].split()
tab2 = splited[1].split()

eq1 = parse_tab(tab1)
eq2 = parse_tab(tab2)

i = 0
while (i < len(eq1) or i < len(eq2)) :
	if (i >= len(eq1)) :
		eq1.append(0)
	if (i >= len(eq2)) :
		eq2.append(0)
	i += 1

# Reduce form
resultTab = list(map(sub, eq1, eq2))

while (len(resultTab) < 3) :
	resultTab.append(0.0)

finalEq = get_reduced_form(resultTab)

print("Reduced form:", finalEq)

# Resolution
if resultTab[2] != 0:
	print("Polynomial degree: 2")
	resolve_second_degree(resultTab);
elif resultTab[1] != 0 :
	print("Polynomial degree: 1")
	resolve_first_degree(resultTab)
elif resultTab[0] != 0 :
	any_solution();
else :
	all_solution();
