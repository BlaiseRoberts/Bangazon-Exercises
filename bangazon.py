import random

class Department():
		''' Parent class for all depts'''

		def __init__(self):
			self.employees = set()

		def get_budget(self):
			self.budget = 1000
			return self.budget

		def add_employee(self, employee):
			employee_details = ""
			try:
				employee_details = ' hours per week: '+ str(employee.hour_per_week)
			except (AttributeError, NameError):
				pass	
			try:
				if employee.access_card == True:
					employee_details += ' and has an access card '
			except (AttributeError, NameError):
				pass						
			try:
				employee_name = employee.firstName+" "+employee.lastName+employee_details
				self.employees.add(employee_name)
			except (AttributeError, NameError):
				print("you need to add an employee")

		def remove_employee(self, employee):
			try:
				employee_name = employee.firstName+" "+employee.lastName
				self.employees.remove(employee_name)
			except AttributeError:
				print("you need to add an employee") 
			except KeyError:
				print("The employee is not currently part of this department")

		def get_employees(self):
			print("Department: {}\n\t{}".format(self.name, ("\n\t".join(self.employees))))


		@property
		def name(self):
			try:
				return self.__name
			except AttributeError:
				return ""

		@name.setter
		def name(self, val):
			if len(val) > 1:
				self.__name = val
			else:
				raise ValueError('Please enter a department name')

		@property
		def supervisor(self):
			try:
				return self.__supervisor
			except AttributeError:
				return ""

		@supervisor.setter
		def supervisor(self, val):
			if len(val) > 4:
				self.__supervisor = val
			else:
				raise ValueError('Please enter a supervisor name longer than 4 characters')

		def meet(self):
			print("Everyone meet in {}'s office".format(self.supervisor))

class HumanResources(Department):
	'''Class representing Human Resources Dept

	Methods: __init__, add_policy, meet
	'''

	def __init__(self, name, supervisor):
		super().__init__()
		self.name = name
		self.supervisor = supervisor

		self.policies = set()

	def add_policy(self, policy_name, policy_text):
		'''Adds a policy(tuple) to the policies(set)

		Arguments:
		policy_name - string
		policy_text - string
		'''

		self.policies.add((policy_name, policy_text))

	def meet(self):
		'''Overwrites parent's meet to include personal message'''
		print("Everyone meet in {}'s office to talk about our feelings".format(self.supervisor))	

	def get_budget(self):
		'''Sets the base budget and adds for the dept'''
		self.budget = super().get_budget() + 650000
		print(self.budget)

class IT(Department):
	'''Class representing IT Dept

	Methods: __init__ & add_computer
	'''

	def __init__(self, name, supervisor):
		super().__init__()
		self.name = name
		self.supervisor = supervisor
		self.computer_dict = dict()

	def add_computer(self, computerID, employeeID = "Not Registered"):
		'''Adds a new computer to the computer_dict as a key,
		if no emplyeeID is entered it will be assigned Not Registered.

		Arguments:
		ComputerID - string
		EmployeeID - string (if nothing is entered the comp will be given the value Not Registered)
		'''

		self.computer_dict[computerID] = employeeID

	def meet(self):
		'''Overwrites parent's meet to include personal message'''
		print("Everyone meet in {}'s office for tech stuff".format(self.supervisor))	
	
	def get_budget(self):
		'''Sets the base budget and adds for the dept'''
		self.budget = super().get_budget() + 780000
		print(self.budget)

class Communications(Department):
	'''Class representing Communications Dept

	Methods: __init__ & add_press_release
	'''

	def __init__(self, name, supervisor):
		super().__init__()
		self.name = name
		self.supervisor = supervisor
		self.press_releases = set()

	def add_press_release(self, press_release, employeeID):
		'''Adds a press_release(tuple) to press_releases(set)

		Arguments:
		press_release - string
		EmployeeID - string 
		'''

		self.press_releases.add((press_release, employeeID))

	def meet(self):
		'''Overwrites parent's meet to include personal message'''
		print("Everyone meet in {}'s office to talk talk talk talk talk".format(self.supervisor))	
	
	def get_budget(self):
		'''Sets the base budget and adds for the dept'''
		self.budget = super().get_budget() + 876000
		print(self.budget)

class Sales(Department):
	'''Class representing Sales Dept

	Methods: __init__ & add_sale
	'''

	def __init__(self, name, supervisor):
		super().__init__()
		self.name = name
		self.supervisor = supervisor
		self.sales_history = list()

	def add_sale(self, emplyeeID, sale_ammount, client):
		'''Adds a sale(tuple) to sales_history(set)

		Arguments:
		employeeID - string 
		sale_ammount - integer
		client - string
		'''

		self.sales_history.append((emplyeeID, sale_ammount, client))

	def meet(self):
		'''Overwrites parent's meet to include personal message'''
		print("Everyone meet in {}'s office or else...".format(self.supervisor))	

	def get_budget(self):
		'''Sets the base budget and adds for the dept'''
		self.budget = super().get_budget() + 907400
		print(self.budget)



class Employee():
	'''Class representing an employee

	Methods: eat
	'''

	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName

	def eat(self, food=None, companions=None):
		resturant_list = ["Chili's", "Red Robin", "Marsh House"]
		random_resturant = resturant_list[random.randrange(3)]
		if food is not None and companions is not None:
			print("{} {} ate a/some {} at {} with {}".format(self.firstName, self.lastName, food, random_resturant, (', '.join(companions))))			
		elif food is not None and companions is None:
			print("{} {} ate a/some {} at the office".format(self.firstName, self.lastName, food))
		elif companions is not None:
			print("{} {} ate at {} with {}".format(self.firstName, self.lastName, random_resturant, (', '.join(companions))))
		else:
			print("{} {} ate at {}".format(self.firstName, self.lastName, random_resturant))
			return random_resturant

class FullTime():
	'''Class representing Full-Time employee'''

	def __init__(self):
		self.hour_per_week = 40

class PartTime():
	'''Class representing Part-Time employee'''

	def __init__(self):
		self.hour_per_week = 20

class AccessCard():
	'''Class representing employee that need Access Card'''

	def __init__(self):
		self.access_card = True

class HumanResourceEmployee(Employee, FullTime, AccessCard):
	'''Class representing Human Resources Employee'''

	def __init__(self, firstName, lastName):
		super().__init__(firstName, lastName)
		FullTime.__init__(self)
		AccessCard.__init__(self)

class ITEmployee(Employee, PartTime, AccessCard):
	'''Class representing IT Employee'''

	def __init__(self, firstName, lastName):
		super().__init__(firstName, lastName)
		PartTime.__init__(self)
		AccessCard.__init__(self)	

class CommunicationsEmployee(Employee, FullTime):
	'''Class representing Communications Employee'''

	def __init__(self, firstName, lastName):
		super().__init__(firstName, lastName)
		FullTime.__init__(self)

class SalesEmployee(Employee, PartTime):
	'''Class representing Communications Employee'''

	def __init__(self, firstName, lastName):
		super().__init__(firstName, lastName)
		PartTime.__init__(self)





if __name__ == '__main__':
	human_resources = HumanResources('Human Resources', 'Harper')
	human_resources.add_policy('No Dating', 'Employees may not date other employees')
	print(human_resources.name)
	print(human_resources.policies)
	com_dept = Communications('Communications', 'Helana')
	com_dept.add_press_release('Dolly Parton Tribute is a bigggggggggggggggggg success!', '357be90')
	print(com_dept.name)
	print(com_dept.press_releases)
	it_dept = IT('IT', 'Kayla')
	it_dept.add_computer('430-4738-123')
	it_dept.add_computer('780-1458-127', '897rd87')
	print(it_dept.name)
	print(it_dept.computer_dict)
	sales_dept = Sales('Sales', 'Taylor')
	sales_dept.add_sale('545jk55', 7496, 'NSS')
	print(sales_dept.name)
	print(sales_dept.sales_history)
	human_resources.meet()
	com_dept.meet()
	it_dept.meet()
	sales_dept.meet()
	human_resources.get_budget()
	com_dept.get_budget()
	it_dept.get_budget()
	sales_dept.get_budget()
	blaise = Employee('Blaise', 'Roberts')
	blaise.eat()
	blaise.eat(food='sandwich')
	blaise.eat(companions=['Harper', 'Angela', 'Kayla'])
	blaise.eat('pizza', ['Harper', 'Angela', 'Kayla'])
	helana = HumanResourceEmployee('Helana', 'Nosrat')
	bob = ITEmployee('Bob', 'Builder')
	tracy = CommunicationsEmployee('Tracy', 'Chapman')
	kanye = SalesEmployee('Kanye', 'West')
	it_dept.add_employee(helana)
	it_dept.add_employee(tracy)
	it_dept.add_employee(blaise)
	it_dept.add_employee(bob)
	it_dept.add_employee(kanye)
	it_dept.get_employees()
	







