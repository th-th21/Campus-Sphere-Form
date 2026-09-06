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

GOOGLE_SCRIPT_URL = ("https://script.google.com/macros/s/AKfycbxjls2H6bZtwwdHMfU1eiuwpEWMJvxwoN5ouWrAKKQITOuf26tH6UbICI0cyKSpFR9jkw/exec")
PURPLE = "#4B248F"


# ============================================================
# STUDENT OPTIONS
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


# ============================================================
# STAFF OPTIONS
# ============================================================

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
# DESIGN
# ============================================================

st.markdown(
    f"""
    <style>

    .main-title {{
        color: {PURPLE};
        text-align: center;
        font-size: 46px;
        font-weight: bold;
        margin-top: 25px;
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
# SESSION STATE
# ============================================================

defaults = {

    # Navigation
    "page": "welcome",

    # Student details
    "student_name": "",
    "student_email": "",
    "student_register": "",
    "student_department": "Select Department",
    "student_year": "Select Year",

    # Student questions
    "student_q6": [],
    "student_q7": [],
    "student_q8": [],
    "student_q9": [],
    "student_q10": [],
    "student_q11": [],
    "student_q12": [],
    "student_q13": [],
    "student_q14": [],
    "student_q15": "",

    # Staff details
    "staff_name": "",
    "staff_id": "",
    "staff_department": "",
    "staff_designation": "Select Designation",

    # Staff questions
    "staff_q1": [],
    "staff_q2": [],
    "staff_q3": [],
    "staff_q4": [],
    "staff_q5": [],
    "staff_q6": [],
    "staff_q7": ""
}

for key, value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# NAVIGATION
# ============================================================

def go_to(page):

    st.session_state.page = page


# ============================================================
# ANSWER FUNCTION
# ============================================================

def answer(value):

    if not value:
        return "None"

    return ", ".join(value)


# ============================================================
# SEND RESPONSE TO GOOGLE SHEETS
# ============================================================

def send_to_google_sheet(data):

    try:

        json_data = json.dumps(data).encode("utf-8")

        request = urllib.request.Request(
            GOOGLE_SCRIPT_URL,
            data=json_data,
            headers={
                "Content-Type": "application/json"
            },
            method="POST"
        )

        with urllib.request.urlopen(
            request,
            timeout=30
        ) as response:

            result = response.read().decode("utf-8")

        return True, result

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

    st.write("")

    st.markdown(
        """
        <div style="
            text-align:center;
            font-size:18px;
            line-height:1.7;
        ">

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
# USER TYPE PAGE
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
# STUDENT PAGE 1 — DETAILS
# ============================================================

elif st.session_state.page == "student_details":

    st.markdown(
        '<div class="section-title">🎓 Student Details</div>',
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
            "💜 Discover",
            type="primary",
            use_container_width=True
        ):

            if not st.session_state.student_name.strip():

                st.error("Please enter your Name.")

            elif (
                st.session_state.student_department
                == "Select Department"
            ):

                st.error("Please select your Department.")

            elif (
                st.session_state.student_year
                == "Select Year"
            ):

                st.error("Please select your Year of Study.")

            else:

                go_to("student_academic")
                st.rerun()


# ============================================================
# STUDENT PAGE 2 — ACADEMIC & CAMPUS
# ============================================================

elif st.session_state.page == "student_academic":

    st.markdown(
        '<div class="section-title">'
        '📚 Academic & Campus Information'
        '</div>',
        unsafe_allow_html=True
    )

    # QUESTION 6

    st.subheader("Academic Information")

    st.multiselect(
        "6. Which academic information would you like to access through Campus Sphere?",
        ACADEMIC_OPTIONS,
        key="student_q6"
    )

    # QUESTION 7

    st.multiselect(
        "7. Which examination-related information would you like to receive through Campus Sphere?",
        EXAM_OPTIONS,
        key="student_q7"
    )

    # QUESTION 8

    st.multiselect(
        "8. Which timetable and regular academic updates would you like to access?",
        TIMETABLE_OPTIONS,
        key="student_q8"
    )

    # QUESTION 9

    st.multiselect(
        "9. Which notices and announcements would you like to receive?",
        NOTICE_OPTIONS,
        key="student_q9"
    )

    # QUESTION 10

    st.multiselect(
        "10. Which events and activities would you like to know about?",
        EVENT_OPTIONS,
        key="student_q10"
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
            "💜 Discover",
            type="primary",
            use_container_width=True
        ):

            go_to("student_opportunities")
            st.rerun()


# ============================================================
# STUDENT PAGE 3 — OPPORTUNITIES, LEARNING & SKILLS
# ============================================================

elif st.session_state.page == "student_opportunities":

    st.markdown(
        '<div class="section-title">'
        '🏆 Opportunities, Learning & Skills'
        '</div>',
        unsafe_allow_html=True
    )

    # QUESTION 11

    st.multiselect(
        "11. Which competitions would you like to receive information about?",
        COMPETITION_OPTIONS,
        key="student_q11"
    )

    # QUESTION 12

    st.multiselect(
        "12. What event and competition results would you like to know?",
        RESULT_OPTIONS,
        key="student_q12"
    )

    # QUESTION 13

    st.multiselect(
        "13. Which seminars, workshops and learning programs interest you?",
        LEARNING_OPTIONS,
        key="student_q13"
    )

    # QUESTION 14

    st.multiselect(
        "14. Which skills or courses are you interested in learning or improving?",
        SKILL_OPTIONS,
        key="student_q14"
    )

    # QUESTION 15

    st.text_area(
        "15. What other information, skills, courses or campus activities would you like to see in Campus Sphere?",
        key="student_q15",
        height=150
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "💜 Rewind",
            use_container_width=True
        ):

            go_to("student_academic")
            st.rerun()

    with col2:

        if st.button(
            "💜 Submit Response",
            type="primary",
            use_container_width=True
        ):

            student_response = {

                "Submitted At":
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),

                "User Type":
                    "Student",

                "Name":
                    st.session_state.student_name.strip(),

                "Email ID":
                    st.session_state.student_email.strip(),

                "Register Number":
                    st.session_state.student_register.strip(),

                "Department":
                    st.session_state.student_department,

                "Year of Study":
                    st.session_state.student_year,

                "Q6 - Academic Information":
                    answer(st.session_state.student_q6),

                "Q7 - Examination Information":
                    answer(st.session_state.student_q7),

                "Q8 - Timetable & Academic Updates":
                    answer(st.session_state.student_q8),

                "Q9 - Notices & Announcements":
                    answer(st.session_state.student_q9),

                "Q10 - Events & Activities":
                    answer(st.session_state.student_q10),

                "Q11 - Competitions":
                    answer(st.session_state.student_q11),

                "Q12 - Competition Results":
                    answer(st.session_state.student_q12),

                "Q13 - Seminars / Workshops / Learning":
                    answer(st.session_state.student_q13),

                "Q14 - Skills / Courses":
                    answer(st.session_state.student_q14),

                "Q15 - Other Information / Suggestions":
                    st.session_state.student_q15.strip()
            }

            success, message = send_to_google_sheet(
                student_response
            )

            if success:

                st.success(
                    "💜 Your student response has been submitted successfully!"
                )

                st.balloons()

            else:

                st.error(
                    "❌ Unable to submit the response."
                )

                st.code(message)


# ============================================================
# STAFF PAGE 1 — DETAILS
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
            "💜 Discover",
            type="primary",
            use_container_width=True
        ):

            if not st.session_state.staff_name.strip():

                st.error("Please enter Staff Name.")

            elif not st.session_state.staff_id.strip():

                st.error("Please enter Staff ID.")

            elif not st.session_state.staff_department.strip():

                st.error("Please enter Department.")

            elif (
                st.session_state.staff_designation
                == "Select Designation"
            ):

                st.error("Please select Designation.")

            else:

                go_to("staff_management")
                st.rerun()


# ============================================================
# STAFF PAGE 2 — CAMPUS MANAGEMENT & UPDATES
# ============================================================

elif st.session_state.page == "staff_management":

    st.markdown(
        '<div class="section-title">'
        '🏫 Campus Management & Updates'
        '</div>',
        unsafe_allow_html=True
    )

    # QUESTION 1

    st.multiselect(
        "1. Which campus information would you like to update or manage?",
        MANAGE_OPTIONS,
        key="staff_q1"
    )

    # QUESTION 2

    st.multiselect(
        "2. Which updates should be regularly communicated to students?",
        UPDATE_OPTIONS,
        key="staff_q2"
    )

    # QUESTION 3

    st.multiselect(
        "3. Which college-related payment information should be maintained?",
        PAYMENT_OPTIONS,
        key="staff_q3"
    )

    # QUESTION 4

    st.multiselect(
        "4. Which payment details should be maintained?",
        PAYMENT_DETAILS_OPTIONS,
        key="staff_q4"
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
            "💜 Discover",
            type="primary",
            use_container_width=True
        ):

            go_to("staff_responsibilities")
            st.rerun()


# ============================================================
# STAFF PAGE 3 — RESPONSIBILITIES & SUGGESTIONS
# ============================================================

elif st.session_state.page == "staff_responsibilities":

    st.markdown(
        '<div class="section-title">'
        '📚 Responsibilities & Suggestions'
        '</div>',
        unsafe_allow_html=True
    )

    # QUESTION 5

    st.multiselect(
        "5. Who is responsible for the payment or activity?",
        RESPONSIBILITY_OPTIONS,
        key="staff_q5"
    )

    # QUESTION 6

    st.multiselect(
        "6. What information should staff be able to add or update?",
        ADD_OPTIONS,
        key="staff_q6"
    )

    # QUESTION 7

    st.text_area(
        "7. What additional features or improvements would you suggest for Campus Sphere?",
        key="staff_q7",
        height=150
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "💜 Rewind",
            use_container_width=True
        ):

            go_to("staff_management")
            st.rerun()

    with col2:

        if st.button(
            "💜 Submit Response",
            type="primary",
            use_container_width=True
        ):

            staff_response = {

                "Submitted At":
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),

                "User Type":
                    "Staff",

                "Staff Name":
                    st.session_state.staff_name.strip(),

                "Staff ID":
                    st.session_state.staff_id.strip(),

                "Department":
                    st.session_state.staff_department.strip(),

                "Designation":
                    st.session_state.staff_designation,

                "Q1 - Campus Information to Manage":
                    answer(st.session_state.staff_q1),

                "Q2 - Regular Student Updates":
                    answer(st.session_state.staff_q2),

                "Q3 - College Payment Information":
                    answer(st.session_state.staff_q3),

                "Q4 - Payment Details":
                    answer(st.session_state.staff_q4),

                "Q5 - Responsibility":
                    answer(st.session_state.staff_q5),

                "Q6 - Information to Add / Update":
                    answer(st.session_state.staff_q6),

                "Q7 - Additional Features / Improvements":
                    st.session_state.staff_q7.strip()
            }

            success, message = send_to_google_sheet(
                staff_response
            )

            if success:

                st.success(
                    "💜 Your staff response has been submitted successfully!"
                )
