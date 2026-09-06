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

PURPLE = "#4B248F"


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
    "page": "welcome",

    "student_name": "",
    "student_email": "",
    "student_register": "",
    "student_department": "Select Department",
    "student_year": "Select Year",

    "staff_name": "",
    "staff_id": "",
    "staff_department": "",
    "staff_designation": "Select Designation"
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
# GET MULTI-SELECT ANSWER
# ============================================================

def answer(value):
    if not value:
        return "None"
    return ", ".join(value)


# ============================================================
# SEND TO GOOGLE SHEET
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
# WELCOME
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
        <div style="text-align:center;font-size:18px;line-height:1.7;">
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
# USER TYPE
# ============================================================

elif st.session_state.page == "user_type":

    st.markdown(
        '<div class="section-title">Choose Your Category</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "👨‍🎓 Student",
            use_container_width=True
        ):

            go_to("student")
            st.rerun()

    with col2:

        if st.button(
            "👩‍🏫 Staff",
            use_container_width=True
        ):

            go_to("staff")
            st.rerun()

    st.write("")

    if st.button("💜 Rewind", use_container_width=True):

        go_to("welcome")
        st.rerun()


# ============================================================
# STUDENT FORM
# ============================================================

elif st.session_state.page == "student":

    st.markdown(
        '<div class="section-title">🎓 STUDENT FORM</div>',
        unsafe_allow_html=True
    )

    st.caption("Please answer all required questions.")

    # --------------------------------------------------------
    # STUDENT DETAILS
    # --------------------------------------------------------

    st.subheader("Student Details")

    name = st.text_input(
        "1. Name *",
        key="student_name"
    )

    email = st.text_input(
        "2. Email ID",
        key="student_email"
    )

    register_number = st.text_input(
        "3. Register Number",
        key="student_register"
    )

    department = st.selectbox(
        "4. Department *",
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

    year = st.selectbox(
        "5. Year of Study *",
        [
            "Select Year",
            "1st Year",
            "2nd Year",
            "3rd Year"
        ],
        key="student_year"
    )

    # --------------------------------------------------------
    # QUESTION 6
    # --------------------------------------------------------

    st.subheader("📚 Academic & Campus Information")

    q6 = st.multiselect(
        "6. Which academic information would you like to access through Campus Sphere?",
        ACADEMIC_OPTIONS,
        key="student_q6"
    )

    # --------------------------------------------------------
    # QUESTION 7
    # --------------------------------------------------------

    q7 = st.multiselect(
        "7. Which examination-related information would you like to receive through Campus Sphere?",
        EXAM_OPTIONS,
        key="student_q7"
    )

    # --------------------------------------------------------
    # QUESTION 8
    # --------------------------------------------------------

    q8 = st.multiselect(
        "8. Which timetable and regular academic updates would you like to access?",
        TIMETABLE_OPTIONS,
        key="student_q8"
    )

    # --------------------------------------------------------
    # QUESTION 9
    # --------------------------------------------------------

    q9 = st.multiselect(
        "9. Which notices and announcements would you like to receive?",
        NOTICE_OPTIONS,
        key="student_q9"
    )

    # --------------------------------------------------------
    # QUESTION 10
    # --------------------------------------------------------

    q10 = st.multiselect(
        "10. Which events and activities would you like to know about?",
        EVENT_OPTIONS,
        key="student_q10"
    )

    # --------------------------------------------------------
    # QUESTION 11
    # --------------------------------------------------------

    st.subheader("🏆 Opportunities, Learning & Skills")

    q11 = st.multiselect(
        "11. Which competitions would you like to receive information about?",
        COMPETITION_OPTIONS,
        key="student_q11"
    )

    # --------------------------------------------------------
    # QUESTION 12
    # --------------------------------------------------------

    q12 = st.multiselect(
        "12. What event and competition results would you like to know?",
        RESULT_OPTIONS,
        key="student_q12"
    )

    # --------------------------------------------------------
    # QUESTION 13
    # --------------------------------------------------------

    q13 = st.multiselect(
        "13. Which seminars, workshops and learning programs interest you?",
        LEARNING_OPTIONS,
        key="student_q13"
    )

    # --------------------------------------------------------
    # QUESTION 14
    # --------------------------------------------------------

    q14 = st.multiselect(
        "14. Which skills or courses are you interested in learning or improving?",
        SKILL_OPTIONS,
        key="student_q14"
    )

    # --------------------------------------------------------
    # QUESTION 15
    # --------------------------------------------------------

    q15 = st.text_area(
        "15. What other information, skills, courses or campus activities would you like to see in Campus Sphere?",
        key="student_q15",
        height=130
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
            "💜 Submit Student Response",
            type="primary",
            use_container_width=True
        ):

            # REQUIRED FIELD CHECK

            if not name.strip():

                st.error("Please enter your Name.")

            elif department == "Select Department":

                st.error("Please select your Department.")

            elif year == "Select Year":

                st.error("Please select your Year of Study.")

            else:

                student_response = {

                    "Submitted At":
                        datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        ),

                    "User Type":
                        "Student",

                    "Name":
                        name.strip(),

                    "Email ID":
                        email.strip(),

                    "Register Number":
                        register_number.strip(),

                    "Department":
                        department,

                    "Year of Study":
                        year,

                    "Q6 - Academic Information":
                        answer(q6),

                    "Q7 - Examination Information":
                        answer(q7),

                    "Q8 - Timetable & Academic Updates":
                        answer(q8),

                    "Q9 - Notices & Announcements":
                        answer(q9),

                    "Q10 - Events & Activities":
                        answer(q10),

                    "Q11 - Competitions":
                        answer(q11),

                    "Q12 - Competition Results":
                        answer(q12),

                    "Q13 - Seminars / Workshops / Learning":
                        answer(q13),

                    "Q14 - Skills / Courses":
                        answer(q14),

                    "Q15 - Other Information / Suggestions":
                        q15.strip()
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
# STAFF FORM
# ============================================================

elif st.session_state.page == "staff":

    st.markdown(
        '<div class="section-title">👩‍🏫 STAFF FORM</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # STAFF DETAILS
    # --------------------------------------------------------

    st.subheader("Staff Details")

    staff_name = st.text_input(
        "Staff Name *",
        key="staff_name"
    )

    staff_id = st.text_input(
        "Staff ID *",
        key="staff_id"
    )

    staff_department = st.text_input(
        "Department *",
        key="staff_department"
    )

    staff_designation = st.selectbox(
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

    # --------------------------------------------------------
    # STAFF QUESTION 1
    # --------------------------------------------------------

    st.subheader("🏫 Campus Management & Updates")

    sq1 = st.multiselect(
        "1. Which campus information would you like to update or manage?",
        MANAGE_OPTIONS,
        key="staff_q1"
    )

    # --------------------------------------------------------
    # STAFF QUESTION 2
    # --------------------------------------------------------

    sq2 = st.multiselect(
        "2. Which updates should be regularly communicated to students?",
        UPDATE_OPTIONS,
        key="staff_q2"
    )

    # --------------------------------------------------------
    # STAFF QUESTION 3
    # --------------------------------------------------------

    sq3 = st.multiselect(
        "3. Which college-related payment information should be maintained?",
        PAYMENT_OPTIONS,
        key="staff_q3"
    )

    # --------------------------------------------------------
    # STAFF QUESTION 4
    # --------------------------------------------------------

    sq4 = st.multiselect(
        "4. Which payment details should be maintained?",
        PAYMENT_DETAILS_OPTIONS,
        key="staff_q4"
    )

    # --------------------------------------------------------
    # STAFF QUESTION 5
    # --------------------------------------------------------

    st.subheader("📚 Responsibilities & Suggestions")

    sq5 = st.multiselect(
        "5. Who is responsible for the payment or activity?",
        RESPONSIBILITY_OPTIONS,
        key="staff_q5"
    )

    # --------------------------------------------------------
    # STAFF QUESTION 6
    # --------------------------------------------------------

    sq6 = st.multiselect(
        "6. What information should staff be able to add or update?",
        ADD_OPTIONS,
        key="staff_q6"
    )

    # --------------------------------------------------------
    # STAFF QUESTION 7
    # --------------------------------------------------------

    sq7 = st.text_area(
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

            go_to("user_type")
            st.rerun()

    with col2:

        if st.button(
            "💜 Submit Staff Response",
            type="primary",
            use_container_width=True
        ):

            if not staff_name.strip():

                st.error("Please enter Staff Name.")

            elif not staff_id.strip():

                st.error("Please enter Staff ID.")

            elif not staff_department.strip():

                st.error("Please enter Department.")

            elif staff_designation == "Select Designation":

                st.error("Please select Designation.")

            else:

                staff_response = {

                    "Submitted At":
                        datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        ),

                    "User Type":
                        "Staff",

                    "Staff Name":
                        staff_name.strip(),

                    "Staff ID":
                        staff_id.strip(),

                    "Department":
                        staff_department.strip(),

                    "Designation":
                        staff_designation,

                    "Q1 - Campus Information to Manage":
                        answer(sq1),

                    "Q2 - Regular Student Updates":
                        answer(sq2),

                    "Q3 - College Payment Information":
                        answer(sq3),

                    "Q4 - Payment Details":
                        answer(sq4),

                    "Q5 - Responsibility":
                        answer(sq5),

                    "Q6 - Information to Add / Update":
                        answer(sq6),

                    "Q7 - Additional Features / Improvements":
                        sq7.strip()
                }

                success, message = send_to_google_sheet(
                    staff_response
                )

                if success:

                    st.success(
                        "💜 Your staff response has been submitted successfully!"
                    )

                    st.balloons()

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
        "Responses are submitted to the connected Google Sheet."
    )V
