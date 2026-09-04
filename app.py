import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime

# ============================================================
# CAMPUS SPHERE - STREAMLIT VERSION
# ============================================================

st.set_page_config(
    page_title="Campus Sphere",
    page_icon="🎓",
    layout="wide"
)

# ------------------------------------------------------------
# SETTINGS
# ------------------------------------------------------------

DATA_FILE = Path("Campus_Sphere_Responses.csv")

# CHANGE THIS PASSWORD
ADMIN_PASSWORD = "ChangeThisPassword123"

PURPLE = "#4B248F"

# ------------------------------------------------------------
# CSS
# ------------------------------------------------------------

st.markdown(
    f"""
    <style>
    .main-title {{
        color: {PURPLE};
        text-align: center;
        font-size: 42px;
        font-weight: bold;
    }}

    .subtitle {{
        text-align: center;
        color: #666666;
        font-size: 18px;
    }}

    .section-title {{
        color: {PURPLE};
        font-size: 28px;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------------------
# SESSION STATE
# ------------------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "home"

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False


def go_to(page):
    st.session_state.page = page


# ------------------------------------------------------------
# SAVE RESPONSE
# ------------------------------------------------------------

def save_response(data):

    new_data = pd.DataFrame([data])

    if DATA_FILE.exists():
        new_data.to_csv(
            DATA_FILE,
            mode="a",
            header=False,
            index=False
        )
    else:
        new_data.to_csv(
            DATA_FILE,
            index=False
        )


# ------------------------------------------------------------
# CHECKBOX HELPER
# ------------------------------------------------------------

def get_checked(prefix, options):

    selected = []

    for option in options:

        key = f"{prefix}_{option}"

        if st.session_state.get(key, False):
            selected.append(option)

    if selected:
        return ", ".join(selected)

    return "None"


# ============================================================
# HOME PAGE
# ============================================================

if st.session_state.page == "home":

    st.markdown(
        '<div class="main-title">🎓 Campus Sphere</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'College Information & Feedback Portal'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.info(
        "Welcome to Campus Sphere. "
        "Please select your category."
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "👨‍🎓 STUDENT",
            use_container_width=True
        ):

            go_to("student1")
            st.rerun()

    with col2:

        if st.button(
            "👩‍🏫 STAFF",
            use_container_width=True
        ):

            go_to("staff1")
            st.rerun()

    st.divider()

    st.caption(
        "Students and staff cannot access submitted responses."
    )


# ============================================================
# STUDENT PAGE 1
# ============================================================

elif st.session_state.page == "student1":

    st.markdown(
        '<div class="section-title">'
        '👨‍🎓 Student Information'
        '</div>',
        unsafe_allow_html=True
    )

    name = st.text_input(
        "Name *",
        key="student_name"
    )

    email = st.text_input(
        "Email ID",
        key="student_email"
    )

    register = st.text_input(
        "Register Number",
        key="student_register"
    )

    department = st.selectbox(
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

    year = st.selectbox(
        "Year of Study *",
        [
            "Select Year",
            "1st Year",
            "2nd Year",
            "3rd Year"
        ],
        key="student_year"
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("⬅ Back"):

            go_to("home")
            st.rerun()

    with col2:

        if st.button(
            "Next ➡",
            type="primary",
            use_container_width=True
        ):

            if not name.strip():

                st.error("Please enter your name.")

            elif department == "Select Department":

                st.error("Please select your department.")

            elif year == "Select Year":

                st.error("Please select your year.")

            else:

                go_to("student2")
                st.rerun()


# ============================================================
# STUDENT PAGE 2
# ============================================================

elif st.session_state.page == "student2":

    st.markdown(
        '<div class="section-title">'
        '📚 Academic Information'
        '</div>',
        unsafe_allow_html=True
    )

    # Academic Information

    st.subheader("Academic Information")

    academic_options = [
        "All",
        "Class Notes",
        "Study Materials",
        "Assignments",
        "Other Academic Information"
    ]

    cols = st.columns(2)

    for i, option in enumerate(academic_options):

        with cols[i % 2]:

            st.checkbox(
                option,
                key=f"academic_{option}"
            )

    # Exam Information

    st.subheader("Exam Information")

    exam_options = [
        "All",
        "Internal Exams",
        "Model Exams",
        "Semester Exams",
        "Exam Timetable"
    ]

    cols = st.columns(2)

    for i, option in enumerate(exam_options):

        with cols[i % 2]:

            st.checkbox(
                option,
                key=f"exam_{option}"
            )

    # Timetable

    st.subheader("Timetable")

    timetable_options = [
        "All",
        "Class Timetable",
        "Exam Timetable",
        "Academic Schedule"
    ]

    cols = st.columns(2)

    for i, option in enumerate(timetable_options):

        with cols[i % 2]:

            st.checkbox(
                option,
                key=f"timetable_{option}"
            )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("⬅ Back"):

            go_to("student1")
            st.rerun()

    with col2:

        if st.button(
            "Next ➡",
            type="primary",
            use_container_width=True
        ):

            go_to("student3")
            st.rerun()


# ============================================================
# STUDENT PAGE 3
# ============================================================

elif st.session_state.page == "student3":

    st.markdown(
        '<div class="section-title">'
        '📢 College Activities & Updates'
        '</div>',
        unsafe_allow_html=True
    )

    # Notices

    st.subheader("Notices")

    notice_options = [
        "All",
        "College Notices",
        "Department Notices",
        "Important Announcements"
    ]

    cols = st.columns(2)

    for i, option in enumerate(notice_options):

        with cols[i % 2]:

            st.checkbox(
                option,
                key=f"notice_{option}"
            )

    # Events

    st.subheader("Events")

    event_options = [
        "All",
        "Department Events",
        "Other Department Events",
        "College Events"
    ]

    cols = st.columns(2)

    for i, option in enumerate(event_options):

        with cols[i % 2]:

            st.checkbox(
                option,
                key=f"event_{option}"
            )

    # Competitions

    st.subheader("Competitions")

    competition_options = [
        "All",
        "Department Competitions",
        "Inter-Department Competitions",
        "College Competitions",
        "Technical & Cultural Competitions"
    ]

    cols = st.columns(2)

    for i, option in enumerate(competition_options):

        with cols[i % 2]:

            st.checkbox(
                option,
                key=f"competition_{option}"
            )

    # Results

    st.subheader("Results & Achievements")

    result_options = [
        "All",
        "Prize Winners",
        "Winning Department",
        "Individual Achievements",
        "Awards & Recognitions"
    ]

    cols = st.columns(2)

    for i, option in enumerate(result_options):

        with cols[i % 2]:

            st.checkbox(
                option,
                key=f"result_{option}"
            )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("⬅ Back"):

            go_to("student2")
            st.rerun()

    with col2:

        if st.button(
            "Next ➡",
            type="primary",
            use_container_width=True
        ):

            go_to("student4")
            st.rerun()


# ============================================================
# STUDENT PAGE 4
# ============================================================

elif st.session_state.page == "student4":

    st.markdown(
        '<div class="section-title">'
        '🎯 Learning, Skills & Suggestions'
        '</div>',
        unsafe_allow_html=True
    )

    # Learning

    st.subheader(
        "Seminars / Workshops / Learning"
    )

    learning_options = [
        "All",
        "Seminars",
        "Workshops",
        "Training Programs",
        "Career & Skill Programs"
    ]

    cols = st.columns(2)

    for i, option in enumerate(learning_options):

        with cols[i % 2]:

            st.checkbox(
                option,
                key=f"learning_{option}"
            )

    # Skills

    st.subheader("Skills / Courses")

    skill_options = [
        "All",
        "Technical Skills",
        "Communication Skills",
        "Career Skills",
        "Other Skills / Courses"
    ]

    cols = st.columns(2)

    for i, option in enumerate(skill_options):

        with cols[i % 2]:

            st.checkbox(
                option,
                key=f"skill_{option}"
            )

    # Suggestions

    st.subheader("Suggestions")

    suggestions = st.text_area(
        "Your suggestions / additional feedback",
        key="student_suggestions",
        height=150
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("⬅ Back"):

            go_to("student3")
            st.rerun()

    with col2:

        if st.button(
            "✅ Submit Response",
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

                "Name":
                    st.session_state.student_name,

                "Email ID":
                    st.session_state.student_email,

                "Register Number":
                    st.session_state.student_register,

                "Department":
                    st.session_state.student_department,

                "Year":
                    st.session_state.student_year,

                "Academic Information":
                    get_checked(
                        "academic",
                        academic_options
                    ),

                "Exam Information":
                    get_checked(
                        "exam",
                        exam_options
                    ),

                "Timetable":
                    get_checked(
                        "timetable",
                        timetable_options
                    ),

                "Notices":
                    get_checked(
                        "notice",
                        notice_options
                    ),

                "Events":
                    get_checked(
                        "event",
                        event_options
                    ),

                "Competitions":
                    get_checked(
                        "competition",
                        competition_options
                    ),

                "Results":
                    get_checked(
                        "result",
                        result_options
                    ),

                "Seminars / Workshops / Learning":
                    get_checked(
                        "learning",
                        learning_options
                    ),

                "Skills / Courses":
                    get_checked(
                        "skill",
                        skill_options
                    ),

                "Suggestions":
                    suggestions
            }

            save_response(response)

            st.success(
                "✅ Your response has been submitted successfully!"
            )


# ============================================================
# STAFF PAGE 1
# ============================================================

elif st.session_state.page == "staff1":

    st.markdown(
        '<div class="section-title">'
        '👩‍🏫 Staff Information'
        '</div>',
        unsafe_allow_html=True
    )

    name = st.text_input(
        "Staff Name *",
        key="staff_name"
    )

    staff_id = st.text_input(
        "Staff ID *",
        key="staff_id"
    )

    department = st.text_input(
        "Department *",
        key="staff_department"
    )

    designation = st.selectbox(
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

    col1, col2 = st.columns(2)

    with col1:

        if st.button("⬅ Back"):

            go_to("home")
            st.rerun()

    with col2:

        if st.button(
            "Next ➡",
            type="primary",
            use_container_width=True
        ):

            if not name.strip():

                st.error("Please enter staff name.")

            elif not staff_id.strip():

                st.error("Please enter Staff ID.")

            elif not department.strip():

                st.error("Please enter department.")

            elif designation == "Select Designation":

                st.error("Please select designation.")

            else:

                go_to("staff2")
                st.rerun()


# ============================================================
# STAFF PAGE 2
# ============================================================

elif st.session_state.page == "staff2":

    st.markdown(
        '<div class="section-title">'
        '🗂️ Staff Information & Updates'
        '</div>',
        unsafe_allow_html=True
    )

    # Information Managed

    st.subheader("Information Managed")

    manage_options = [
        "Academic Notes",
        "Exam Timetables",
        "Class Timetables",
        "Notices & Announcements",
        "Events & Activities",
        "Seminars & Workshops",
        "Competitions & Results",
        "Student Achievements"
    ]

    cols = st.columns(2)

    for i, option in enumerate(manage_options):

        with cols[i % 2]:

            st.checkbox(
                option,
                key=f"manage_{option}"
            )

    # Regular Updates

    st.subheader("Regular Updates")

    update_options = [
        "Academic Updates",
        "Exam Updates",
        "Events",
        "Workshops",
        "Seminars",
        "Competitions",
        "Important Notices",
        "All Updates"
    ]

    cols = st.columns(2)

    for i, option in enumerate(update_options):

        with cols[i % 2]:

            st.checkbox(
                option,
                key=f"update_{option}"
            )

    # Payment Information

    st.subheader("Payment Information")

    payment_options = [
        "Department Event Fees",
        "Cultural Event Fees",
        "Competition Fees",
        "Other College Fees"
    ]

    cols = st.columns(2)

    for i, option in enumerate(payment_options):

        with cols[i % 2]:

            st.checkbox(
                option,
                key=f"payment_{option}"
            )

    # Payment Details

    st.subheader("Payment Details")

    payment_details_options = [
        "Student Name / Register Number",
        "Amount Paid",
        "Payment Type",
        "Payment Status",
        "Date of Payment",
        "Person in Charge"
    ]

    cols = st.columns(2)

    for i, option in enumerate(payment_details_options):

        with cols[i % 2]:

            st.checkbox(
                option,
                key=f"payment_details_{option}"
            )

    # Responsibility

    st.subheader("Responsibility")

    responsibility_options = [
        "Staff",
        "Student",
        "Department Coordinator",
        "Other"
    ]

    cols = st.columns(2)

    for i, option in enumerate(responsibility_options):

        with cols[i % 2]:

            st.checkbox(
                option,
                key=f"responsibility_{option}"
            )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("⬅ Back"):

            go_to("staff1")
            st.rerun()

    with col2:

        if st.button(
            "Next ➡",
            type="primary",
            use_container_width=True
        ):

            go_to("staff3")
            st.rerun()


# ============================================================
# STAFF PAGE 3
# ============================================================

elif st.session_state.page == "staff3":

    st.markdown(
        '<div class="section-title">'
        '📝 Additional Staff Information'
        '</div>',
        unsafe_allow_html=True
    )

    st.subheader(
        "Information Added / Updated"
    )

    add_options = [
        "Notes / Study Materials",
        "Timetables",
        "Notices",
        "Events",
        "Workshops / Seminars",
        "Competition Results",
        "Student Achievements",
        "Other Updates"
    ]

    cols = st.columns(2)

    for i, option in enumerate(add_options):

        with cols[i % 2]:

            st.checkbox(
                option,
                key=f"add_{option}"
            )

    st.subheader(
        "Additional Features / Improvements"
    )

    suggestions = st.text_area(
        "Suggestions / additional information",
        key="staff_suggestions",
        height=150
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("⬅ Back"):

            go_to("staff2")
            st.rerun()

    with col2:

        if st.button(
            "✅ Submit Response",
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

                "Name":
                    st.session_state.staff_name,

                "Staff ID":
                    st.session_state.staff_id,

                "Department":
                    st.session_state.staff_department,

                "Designation":
                    st.session_state.staff_designation,

                "Information Managed":
                    get_checked(
                        "manage",
                        manage_options
                    ),

                "Regular Updates":
                    get_checked(
                        "update",
                        update_options
                    ),

                "Payment Information":
                    get_checked(
                        "payment",
                        payment_options
                    ),

                "Payment Details":
                    get_checked(
                        "payment_details",
                        payment_details_options
                    ),

                "Responsibility":
                    get_checked(
                        "responsibility",
                        responsibility_options
                    ),

                "Information Added / Updated":
                    get_checked(
                        "add",
                        add_options
                    ),

                "Suggestions":
                    suggestions
            }

            save_response(response)

            st.success(
                "✅ Your response has been submitted successfully!"
            )


# ============================================================
# ADMIN / PRIVATE RESPONSE VIEWER
# ============================================================

elif st.session_state.page == "admin":

    st.markdown(
        '<div class="section-title">'
        '🔐 Private Response Viewer'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "This section is only for the administrator."
    )

    if not st.session_state.admin_logged_in:

        password = st.text_input(
            "Admin Password",
            type="password"
        )

        if st.button(
            "🔓 Login",
            type="primary"
        ):

            if password == ADMIN_PASSWORD:

                st.session_state.admin_logged_in = True
                st.rerun()

            else:

                st.error(
                    "❌ Incorrect password."
                )

    else:

        st.success(
            "🔓 Admin access granted."
        )

        if DATA_FILE.exists():

            df = pd.read_csv(DATA_FILE)

            st.write(
                f"### Total Responses: {len(df)}"
            )

            st.dataframe(
                df,
                use_container_width=True,
                height=600
            )

        else:

            st.info(
                "No responses have been submitted yet."
            )

        if st.button("🔒 Logout"):

            st.session_state.admin_logged_in = False
            st.rerun()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🎓 Campus Sphere")

    st.divider()

    if st.button(
        "🏠 Home",
        use_container_width=True
    ):

        go_to("home")
        st.rerun()

    if st.button(
        "🔐 Admin / View Responses",
        use_container_width=True
    ):

        go_to("admin")
        st.rerun()
