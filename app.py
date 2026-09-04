import streamlit as st
import csv
from io import StringIO

# ==================================================
# CAMPUS SPHERE
# ==================================================

st.set_page_config(
    page_title="Campus Sphere",
    page_icon="🎓",
    layout="centered"
)

# ==================================================
# STYLE
# ==================================================

st.markdown("""
<style>
.stApp {
    background-color: #FAF7FF;
}

.main-title {
    text-align: center;
    color: #4B248F;
    font-size: 32px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #321567;
    font-size: 15px;
}

.section-title {
    color: #321567;
    font-size: 21px;
    font-weight: bold;
}

div.stButton > button {
    background-color: #4B248F;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #321567;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

st.markdown(
    '<div class="main-title">🎓 CAMPUS SPHERE ♡</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Student Information & Preferences Form</div>',
    unsafe_allow_html=True
)

st.divider()

# ==================================================
# SESSION STATE
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = 0

if "user_type" not in st.session_state:
    st.session_state.user_type = ""

if "submitted" not in st.session_state:
    st.session_state.submitted = False

# ==================================================
# PAGE 0 - WELCOME
# ==================================================

if st.session_state.page == 0:

    st.markdown(
        "<h2 style='text-align:center;color:#4B248F;'>"
        "Welcome to Campus Sphere"
        "</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;color:#777777;'>"
        "Your campus information, all in one place."
        "</p>",
        unsafe_allow_html=True
    )

    if st.button(
        "✨ Enter the Sphere",
        use_container_width=True,
        key="welcome_button"
    ):
        st.session_state.page = 1
        st.rerun()

# ==================================================
# PAGE 1 - USER TYPE
# ==================================================

elif st.session_state.page == 1:

    st.markdown(
        '<div class="section-title">Who are you?</div>',
        unsafe_allow_html=True
    )

    st.write("Select your user type to continue.")

    if st.button(
        "🎓 Student",
        use_container_width=True,
        key="student_button"
    ):
        st.session_state.user_type = "Student"
        st.session_state.page = 2
        st.rerun()

    if st.button(
        "👩‍🏫 Staff",
        use_container_width=True,
        key="staff_button"
    ):
        st.session_state.user_type = "Staff"
        st.session_state.page = 6
        st.rerun()

# ==================================================
# STUDENT PAGE 1
# ==================================================

elif st.session_state.page == 2:

    st.markdown(
        '<div class="section-title">🎓 Student Details</div>',
        unsafe_allow_html=True
    )

    st.caption("Page 1 of 4")

    name = st.text_input(
        "1. Name (Required)",
        key="student_name_input"
    )

    email = st.text_input(
        "2. Email ID (Optional)",
        key="student_email_input"
    )

    register = st.text_input(
        "3. Register Number (Optional)",
        key="student_register_input"
    )

    department = st.selectbox(
        "4. Department (Required)",
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
        key="student_department_input"
    )

    year = st.selectbox(
        "5. Year of Study (Required)",
        [
            "Select Year",
            "1st Year",
            "2nd Year",
            "3rd Year"
        ],
        key="student_year_input"
    )

    if st.button(
        "Discover 💜 ➜",
        use_container_width=True,
        key="student_page1_next"
    ):

        if name.strip() == "":
            st.warning("Please enter your Name.")

        elif department == "Select Department":
            st.warning("Please select your Department.")

        elif year == "Select Year":
            st.warning("Please select your Year of Study.")

        else:
            st.session_state.student_name = name
            st.session_state.student_email = email
            st.session_state.student_register = register
            st.session_state.student_department = department
            st.session_state.student_year = year

            st.session_state.page = 3
            st.rerun()

# ==================================================
# STUDENT PAGE 2
# ==================================================

elif st.session_state.page == 3:

    st.markdown(
        '<div class="section-title">'
        '📚 Academic, Examination, Timetables, Notices & Events'
        '</div>',
        unsafe_allow_html=True
    )

    st.caption("Page 2 of 4")

    academic = st.multiselect(
        "6. Which academic information would you like to access through Campus Sphere?",
        [
            "All",
            "Class Notes",
            "Study Materials",
            "Assignments",
            "Other Academic Information"
        ],
        key="academic_question"
    )

    exam = st.multiselect(
        "7. Which examination-related information would you like to receive through Campus Sphere?",
        [
            "All",
            "Internal Exams",
            "Model Exams",
            "Semester Exams",
            "Exam Timetable"
        ],
        key="exam_question"
    )

    timetable = st.multiselect(
        "8. Which timetable and regular academic updates would you like to access?",
        [
            "All",
            "Class Timetable",
            "Exam Timetable",
            "Academic Schedule"
        ],
        key="timetable_question"
    )

    notice = st.multiselect(
        "9. Which notices and announcements would you like to receive?",
        [
            "All",
            "College Notices",
            "Department Notices",
            "Important Announcements"
        ],
        key="notice_question"
    )

    event = st.multiselect(
        "10. Which events and activities would you like to know about?",
        [
            "All",
            "Department Events",
            "Other Department Events",
            "College Events"
        ],
        key="event_question"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "⏪ Rewind",
            use_container_width=True,
            key="student_page2_back"
        ):
            st.session_state.page = 2
            st.rerun()

    with col2:
        if st.button(
            "Discover 💜 ➜",
            use_container_width=True,
            key="student_page2_next"
        ):
            st.session_state.academic = academic
            st.session_state.exam = exam
            st.session_state.timetable = timetable
            st.session_state.notice = notice
            st.session_state.event = event

            st.session_state.page = 4
            st.rerun()

# ==================================================
# STUDENT PAGE 3
# ==================================================

elif st.session_state.page == 4:

    st.markdown(
        '<div class="section-title">'
        '🏆 Opportunities, Learning & Skills'
        '</div>',
        unsafe_allow_html=True
    )

    st.caption("Page 3 of 4")

    competition = st.multiselect(
        "11. Which competitions would you like to receive information about?",
        [
            "All",
            "Department Competitions",
            "Inter-Department Competitions",
            "College Competitions",
            "Technical & Cultural Competitions"
        ],
        key="competition_question"
    )

    result = st.multiselect(
        "12. What event and competition results would you like to know?",
        [
            "All",
            "Prize Winners",
            "Winning Department",
            "Individual Achievements",
            "Awards & Recognitions"
        ],
        key="result_question"
    )

    learning = st.multiselect(
        "13. Which seminars, workshops and learning programs interest you?",
        [
            "All",
            "Seminars",
            "Workshops",
            "Training Programs",
            "Career & Skill Programs"
        ],
        key="learning_question"
    )

    skill = st.multiselect(
        "14. Which skills or courses are you interested in learning or improving?",
        [
            "All",
            "Technical Skills",
            "Communication Skills",
            "Career Skills",
            "Other Skills / Courses"
        ],
        key="skill_question"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "⏪ Rewind",
            use_container_width=True,
            key="student_page3_back"
        ):
            st.session_state.page = 3
            st.rerun()

    with col2:
        if st.button(
            "Discover 💜 ➜",
            use_container_width=True,
            key="student_page3_next"
        ):
            st.session_state.competition = competition
            st.session_state.result = result
            st.session_state.learning = learning
            st.session_state.skill = skill

            st.session_state.page = 5
            st.rerun()

# ==================================================
# STUDENT PAGE 4
# ==================================================

elif st.session_state.page == 5:

    st.markdown(
        '<div class="section-title">💌 Suggestions</div>',
        unsafe_allow_html=True
    )

    st.caption("Page 4 of 4")

    suggestion = st.text_area(
        "15. What other information, skills, courses or campus activities would you like to see in Campus Sphere?",
        height=150,
        key="student_suggestion_input"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "⏪ Rewind",
            use_container_width=True,
            key="student_page4_back"
        ):
            st.session_state.page = 4
            st.rerun()

    with col2:
        if st.button(
            "✓ Submit 💜",
            use_container_width=True,
            key="student_submit"
        ):
            st.session_state.student_suggestion = suggestion
            st.session_state.submitted = True

    if st.session_state.submitted:
        st.success("Your response has been recorded successfully! 💜")

        st.markdown(
            "<h3 style='text-align:center;color:#4B248F;'>"
            "Thank You! ♡"
            "</h3>",
            unsafe_allow_html=True
        )

# ==================================================
# STAFF PAGE 1
# ==================================================

elif st.session_state.page == 6:

    st.markdown(
        '<div class="section-title">👩‍🏫 Staff Details</div>',
        unsafe_allow_html=True
    )

    st.caption("Staff Page 1 of 3")

    staff_name = st.text_input(
        "Staff Name (Required)",
        key="staff_name_input"
    )

    staff_id = st.text_input(
        "Staff ID (Required)",
        key="staff_id_input"
    )

    staff_department = st.selectbox(
        "Department (Required)",
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
        key="staff_department_input"
    )

    designation = st.selectbox(
        "Designation (Required)",
        [
            "Select Designation",
            "Assistant Professor",
            "Associate Professor",
            "Professor",
            "Head of Department",
            "Coordinator",
            "Other"
        ],
        key="designation_input"
    )

    if st.button(
        "Discover 💜 ➜",
        use_container_width=True,
        key="staff_page1_next"
    ):

        if staff_name.strip() == "":
            st.warning("Please enter Staff Name.")

        elif staff_id.strip() == "":
            st.warning("Please enter Staff ID.")

        elif staff_department == "Select Department":
            st.warning("Please select Department.")

        elif designation == "Select Designation":
            st.warning("Please select Designation.")

        else:
            st.session_state.staff_name = staff_name
            st.session_state.staff_id = staff_id
            st.session_state.staff_department = staff_department
            st.session_state.designation = designation

            st.session_state.page = 7
            st.rerun()

# ==================================================
# STAFF PAGE 2
# ==================================================

elif st.session_state.page == 7:

    st.markdown(
        '<div class="section-title">'
        '📋 Campus Management & Updates'
        '</div>',
        unsafe_allow_html=True
    )

    st.caption("Staff Page 2 of 3")

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
        ],
        key="staff_manage_question"
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
        ],
        key="staff_update_question"
    )

    staff_payment = st.multiselect(
        "3. Which college-related payment information should be maintained?",
        [
            "Department Event Fees",
            "Cultural Event Fees",
            "Competition Fees",
            "Other College Fees"
        ],
        key="staff_payment_question"
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
        ],
        key="staff_payment_details_question"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "⏪ Rewind",
            use_container_width=True,
            key="staff_page2_back"
        ):
            st.session_state.page = 6
            st.rerun()

    with col2:
        if st.button(
            "Discover 💜 ➜",
            use_container_width=True,
            key="staff_page2_next"
        ):
            st.session_state.staff_manage = staff_manage
            st.session_state.staff_update = staff_update
            st.session_state.staff_payment = staff_payment
            st.session_state.staff_payment_details = staff_payment_details

            st.session_state.page = 8
            st.rerun()

# ==================================================
# STAFF PAGE 3
# ==================================================

elif st.session_state.page == 8:

    st.markdown(
        '<div class="section-title">'
        '📚 Responsibilities, Updates & Suggestions'
        '</div>',
        unsafe_allow_html=True
    )

    st.caption("Staff Page 3 of 3")

    responsibility = st.multiselect(
        "5. Who is responsible for the payment or activity?",
        [
            "Staff",
            "Student",
            "Department Coordinator",
            "Other"
        ],
        key="responsibility_question"
    )

    add_update = st.multiselect(
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
        ],
        key="staff_add_update_question"
    )

    staff_suggestion = st.text_area(
        "7. What additional features or improvements would you suggest for Campus Sphere?",
        height=150,
        key="staff_suggestion_input"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "⏪ Rewind",
            use_container_width=True,
            key="staff_page3_back"
        ):
            st.session_state.page = 7
            st.rerun()

    with col2:
        if st.button(
            "✓ Submit 💜",
            use_container_width=True,
            key="staff_submit"
        ):
            st.session_state.staff_responsibility = responsibility
            st.session_state.staff_add_update = add_update
            st.session_state.staff_suggestion = staff_suggestion
            st.session_state.submitted = True

    if st.session_state.submitted:
        st.success("Your response has been recorded successfully! 💜")

        st.markdown(
            "<h3 style='text-align:center;color:#4B248F;'>"
            "Thank You! ♡"
            "</h3>",
            unsafe_allow_html=True
        )

# ==================================================
# CSV DOWNLOAD
# ==================================================

if st.session_state.submitted:

    headers = [
        "User Type",
        "Name",
        "Email ID",
        "Register Number",
        "Department",
        "Year of Study",
        "Staff ID",
        "Designation",
        "Academic Information",
        "Examination Information",
        "Timetable & Academic Updates",
        "Notices & Announcements",
        "Events & Activities",
        "Competitions",
        "Event & Competition Results",
        "Seminars, Workshops & Learning Programs",
        "Skills / Courses",
        "Student Suggestions",
        "Staff Information Managed",
        "Staff Regular Updates",
        "Staff Payment Information",
        "Staff Payment Details",
        "Staff Responsibility",
        "Staff Information Added / Updated",
        "Staff Suggestions"
    ]

    if st.session_state.user_type == "Student":

        data = [
            "Student",
            st.session_state.get("student_name", ""),
            st.session_state.get("student_email", ""),
            st.session_state.get("student_register", ""),
            st.session_state.get("student_department", ""),
            st.session_state.get("student_year", ""),
            "",
            "",
            ", ".join(st.session_state.get("academic", [])),
            ", ".join(st.session_state.get("exam", [])),
            ", ".join(st.session_state.get("timetable", [])),
            ", ".join(st.session_state.get("notice", [])),
            ", ".join(st.session_state.get("event", [])),
            ", ".join(st.session_state.get("competition", [])),
            ", ".join(st.session_state.get("result", [])),
            ", ".join(st.session_state.get("learning", [])),
            ", ".join(st.session_state.get("skill", [])),
            st.session_state.get("student_suggestion", ""),
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ]

    else:

        data = [
            "Staff",
            st.session_state.get("staff_name", ""),
            "",
            "",
            st.session_state.get("staff_department", ""),
            "",
            st.session_state.get("staff_id", ""),
            st.session_state.get("designation", ""),
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ", ".join(st.session_state.get("staff_manage", [])),
            ", ".join(st.session_state.get("staff_update", [])),
            ", ".join(st.session_state.get("staff_payment", [])),
            ", ".join(st.session_state.get("staff_payment_details", [])),
            ", ".join(st.session_state.get("staff_responsibility", [])),
            ", ".join(st.session_state.get("staff_add_update", [])),
            st.session_state.get("staff_suggestion", "")
        ]

    output = StringIO()

    writer = csv.writer(output)
    writer.writerow(headers)
    writer.writerow(data)

    st.divider()

    st.markdown(
        "<h4 style='text-align:center;color:#4B248F;'>"
        "📊 Your Response"
        "</h4>",
        unsafe_allow_html=True
    )
