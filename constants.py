USER_TYPE_CHOICES = [
    ('admin', 'Admin'),
    ('management', 'Management'),
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    ('payrollmanagement', 'PayrollManagement'),
    ('boarding', 'Boarding'),
    ('non-teaching', 'Non-teaching')
]

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'female'),
    ('other', 'Other'),
]

RELIGION_CHOICES = [
    ('christian', 'Christian'),
    ('islam', 'Islam'),
    ('hinduism', 'Hinduism'),
    ('buddhism', 'Buddhism'),
    ('sikhism', 'Sikhism'),
    ('judaism', 'Judaism'),
    ('other', 'Other'),
]
BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

CLASS_CHOICES = [
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
    ('5th', '5th'),
    ('6th', '6th'),
    ('7th', '7th'),
    ('8th', '8th'),
    ('9th', '9th'),
    ('10th', '10th'),
    ('11th', '11th'),
    ('12th', '12th'),
]

SUBJECT_CHOICES = [
    ("english", "english"),
    ("hindi", "hindi"),
    ("maths", "maths"),
    ("science", "science"),
]
ROLE_CHOICES = [
    ("teacher", "teacher"),
    ("class_teacher", "class_teacher")
]

ATTENDENCE_CHOICE = [
    ("P", "present"),
    ("A", "Absent"),
    ("L", "On_leave")
]

EXAME_TYPE_CHOICE = [
    ('Annual Exams', 'Annual Exams'),
    ('Half Yearly Exams', 'Half Yearly Exams'),
    ('Quarterly Exams', 'Quarterly Exams'),
    ('Pre-Board Exams', 'Pre-Board Exams'),
]
class UserLoginMessage:
    USER_DOES_NOT_EXISTS = "User does not exists."
    INCORRECT_PASSWORD = "Incorrect password, please try again."
    SIGNUP_SUCCESSFUL = "User Signup successful."
    STAFF_ALREADY_EXISTS = "Staff email or phone already exists"
    USER_LOGIN_SUCCESSFUL = "User login successfully."


class UserResponseMessage:
    USER_DOES_NOT_EXISTS = "User does not exists."
    USER_NOT_FOUND = "User not found"
    USER_DETAIL_MESSAGE = "User detail fetch successfully."
    USER_LIST_MESSAGE = "All user's fetch successfully."
    USER_DELETE_MESSAGE = "User deleted successfully."
    PROFILE_UPDATED_SUCCESSFULLY = "User profile updated successfully"
    EMAIL_ALREADY_EXIST = "Email already exist."
    TOKEN_HAS_EXPIRED = "Token has expired."


class CurriculumMessage:
    CURRICULUM_CREATED_SUCCESSFULLY = "Curriculum created successfully."
    CURRICULUM_LIST_MESSAGE = "All curriculum fetch successfully."
    CURRICULUM_DELETED_SUCCESSFULLY = "Curriculum deleted successfully."
    CURRICULUM_NOT_FOUND = "Curriculum not found."
    CURRICULUM_DETAIL_MESSAGE = "Curriculum detail fetch successfully."


class ScheduleMessage:
    SCHEDULE_CREATED_SUCCESSFULLY = "Schedule created successfully.",
    SCHEDULE_FETCHED_SUCCESSFULLY = "Schedule fetched successfully."
    SCHEDULE_NOT_FOUND = "Schedule not found."
    SCHEDULE_DELETED_SUCCESSFULLY = "Schedule deleted successfully.",
    SCHEDULE_LIST_MESSAGE = "All schedule fetch successfully."
    SCHEDULE_UPDATED_SUCCESSFULLY = "Teacher schedule updated successfully"


class AttendenceMarkedMessage:
    ATTENDENCE_MARKED_SUCCESSFULLY = "Attendence marked successfully."
    ATTENDANCE_FETCHED_SUCCESSFULLY = 'Attendance fetched successfully.'
    STUDENT_ATTENDANCE_FETCHED_SUCCESSFULLY = 'Student attendance fetched successfully.'


class SchoolMessage:
    SCHOOL_CREATED_SUCCESSFULLY = "School created successfully."
    SCHOOL_DETAIL_MESSAGE = "School profile fetch successfully."
    SCHOOL_DOES_NOT_EXISTS = "School does not exists."
    SCHOOL_PROFILE_UPDATED_SUCCESSFULLY = "School profile updated successfully"
    SCHOOL_EMAIL_ALREADY_EXIST = "School with this email already exist."
    SCHOOL_DELETED_SCCCESSFULLY = "School profile deleted successfully."


class DayReviewMessage:
    DAY_REVIEW_CREATED_SUCCESSFULLY = "Day and reviw created successfully."
    DAY_REVIEW_FETCHED_SUCCESSFULLY = "Day and review detail fetch successfully."
    DAY_REVIEW_NOT_FOUND = "Day and review not found."


class NotificationMessage:
    NOTIFICATION_CREATED_SUCCESSFULLY = "Notification created successfully."
    NOTIFICATION_FETCHED_SUCCESSFULLY = "Notification fetched successfully."


class AnnouncementMessage:
    ANNOUNCEMENT_CREATED_SUCCESSFULLE = "Announcement created successfully."
    ANNOUNCEMENT_FETCHED_SUCCESSFULLE = "Announcement fetched successfully."


class TimeTableMessage:
    TIMETABLE_CREATED_SUCCESSFULLY = "Timetable created successfully."
    UNDECLARED_TIMETABLE_FETCHED_SUCCESSFULLY = "Undeclared timetable fetched successfully."
    DECLARED_TIMETABLE_FETCHED_SUCCESSFULLY = "declared timetable fetched successfully."
    TIMETABLE_FETCHED_SUCCESSFULLY = "Timetable fetched successfully."
    TIMETABLE_NOT_EXIST = "Timetable does not exist."
    TIMETABLE_DELETED_SUCCESSFULLY = "Timetable deleted successfully."
    TIMETABLE_UPDATED_SUCCESSFULLY = "Timetable updated successfully."
    TIMETABLE_DECLARE_SUCCESSFULLY = "Timetable declare successfully."


class ReportCardMesssage:
    REPORT_CARD_CREATED_SUCCESSFULLY = "Report card created successfully."
    REPORT_CARD_FETCHED_SUCCESSFULLY = "Report card fetched successfully."
    REPORT_CARD_DELETED_SUCCESSFULLY = "Report card deleted successfully."
    REPORT_CARD_UPDATED_SUCCESSFULLY = "Report card updated successfully."
    REPORT_CARD_list_SUCCESSFULLY = "All report card fetched successfully."
    REPORT_CARD_DECLARE_SUCCESSFULLY = "Report card declare successfully."
    UNDECLARED_REPORT_CARD_FETCHED_SUCCESSFULLY = "Undeclared report card fetched successfully."
    DECLARED_REPORT_CARD_FETCHED_SUCCESSFULLY = "declared report card fetched successfully."
    REPORT_CARD_NOT_EXIST = "Report card does not exist."