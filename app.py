import streamlit as st
import json
import urllib.request
from datetime import datetime


# ============================================================
# CAMPUS SPHERE
# ============================================================

st.set_page_config(
    page_title="Campus Sphere",
    page_icon="💜",
    layout="wide"
)


# ============================================================
# GOOGLE APPS SCRIPT URL
# ============================================================

GOOGLE_SCRIPT_URL = (
    "https://script.google.com/macros/s/"
    "AKfycbyVCqbH-YzW7OE03d-s0RnVnAzf3ZwVxRrBqwjmNZRC8tK0xxpSL7fMYrbe-PJKPee9/"
    "exec"
)


# ============================================================
# DESIGN
# ============================================================

PURPLE = "#4B248F"

st.markdown(
    f"""
    <style>

    .main-title {{
        color: {PURPLE};
        text-align: center;
        font-size: 46px;
        font-weight: bold;
        margin-top: 30px;
    }}

    .subtitle {{
        color: #777777;
        text-align: center;
        font-size: 19px;
        margin-bottom: 30px;
    }}

    .section-title {{
        color: {PURPLE};
        font-size: 30px;
        font-weight: bold;
        margin-bottom: 20px;
    }}

    .question-title {{
        color: {PURPLE};
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }}

    .welcome-text {{
        color: #555555;
        text-align: center;
        font-size: 18px;
        line-height: 1.7;
    }}

    div.stButton > button {{
        border-radius: 10px;
        font-weight: bold;
        min-height: 45px;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# OPTIONS
# ============================================================

ACADEMIC_OPTIONS = [
    "All",
    "Class Notes",
    "Study Materials",
    "Assignments",
    "Other Academic Information"
]

EXAM_OPTIONS = [
    "All",
    "Internal Exams",
    "Model Exams",
    "Semester Exams",
    "Exam Timetable"
]

TIMETABLE_OPTIONS = [
    "All",
    "Class Timetable",
    "Exam Timetable",
    "Academic Schedule"
]

NOTICE_OPTIONS = [
    "All",
    "College Notices",
    "Department Notices",
    "Important Announcements"
]

EVENT_OPTIONS = [
    "All",
    "Department Events",
    "Other Department Events",
    "College Events"
]

COMPETITION_OPTIONS = [
    "All",
    "Department Competitions",
    "Inter-Department Competitions",
    "College Competitions",
    "Technical & Cultural Competitions"
]

RESULT_OPTIONS = [
    "All",
    "Prize Winners",
    "Winning Department",
    "Individual Achievements",
    "Awards & Recognitions"
]

LEARNING_OPTIONS = [
    "All",
    "Seminars",
    "Workshops",
    "Training Programs",
    "Career & Skill Programs"
]

SKILL_OPTIONS = [
    "All",
    "Technical Skills",
    "Communication Skills",
    "Career Skills",
    "Other Skills / Courses"
]

MANAGE_OPTIONS = [
    "Academic Notes",
    "Exam Timetables",
    "Class Timetables",
    "Notices & Announcements",
    "Events & Activities",
    "Seminars & Workshops",
    "Competitions & Results",
    "Student Achievements"
]

UPDATE_OPTIONS = [
    "Academic Updates",
    "Exam Updates",
    "Events",
    "Workshops",
    "Seminars",
    "Competitions",
    "Important Notices",
    "All Updates"
]

PAYMENT_OPTIONS = [
    "Department Event Fees",
    "Cultural Event Fees",
    "Competition Fees",
    "Other College Fees"
]

PAYMENT_DETAILS_OPTIONS = [
    "Student Name / Register Number",
    "Amount Paid",
    "Payment Type",
    "Payment Status",
    "Date of Payment",
    "Person in Charge"
]

RESPONSIBILITY_OPTIONS = [
    "Staff",
    "Student",
    "Department Coordinator",
    "Other"
]

ADD_OPTIONS = [
    "Notes / Study Materials",
    "Timetables",
    "Notices",
    "Events",
    "Workshops / Seminars",
    "Competition Results",
    "Student Achievements",
    "Other Updates"
]


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "welcome"

# Student details
if "student_name" not in st.session_state:
    st.session_state.student_name = ""

if "student_email" not in st.session_state:
    st.session_state.student_email = ""

if "student_register" not in st.session_state:
    st.session_state.student_register = ""

if "student_department" not in st.session_state:
    st.session_state.student_department = "Select Department"

if "student_year" not in st.session_state:
    st.session_state.student_year = "Select Year"

# Student question 10
if "student_other_information" not in st.session_state:
    st.session_state.student_other_information = ""

# Staff details
if "staff_name" not in st.session_state:
    st.session_state.staff_name = ""

if "staff_id" not in st.session_state:
    st.session_state.staff_id = ""

if "staff_department" not in st.session_state:
    st.session_state.staff_department = ""

if "staff_designation" not in st.session_state:
    st.session_state.staff_designation = "Select Designation"

# Staff question 7
if "staff_suggestions" not in st.session_state:
    st.session_state.staff_suggestions = ""


# ============================================================
# NAVIGATION
# ============================================================

def go_to(page):
    st.session_state.page = page


# ============================================================
# CHECKBOX FUNCTION
# ============================================================

def get_checked(prefix, options):

    selected = []

    for option in options:

        key = f"{prefix}_{option}"

        if st.session_state.get(key, False):
            selected.append(option)

    if not selected:
        return "None"

    return ", ".join(selected)


# ============================================================
# SEND RESPONSE TO GOOGLE SHEETS
# ============================================================

def send_to_google_sheet(response):

    try:

        data = json.dumps(response).encode("utf-8")

        request = urllib.request.Request(
            GOOGLE_SCRIPT_URL,
            data=data,
            headers={
                "Content-Type": "application/json"
            },
            method="POST"
        )

        with urllib.request.urlopen(
            request,
            timeout=30
        ) as result:

            response_text = result.read().decode("utf-8")

        return True, response_text

    except Exception as error:

        return False, str(error)


# ============================================================
# WELCOME PAGE
# ============================================================

if st.session_state.page == "welcome":

    st.markdown(
        '<div class="main-title">💜 Campus Sphere</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Welcome to Campus Sphere</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="welcome-text">

        Welcome to <b>Campus Sphere</b> — your college
        information and feedback portal.

        <br><br>

        Connect, discover and share information
        within your campus community.

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        if st.button(
            "💜 Enter the Sphere",
            type="primary",
            use_container_width=True
        ):

            go_to("user_type")
            st.rerun()


# ============================================================
# USER TYPE
# ============================================================

elif st.session_state.page == "user_type":

    st.markdown(
        '<div class="section-title">Choose Your Category</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Please select whether you are a student or staff member."
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "👨‍🎓 Student",
            use_container_width=True
        ):

            go_to("student_details")
            st.rerun()

    with col2:

        if st.button(
            "👩‍🏫 Staff",
            use_container_width=True
        ):

            go_to("staff_details")
            st.rerun()

    st.write("")

    if st.button(
        "💜 Rewind",
        use_container_width=True
    ):

        go_to("welcome")
        st.rerun()


# ============================================================
# STUDENT DETAILS
# ============================================================

elif st.session_state.page == "student_details":

    st.markdown(
        '<div class="section-title">👨‍🎓 Student Details</div>',
        unsafe_allow_html=True
    )

    st.text_input(
        "Name *",
        key="student_name"
    )

    st.text_input(
        "Email ID",
        key="student_email"
    )

    st.text_input(
        "Register Number",
        key="student_register"
    )

    st.selectbox(
        "Department *",
        [
            "Select Department",
            "B.Sc Data Science",
            "BCA",
            "B.Com",
            "B.Com CA",
            "History",
            "Mathematics",
            "Other"
        ],
        key="student_department"
    )

    st.selectbox(
        "Year of Study *",
        [
            "Select Year",
            "1st Year",
            "2nd Year",
            "3rd Year"
        ],
        key="student_year"
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "💜 Rewind",
            use_container_width=True
        ):

            go_to("user_type")
            st.rerun()

    with col2:

        if st.button(
            "💜 Continue",
            type="primary",
            use_container_width=True
        ):

            if not st.session_state.student_name.strip():

                st.error("Please enter your name.")

            elif (
                st.session_state.student_department
                == "Select Department"
            ):

                st.error("Please select your department.")

            elif (
                st.session_state.student_year
                == "Select Year"
            ):

                st.error("Please select your year of study.")

            else:

                go_to("student_questions1")
                st.rerun()


# ============================================================
# STUDENT QUESTIONS 1
# ============================================================

elif st.session_state.page == "student_questions1":

    st.markdown(
        '<div class="section-title">'
        '📚 Academic & Campus Information'
        '</div>',
        unsafe_allow_html=True
    )

    # QUESTION 1

    st.markdown(
        '<div class="question-title">'
        'Q1. Which academic information would you like to access through Campus Sphere?'
        '</div>',
        unsafe_allow_html=True
    )

    for option in ACADEMIC_OPTIONS:

        st.checkbox(
            option,
            key=f"academic_{option}"
        )


    # QUESTION 2

    st.markdown(
        '<div class="question-title">'
        'Q2. Which examination-related information would you like to receive through Campus Sphere?'
        '</div>',
        unsafe_allow_html=True
    )

    for option in EXAM_OPTIONS:

        st.checkbox(
            option,
            key=f"exam_{option}"
        )


    # QUESTION 3

    st.markdown(
        '<div class="question-title">'
        'Q3. Which timetable and regular academic updates would you like to access?'
        '</div>',
        unsafe_allow_html=True
    )

    for option in TIMETABLE_OPTIONS:

        st.checkbox(
            option,
            key=f"timetable_{option}"
        )


    # QUESTION 4

    st.markdown(
        '<div class="question-title">'
        'Q4. Which notices and announcements would you like to receive?'
        '</div>',
        unsafe_allow_html=True
    )

    for option in NOTICE_OPTIONS:

        st.checkbox(
            option,
            key=f"notice_{option}"
        )


    # QUESTION 5

    st.markdown(
        '<div class="question-title">'
        'Q5. Which events and activities would you like to know about?'
        '</div>',
        unsafe_allow_html=True
    )

    for option in EVENT_OPTIONS:

        st.checkbox(
            option,
            key=f"event_{option}"
        )


    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "💜 Rewind",
            use_container_width=True
        ):

            go_to("student_details")
            st.rerun()

    with col2:

        if st.button(
            "💜 Continue",
            type="primary",
            use_container_width=True
        ):

            go_to("student_questions2")
            st.rerun()


# ============================================================
# STUDENT QUESTIONS 2
# ============================================================

elif st.session_state.page == "student_questions2":

    st.markdown(
        '<div class="section-title">'
        '🏆 Opportunities, Learning & Skills'
        '</div>',
        unsafe_allow_html=True
    )

    # QUESTION 6

    st.markdown(
        '<div class="question-title">'
        'Q6. Which competitions would you like to receive information about?'
        '</div>',
        unsafe_allow_html=True
    )

    for option in COMPETITION_OPTIONS:

        st.checkbox(
            option,
            key=f"competition_{option}"
        )


    # QUESTION 7

    st.markdown(
        '<div class="question-title">'
        'Q7. What event and competition results would you like to know?'
        '</div>',
        unsafe_allow_html=True
    )

    for option in RESULT_OPTIONS:

        st.checkbox(
            option,
            key=f"result_{option}"
        )


    # QUESTION 8

    st.markdown(
        '<div class="question-title">'
        'Q8. Which seminars, workshops and learning programs interest you?'
        '</div>',
        unsafe_allow_html=True
    )

    for option in LEARNING_OPTIONS:

        st.checkbox(
            option,
            key=f"learning_{option}"
        )


    # QUESTION 9

    st.markdown(
        '<div class="question-title">'
        'Q9. Which skills or courses are you interested in learning or improving?'
        '</div>',
        unsafe_allow_html=True
    )

    for option in SKILL_OPTIONS:

        st.checkbox(
            option,
            key=f"skill_{option}"
        )


    # QUESTION 10

    st.markdown(
        '<div class="question-title">'
        'Q10. What other information, skills, courses or campus activities would you like to see in Campus Sphere?'
        '</div>',
        unsafe_allow_html=True
    )

    st.text_area(
        "Your answer",
        key="student_other_information",
        height=150
    )


    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "💜 Rewind",
            use_container_width=True
        ):

            go_to("student_questions1")
            st.rerun()

    with col2:

        if st.button(
            "💜 Submit Response",
            type="primary",
            use_container_width=True
        ):

            response = {

                "Submitted At":
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),

                "User Type":
                    "Student",

                # STUDENT DETAILS

                "Name":
                    st.session_state.student_name,

                "Email ID":
                    st.session_state.student_email,

                "Register Number":
                    st.session_state.student_register,

                "Department":
                    st.session_state.student_department,

                "Year of Study":
                    st.session_state.student_year,

                # QUESTIONS

                "Q1 - Academic Information":
                    get_checked(
                        "academic",
                        ACADEMIC_OPTIONS
                    ),

                "Q2 - Examination Information":
                    get_checked(
                        "exam",
                        EXAM_OPTIONS
                    ),

                "Q3 - Timetable & Academic Updates":
                    get_checked(
                        "timetable",
                        TIMETABLE_OPTIONS
                    ),

                "Q4 - Notices & Announcements":
                    get_checked(
                        "notice",
                        NOTICE_OPTIONS
                    ),

                "Q5 - Events & Activities":
                    get_checked(
                        "event",
                        EVENT_OPTIONS
                    ),

                "Q6 - Competitions":
                    get_checked(
                        "competition",
                        COMPETITION_OPTIONS
                    ),

                "Q7 - Results & Achievements":
                    get_checked(
                        "result",
                        RESULT_OPTIONS
                    ),

                "Q8 - Seminars / Workshops / Learning":
                    get_checked(
                        "learning",
                        LEARNING_OPTIONS
                    ),

                "Q9 - Skills / Courses":
                    get_checked(
                        "skill",
                        SKILL_OPTIONS
                    ),

                "Q10 - Other Information":
                    st.session_state.student_other_information
            }

            success, message = send_to_google_sheet(response)

            if success:

                st.success(
                    "💜 Your response has been submitted successfully!"
                )

            else:

                st.error(
                    "❌ Unable to submit the response."
                )

                st.code(message)


# ============================================================
# STAFF DETAILS
# ============================================================

elif st.session_state.page == "staff_details":

    st.markdown(
        '<div class="section-title">👩‍🏫 Staff Details</div>',
        unsafe_allow_html=True
    )

    st.text_input(
        "Staff Name *",
        key="staff_name"
    )

    st.text_input(
        "Staff ID *",
        key="staff_id"
    )

    st.text_input(
        "Department *",
        key="staff_department"
    )

    st.selectbox(
        "Designation *",
        [
            "Select Designation",
            "Assistant Professor",
            "Associate Professor",
            "Professor",
            "Head of Department",
            "Coordinator",
            "Other"
        ],
        key="staff_designation"
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "💜 Rewind",
            use_container_width=True
        ):

            go_to("user_type")
            st.rerun()

    with col2:

        if st.button(
            "💜 Continue",
            type="primary",
            use_container_width=True
        ):

            if not st.session_state.staff_name.strip():

                st.error("Please enter staff name.")

            elif not st.session_state.staff_id.strip():

                st.error("Please enter Staff ID.")

            elif not st.session_state.staff_department.strip():

                st.error("Please enter department.")

            elif (
                st.session_state.staff_designation
                == "Select Designation"
            ):

                st.error("Please select designation.")

            else:

                go_to("staff_questions")
                st.rerun()


# ============================================================
# STAFF QUESTIONS
# ============================================================

elif st.session_state.page == "staff_questions":

    st.markdown(
        '<div class="section-title">'
        '🗂️ Campus Management & Updates'
        '</div>',
        unsafe_allow_html=True
    )


    # QUESTION 1

    st.markdown(
        '<div class="question-title">'
        'Q1. Which campus information would you like to update or manage?'
        '</div>',
        unsafe_allow_html=True
    )

    for option in MANAGE_OPTIONS:

        st.checkbox(
            option,
            key=f"manage_{option}"
        )


    # QUESTION 2

    st.markdown(
        '<div class="question-title">'
        'Q2. Which updates should be regularly communicated to students?'
        '</div>',
        unsafe_allow_html=True
    )

    for option in UPDATE_OPTIONS:

        st.checkbox(
            option,
            key=f"update_{option}"
        )


    # QUESTION 3

    st.markdown(
        '<div class="question-title">'
        'Q3. Which college-related payment information should be maintained?'
        '</div>',
        unsafe_allow_html=True
    )

    for option in PAYMENT_OPTIONS:

        st.checkbox(
            option,
            key=f"payment_{option}"
        )


    # QUESTION 4

    st.markdown(
        '<div class="question-title">'
        'Q4. Which payment details should be maintained?'
        '</div>',
        unsafe_allow_html=True
    )

    for option in PAYMENT_DETAILS_OPTIONS:

        st.checkbox(
            option,
            key=f"payment_details_{option}"
        )


    # QUESTION 5

    st.markdown(
        '<div class="question-title">'
        'Q5. Who is responsible for the payment or activity?'
        '</div>',
        unsafe_allow_html=True
    )

    for option in RESPONSIBILITY_OPTIONS:

        st.checkbox(
            option,
            key=f"responsibility_{option}"
        )


    # QUESTION 6

    st.markdown(
        '<div class="question-title">'
        'Q6. What information should staff be able to add or update?'
        '</div>',
        unsafe_allow_html=True
    )

    for option in ADD_OPTIONS:

        st.checkbox(
            option,
            key=f"add_{option}"
        )


    # QUESTION 7

    st.markdown(
        '<div class="question-title">'
        'Q7. What additional features or improvements would you suggest for Campus Sphere?'
        '</div>',
        unsafe_allow_html=True
    )

    st.text_area(
        "Your suggestions",
        key="staff_suggestions",
        height=150
    )


    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "💜 Rewind",
            use_container_width=True
        ):

            go_to("staff_details")
            st.rerun()

    with col2:

        if st.button(
            "💜 Submit Response",
            type="primary",
            use_container_width=True
        ):

            response = {

                "Submitted At":
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),

                "User Type":
                    "Staff",

                # STAFF DETAILS

                "Staff Name":
                    st.session_state.staff_name,

                "Staff ID":
                    st.session_state.staff_id,

                "Department":
                    st.session_state.staff_department,

                "Designation":
                    st.session_state.staff_designation,

                # QUESTIONS

                "Q1 - Campus Information Managed":
                    get_checked(
                        "manage",
                        MANAGE_OPTIONS
                    ),

                "Q2 - Regular Updates":
                    get_checked(
                        "update",
                        UPDATE_OPTIONS
                    ),

                "Q3 - Payment Information":
                    get_checked(
                        "payment",
                        PAYMENT_OPTIONS
                    ),

                "Q4 - Payment Details":
                    get_checked(
                        "payment_details",
                        PAYMENT_DETAILS_OPTIONS
                    ),

                "Q5 - Responsibility":
                    get_checked(
                        "responsibility",
                        RESPONSIBILITY_OPTIONS
                    ),

                "Q6 - Information Added / Updated":
                    get_checked(
                        "add",
                        ADD_OPTIONS
                    ),

                "Q7 - Additional Features / Improvements":
                    st.session_state.staff_suggestions
            }

            success, message = send_to_google_sheet(response)

            if success:

                st.success(
                    "💜 Your response has been submitted successfully!"
                )

            else:

                st.error(
                    "❌ Unable to submit the response."
                )

                st.code(message)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 💜 Campus Sphere")

    st.divider()

    if st.button(
        "🏠 Welcome",
        use_container_width=True
    ):

        go_to("welcome")
        st.rerun()

    st.divider()

    st.caption(
        "Responses are submitted securely to the connected Google Sheet."
    )
