import streamlit as st
from openpyxl import Workbook, load_workbook
import os

# ============================================================
# CAMPUS SPHERE - STREAMLIT VERSION
# ============================================================

st.set_page_config(
    page_title="Campus Sphere",
    page_icon="🎓",
    layout="centered"
)

PURPLE = "#4B248F"
DARK_PURPLE = "#321567"
LIGHT_PURPLE = "#F4EEFF"
BORDER_PURPLE = "#D8C9EE"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: #FAF7FF;
    }}

    .main-title {{
        text-align: center;
        color: {PURPLE};
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 0;
    }}

    .sub-title {{
        text-align: center;
        color: {DARK_PURPLE};
        font-size: 15px;
        margin-bottom: 8px;
    }}

    .line {{
        height: 3px;
        background-color: {PURPLE};
        margin: 10px 0 20px 0;
    }}

    .section-title {{
        color: {DARK_PURPLE};
        font-size: 20px;
        font-weight: 700;
    }}

    .card {{
        background-color: white;
        border: 1px solid {BORDER_PURPLE};
        border-radius: 8px;
        padding: 18px;
        margin-bottom: 12px;
    }}

    .user-type {{
        background-color: {LIGHT_PURPLE};
        color: {PURPLE};
        padding: 8px 12px;
        border-radius: 5px;
        font-weight: 700;
        display: inline-block;
        margin: 8px 0 15px 0;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

FILE_NAME = "Campus_Sphere_Responses.xlsx"

# ============================================================
# EXCEL FUNCTIONS
# ============================================================

def save_to_excel(sheet_name, headers, data):

    try:

        if os.path.exists(FILE_NAME):

            workbook = load_workbook(FILE_NAME)

        else:

            workbook = Workbook()
            default_sheet = workbook.active
            workbook.remove(default_sheet)

        if sheet_name in workbook.sheetnames:
            sheet = workbook[sheet_name]
        else:
            sheet = workbook.create_sheet(sheet_name)
            sheet.append(headers)

        sheet.append(data)

        for column in sheet.columns:

            max_length = 0
            column_letter = column[0].column_letter

            for cell in column:

                if cell.value is not None:
                    max_length = max(
                        max_length,
                        len(str(cell.value))
                    )

            sheet.column_dimensions[column_letter].width = min(
                max(max_length + 2, 12),
                35
            )

        workbook.save(FILE_NAME)

        return True, ""

    except PermissionError:

        return False, (
            "Please close the Campus_Sphere_Responses.xlsx "
            "file and try submitting again."
        )

    except Exception as error:

        return False, str(error)


def selected(values):
    return ", ".join(values) if values else ""


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🎓 CAMPUS SPHERE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Student Information & Preferences Form</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="line"></div>', unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = 0

if "user_type" not in st.session_state:
    st.session_state.user_type = ""


def next_page():
    st.session_state.page += 1


def previous_page():
    st.session_state.page -= 1


# ============================================================
# WELCOME PAGE
# ============================================================

if st.session_state.page == 0:

    st.markdown(
        "<h1 style='text-align:center;color:#4B248F;'>"
        "Welcome to Campus Sphere"
        "</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;color:#777777;'>"
        "Your campus information, all in one place."
        "</p>",
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "Enter the Sphere",
        use_container_width=True
    ):
        st.session_state.page = -1
        st.rerun()


# ============================================================
# USER TYPE PAGE
# ============================================================

elif st.session_state.page == -1:

    st.markdown(
        '<div class="section-title">Who are you?</div>',
        unsafe_allow_html=True
    )

    st.write("Select your user type to continue.")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🎓 Student",
            use_container_width=True
        ):

            st.session_state.user_type = "Student"
            st.session_state.page = 1
            st.rerun()

    with col2:

        if st.button(
            "👩‍🏫 Staff",
            use_container_width=True
        ):

            st.session_state.user_type = "Staff"
            st.session_state.page = 5
            st.rerun()


# ============================================================
# STUDENT PAGE 1
# ============================================================

elif st.session_state.page == 1:

    st.markdown(
        '<div class="section-title">🎓 Student Details</div>',
        unsafe_allow_html=True
    )

    st.caption("Please provide your basic information.")

    st.markdown(
        '<div class="user-type">User Type: Student</div>',
        unsafe_allow_html=True
    )

    name = st.text_input(
        "1. Name (Required)",
        placeholder="Enter your name"
    )

    email = st.text_input(
        "2. Email ID (Optional)",
        placeholder="Enter your email ID"
    )

    register = st.text_input(
        "3. Register Number (Optional)",
        placeholder="Enter your register number"
    )

    department = st.selectbox(
        "4. Department (Required)",
        [
            "",
            "B.Sc Data Science",
            "BCA",
            "B.Com",
            "B.Com CA",
            "History",
            "Mathematics",
            "Other"
        ]
    )

    year = st.selectbox(
        "5. Year of Study (Required)",
        [
            "",
            "1st Year",
            "2nd Year",
            "3rd Year"
        ]
    )

    st.progress(0.20)
    st.caption("20% Completed")

    if st.button("Discover 💜 ➜", use_container_width=True):

        if name.strip() == "":
            st.warning("Please enter your Name.")

        elif department == "":
            st.warning("Please select your Department.")

        elif year == "":
            st.warning("Please select your Year of Study.")

        else:

            st.session_state.student_name = name
            st.session_state.student_email = email
            st.session_state.student_register = register
            st.session_state.student_department = department
            st.session_state.student_year = year

            st.session_state.page = 2
            st.rerun()


# ============================================================
# STUDENT PAGE 2
# ============================================================

elif st.session_state.page == 2:

    st.markdown(
        '<div class="section-title">'
        '📚 Academic, Examination, Timetables, Notices & Events'
        '</div>',
        unsafe_allow_html=True
    )

    academic = st.multiselect(
        "6. Which academic information would you like to access through Campus Sphere?",
        [
            "All",
            "Class Notes",
            "Study Materials",
            "Assignments",
            "Other Academic Information"
        ]
    )

    exam = st.multiselect(
        "7. Which examination-related information would you like to receive through Campus Sphere?",
        [
            "All",
            "Internal Exams",
            "Model Exams",
            "Semester Exams",
            "Exam Timetable"
        ]
    )

    timetable = st.multiselect(
        "8. Which timetable and regular academic updates would you like to access?",
        [
            "All",
            "Class Timetable",
            "Exam Timetable",
            "Academic Schedule"
        ]
    )

    notice = st.multiselect(
        "9. Which notices and announcements would you like to receive?",
        [
            "All",
            "College Notices",
            "Department Notices",
            "Important Announcements"
        ]
    )

    event = st.multiselect(
        "10. Which events and activities would you like to know about?",
        [
            "All",
            "Department Events",
            "Other Department Events",
            "College Events"
        ]
    )

    st.session_state.academic = academic
    st.session_state.exam = exam
    st.session_state.timetable = timetable
    st.session_state.notice = notice
    st.session_state.event = event

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⏪ Rewind 💜", use_container_width=True):
            st.session_state.page = 1
            st.rerun()

    with col2:
        if st.button("Discover 💜 ➜", use_container_width=True):
            st.session_state.page = 3
            st.rerun()

    st.progress(0.50)
    st.caption("50% Completed")


# ============================================================
# STUDENT PAGE 3
# ============================================================

elif st.session_state.page == 3:

    st.markdown(
        '<div class="section-title">🏆 Opportunities, Learning & Skills</div>',
        unsafe_allow_html=True
    )

    competition = st.multiselect(
        "11. Which competitions would you like to receive information about?",
        [
            "All",
            "Department Competitions",
            "Inter-Department Competitions",
            "College Competitions",
            "Technical & Cultural Competitions"
        ]
    )

    result = st.multiselect(
        "12. What event and competition results would you like to know?",
        [
            "All",
            "Prize Winners",
            "Winning Department",
            "Individual Achievements",
            "Awards & Recognitions"
        ]
    )

    learning = st.multiselect(
        "13. Which seminars, workshops and learning programs interest you?",
        [
            "All",
            "Seminars",
            "Workshops",
            "Training Programs",
            "Career & Skill Programs"
        ]
    )

    skill = st.multiselect(
        "14. Which skills or courses are you interested in learning or improving?",
        [
            "All",
            "Technical Skills",
            "Communication Skills",
            "Career Skills",
            "Other Skills / Courses"
        ]
    )

    st.session_state.competition = competition
    st.session_state.result = result
    st.session_state.learning = learning
    st.session_state.skill = skill

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⏪ Rewind 💜", use_container_width=True):
            st.session_state.page = 2
            st.rerun()

    with col2:
        if st.button("Discover 💜 ➜", use_container_width=True):
            st.session_state.page = 4
            st.rerun()

    st.progress(0.75)
    st.caption("75% Completed")


# ============================================================
# STUDENT PAGE 4
# ============================================================

elif st.session_state.page == 4:

    st.markdown(
        '<div class="section-title">💌 Suggestions</div>',
        unsafe_allow_html=True
    )

    suggestion = st.text_area(
        "15. What other information, skills, courses or campus activities would you like to see in Campus Sphere?",
        height=160
    )

    st.markdown(
        "<h3 style='text-align:center;color:#4B248F;'>💌<br>Thank You!</h3>",
        unsafe_allow_html=True
    )

    st.caption(
        "Your response helps us build a better Campus Sphere for you."
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⏪ Rewind 💜", use_container_width=True):
            st.session_state.page = 3
            st.rerun()

    with col2:

        if st.button(
            "✓ Submit 💜",
            use_container_width=True
        ):

            headers = [
                "User Type",
                "Name",
                "Email ID",
                "Register Number",
                "Department",
                "Year of Study",
                "Staff ID",
                "Designation",
                "Student - Academic Information",
                "Student - Examination Information",
                "Student - Timetable & Academic Updates",
                "Student - Notices & Announcements",
                "Student - Events & Activities",
                "Student - Competitions",
                "Student - Event & Competition Results",
                "Student - Seminars, Workshops & Learning Programs",
                "Student - Skills / Courses",
                "Student - Suggestions"
            ]

            data = [
                "Student",
                st.session_state.student_name,
                st.session_state.student_email,
                st.session_state.student_register,
                st.session_state.student_department,
                st.session_state.student_year,
                "",
                "",
                selected(st.session_state.academic),
                selected(st.session_state.exam),
                selected(st.session_state.timetable),
                selected(st.session_state.notice),
                selected(st.session_state.event),
                selected(st.session_state.competition),
                selected(st.session_state.result),
                selected(st.session_state.learning),
                selected(st.session_state.skill),
                suggestion
            ]

            success, error = save_to_excel(
                "Student Details and Data",
                headers,
                data
            )

            if success:

                st.success(
                    "Your response has been saved successfully! 💜"
                )

                st.info(
                    "Student details are stored in the "
                    "'Student Details and Data' sheet of "
                    "Campus_Sphere_Responses.xlsx."
                )

            else:

                st.error(
                    f"Could not save the response.\n\n{error}"
                )

    st.progress(1.0)
    st.caption("100% Completed")


# ============================================================
# STAFF PAGE 1
# ============================================================

elif st.session_state.page == 5:

    st.markdown(
        '<div class="section-title">👩‍🏫 Staff Details</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Please provide your college-related staff information."
    )

    st.markdown(
        '<div class="user-type">User Type: Staff</div>',
        unsafe_allow_html=True
    )

    staff_name = st.text_input(
        "Staff Name (Required)",
        placeholder="Enter staff name"
    )

    staff_id = st.text_input(
        "Staff ID (Required)",
        placeholder="Enter staff ID"
    )

    staff_department = st.selectbox(
        "Department (Required)",
        [
            "",
            "B.Sc Data Science",
            "BCA",
            "B.Com",
            "B.Com CA",
            "History",
            "Mathematics",
            "Other"
        ]
    )

    designation = st.selectbox(
        "Designation (Required)",
        [
            "",
            "Assistant Professor",
            "Associate Professor",
            "Professor",
            "Head of Department",
            "Coordinator",
            "Other"
        ]
    )

    if st.button("Discover 💜 ➜", use_container_width=True):

        if staff_name.strip() == "":
            st.warning("Please enter Staff Name.")

        elif staff_id.strip() == "":
            st.warning("Please enter Staff ID.")

        elif staff_department == "":
            st.warning("Please select Department.")

        elif designation == "":
            st.warning("Please select Designation.")

        else:

            st.session_state.staff_name = staff_name
            st.session_state.staff_id = staff_id
            st.session_state.staff_department = staff_department
            st.session_state.designation = designation

            st.session_state.page = 6
            st.rerun()

    st.progress(0.33)
    st.caption("33% Completed")


# ============================================================
# STAFF PAGE 2
# ============================================================

elif st.session_state.page == 6:

    st.markdown(
        '<div class="section-title">📋 Campus Management & Updates</div>',
        unsafe_allow_html=True
    )

    staff_manage = st.multiselect(
        "1. Which campus information would you like to update or manage?",
        [
            "Academic Notes",
            "Exam Timetables",
            "Class Timetables",
            "Notices & Announcements",
            "Events & Activities",
            "Seminars & Workshops",
            "Competitions & Results",
            "Student Achievements"
        ]
    )

    staff_update = st.multiselect(
        "2. Which updates should be regularly communicated to students?",
        [
            "Academic Updates",
            "Exam Updates",
            "Events",
            "Workshops",
            "Seminars",
            "Competitions",
            "Important Notices",
            "All Updates"
        ]
    )

    staff_payment = st.multiselect(
        "3. Which college-related payment information should be maintained?",
        [
            "Department Event Fees",
            "Cultural Event Fees",
            "Competition Fees",
            "Other College Fees"
        ]
    )

    staff_payment_details = st.multiselect(
        "4. Which payment details should be maintained?",
        [
            "Student Name / Register Number",
            "Amount Paid",
            "Payment Type",
            "Payment Status",
            "Date of Payment",
            "Person in Charge"
        ]
    )

    st.session_state.staff_manage = staff_manage
    st.session_state.staff_update = staff_update
    st.session_state.staff_payment = staff_payment
    st.session_state.staff_payment_details = staff_payment_details

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⏪ Rewind 💜", use_container_width=True):
            st.session_state.page = 5
            st.rerun()

    with col2:
        if st.button("Discover 💜 ➜", use_container_width=True):
            st.session_state.page = 7
            st.rerun()

    st.progress(0.66)
    st.caption("66% Completed")


# ============================================================
# STAFF PAGE 3
# ============================================================

elif st.session_state.page == 7:

    st.markdown(
        '<div class="section-title">'
        '📚 Responsibilities, Updates & Suggestions'
        '</div>',
        unsafe_allow_html=True
    )

    staff_responsibility = st.multiselect(
        "5. Who is responsible for the payment or activity?",
        [
            "Staff",
            "Student",
            "Department Coordinator",
            "Other"
        ]
    )

    staff_add_update = st.multiselect(
        "6. What information should staff be able to add or update?",
        [
            "Notes / Study Materials",
            "Timetables",
            "Notices",
            "Events",
            "Workshops / Seminars",
            "Competition Results",
            "Student Achievements",
            "Other Updates"
        ]
    )

    staff_suggestion = st.text_area(
        "7. What additional features or improvements would you suggest for Campus Sphere?",
        height=130
    )

    st.session_state.staff_responsibility = staff_responsibility
    st.session_state.staff_add_update = staff_add_update

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⏪ Rewind 💜", use_container_width=True):
            st.session_state.page = 6
            st.rerun()

    with col2:

        if st.button(
            "✓ Submit 💜",
            use_container_width=True
        ):

            headers = [
                "User Type",
                "Staff Name",
                "Staff ID",
                "Department",
                "Designation",
                "Staff - Information Managed",
                "Staff - Regular Updates",
                "Staff - Payment Information",
                "Staff - Payment Details",
                "Staff - Responsibility",
                "Staff - Information Added / Updated",
                "Staff - Suggestions"
            ]

            data = [
                "Staff",
                st.session_state.staff_name,
                st.session_state.staff_id,
                st.session_state.staff_department,
                st.session_state.designation,
                selected(st.session_state.staff_manage),
                selected(st.session_state.staff_update),
                selected(st.session_state.staff_payment),
                selected(st.session_state.staff_payment_details),
                selected(st.session_state.staff_responsibility),
                selected(st.session_state.staff_add_update),
                staff_suggestion
            ]

            success, error = save_to_excel(
                "Staff Details and Data",
                headers,
                data
            )

            if success:

                st.success(
                    "Your response has been saved successfully! 💜"
                )

                st.info(
                    "Staff details are stored in the "
                    "'Staff Details and Data' sheet of "
                    "Campus_Sphere_Responses.xlsx."
                )

            else:

                st.error(
                    f"Could not save the response.\n\n{error}"
                )

    st.progress(1.0)
    st.caption("100% Completed")
