def class_amount():
	
	class_amount = raw_input("How many classes do you have? > ")
	class_amount_int = int(class_amount)

	return class_amount_int

def class_names_def():
	class_names = []
	class_name = raw_input("What class is it? > ")


	return class_name

def current_grades_def():
	current_grades = []
	current_grade = raw_input("What grade do you have in the class? > ")

	return current_grade

def required_grades_def():
	required_grades = []
	required_grade = raw_input("What grade do you want to finish with? > ")

	return required_grade

def final_worths_def():
	final_worths = []
	final_worth = raw_input("How much is your final worth? > ")

	return final_worth

def calculate():
	final_grades_needed = []

	class_names = []
	current_grades = []
	required_grades = []
	final_worths = []

	class_amount_int = class_amount()

	for i in range(class_amount_int):
		
		classes = class_names_def()
		class_names.append(classes)

		grade = current_grades_def()
		if "." not in grade:
			grade = grade + ".0"
		current_grades.append((float(grade)) / 100)

		grade_wanted = required_grades_def()
		if "." not in grade_wanted:
			grade_wanted = grade_wanted + ".0"
		required_grades.append((float(grade_wanted)) / 100)

		final_weight = final_worths_def()
		if "." not in final_weight:
			final_weight = final_weight + ".0"
		final_worths.append((float(final_weight)) / 100)


		final_grade_needed = (required_grades[i] - ((1 - final_worths[i]) * (current_grades[i]))) / final_worths[i]
		final_grades_needed.append(final_grade_needed)

		print "In %s you need a %s percent\n" % (class_names[i], str((final_grades_needed[i] * 100)))

	for i in range(class_amount_int):
		print "In %s you need a %s percent" % (class_names[i], str((final_grades_needed[i] * 100)))




calculate()