from selene import have
from demoqa_tests.data.data import User
from demoqa_tests.hw_tests.application_manager import app
import logging

logging.getLogger('WDM').setLevel(logging.NOTSET)


def test_register_student_dev_patel(open_auto_practice_form):
	student = User()
	app.registration_form.set_first_name(student.first_name) \
		.set_last_name(student.last_name).set_email(student.email)\
		.set_male_gender()\
		.set_mobile_number(student.mobile_number)\
		.set_date_of_birth(student.birthday_day, student.birthday_month, student.birthday_year)\
		.add_subject(student.subject_computer_science)\
		.add_subject(student.subject_social_studies)\
		.add_subject(student.subject_chemistry)\
		.add_subject(student.subject_maths) \
		.add_subject(student.subject_physics)\
		.add_hobbies(student.hobby_sports)\
		.add_hobbies(student.hobby_reading)\
		.add_hobbies(student.hobby_music)\
		.browse_picture(student.picture)\
		.set_address(student.address)\
		.select_state(option=student.state)\
		.select_city(option=student.city)\
		.submit()

	app.results_modal.table.check_cells_of_row(1).should(have.exact_texts(
		'Student Name', f'{student.first_name} {student.last_name}'))
	app.results_modal.table.check_cells_of_row(2).should(have.exact_texts(
		'Student Email', f'{student.email}'))
	app.results_modal.table.check_cells_of_row(3).should(have.exact_texts(
		'Gender', f'{student.gender}'))
	app.results_modal.table.check_cells_of_row(4).should(have.exact_texts(
		'Mobile', f'{student.mobile_number}'))
	app.results_modal.table.check_cells_of_row(5).should(have.exact_texts(
		'Date of Birth', f'{student.birthday_day} {student.birthday_month_name},{student.birthday_year}'))
	app.results_modal.table.check_cells_of_row(6).should(have.exact_texts(
		'Subjects',
		f'{student.subject_computer_science}, {student.subject_social_studies}, '
		f'{student.subject_chemistry}, {student.subject_maths}, {student.subject_physics}'))
	app.results_modal.table.check_cells_of_row(7).should(have.exact_texts(
		'Hobbies', f'{student.hobby_sports}, {student.hobby_reading}, {student.hobby_music}'))
	app.results_modal.table.check_cells_of_row(8).should(have.exact_texts(
		'Picture', student.picture))
	app.results_modal.table.check_cells_of_row(9).should(have.exact_texts(
		'Address', student.address))
	app.results_modal.table.check_cells_of_row(10).should(have.exact_texts(
		'State and City', f'{student.state} {student.city}'))

	app.results_modal.close_modal_and_check_result()
