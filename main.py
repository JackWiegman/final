def calculate():
	class_amount = raw_input("How many classes do you have? > ")
	class_amount_int = int(class_amount)

	class_names = []
	current_grades = []
	required_grades = []
	final_worths = []
	calculate_needed_info = []
	full_info = []
	final_grades_needed = []

	for i in range(class_amount_int):
		class_name = raw_input("What class is it? > ")
		class_names.append(class_name)

		current_grade = raw_input("What grade do you have in the class? (float) > ")
		if "." not in current_grade:
			current_grade = current_grade + ".0"
		current_grades.append((float(current_grade)) / 100)

		required_grade = raw_input("What grade do you want to finish with? (Float) > ")
		if "." not in current_grade:
			required_grade = required_grade + ".0"
		required_grades.append((float(required_grade)) / 100)

		final_worth = raw_input("How much is your final worth? (float) > ")
		if "." not in current_grade:
			final_worth = final_worth + ".0"
		final_worths.append((float(final_worth)) / 100)

		final_grade_needed = (required_grades[i] - ((1 - final_worths[i]) * (current_grades[i]))) / final_worths[i]
		final_grades_needed.append(final_grade_needed)

		print "In %s you need a %s percent" % (class_names[i], str((final_grades_needed[i] * 100)))

	for i in range(class_amount_int):
		print "\nIn %s you need a %s percent" % (class_names[i], str((final_grades_needed[i] * 100)))

calculate()