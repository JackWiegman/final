def class_amount():
	
		class_amount = raw_input("How many classes do you have? > ")
		class_amount_int = int(class_amount)

	return class_amount_int

def class_names():
	classes_num = class_amount()
	class_names = []
	for i in range(classes_num):
		class_name = raw_input("What class is it? > ")
		class_names.append(class_name)

	return class_names

def current_grades():
	classes_num = class_amount()
	current_grades = []
	current_grade = raw_input("What grade do you have in the class? > ")
	for i in range(classes_num):
		if "." not in current_grade:
			current_grade = current_grade + ".0"
		current_grades.append((float(current_grade)) / 100)

	return current_grades

def required_grades():
	classes_num = class_amount()
	required_grades = []
	required_grade = raw_input("What grade do you want to finish with? > ")
	for i in range(classes_num):
		if "." not in required_grade:
			required_grade = required_grade + ".0"
		required_grades.append((float(required_grade)) / 100)

	return required_grades

def final_worths():
	classes_num = class_amount()
	final_worths = []
	final_worth = raw_input("How much is your final worth? > ")
	for i in range(classes_num):
		if "." not in final_worth:
			final_worth = final_worth + ".0"
		final_worths.append((float(final_worth)) / 100)

	return final_worths

def calculate():
	final_grades_needed = []

	# classes = class_names()
	# grades = current_grades()
	# grades_wanted = required_grades()
	# final_weights = final_worths()

	# final_grade_needed = (grades_wanted[0] - ((1 - final_weights[0]) * (grades[0]))) / final_weights[0]
	# final_grades_needed.append(final_grade_needed)

	# print "In %s you need a %s percent" % (classes[0], str((final_grades_needed[0] * 100)))

	classes = class_names()
	grades = current_grades()
	grades_wanted = required_grades()
	final_weights = final_worths()

	for i in range(class_amount_int):
		final_grade_needed = (grades_wanted[i] - ((1 - final_weights[i]) * (grades[i]))) / final_weights[i]
		final_grades_needed.append(final_grade_needed)

		print "In %s you need a %s percent" % (classes[i], str((final_grades_needed[i] * 100)))

	for i in range(class_amount_int):
		print "\nIn %s you need a %s percent" % (classes[i], str((final_grades_needed[i] * 100)))


calculate()