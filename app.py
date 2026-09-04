import streamlit as st
import pandas as pd
from pathlib import Path
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
# SETTINGS
# ============================================================

DATA_FILE = Path("Campus_Sphere_Responses.csv")

# CHANGE THIS PASSWORD
ADMIN_PASSWORD = "ChangeThisPassword123"

PURPLE = "#4B248F"

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
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False


def go_to(page):
    st.session_state.page = page


# ============================================================
# SAVE RESPONSE
# ============================================================

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


# ============================================================
# GET CHECKED OPTIONS
# ============================================================

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
# STUDENT / STAFF SELECTION
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

            go_to("student1")
            st.rerun()

    with col2:

        if st.button(
            "👩‍🏫 Staff",
            use_container_width=True
        ):

            go_to("staff1")
            st.rerun()

    st.write("")

    if st.button(
        "💜 Rewind",
        use_container_width=True
    ):

        go_to("welcome")
        st.rerun()


# ============================================================
# STUDENT PAGE 1
# ============================================================

elif st.session_state.page == "student1":

    st.markdown(
        '<div class="section-title">👨‍🎓 Student Information</div>',
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

            if not st.session_state.get("student_name", "").strip():

                st.error("Please enter your name.")

            elif st.session_state.get("student_department") == "Select Department":

                st.error("Please select your department.")

            elif st.session_state.get("student_year") == "Select Year":

                st.error("Please select your year of study.")

            else:

                go_to("student2")
                st.rerun()


# ============================================================
# STUDENT PAGE 2
# ============================================================

elif st.session_state.page == "student2":

    st.markdown(
        '<div class="section-title">📚 Academic Information</div>',
        unsafe_allow_html=True
    )

    # ---------------- ACADEMIC ----------------

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

    # ---------------- EXAMS ----------------

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

    # ---------------- TIMETABLE ----------------

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

        if st.button(
            "💜 Rewind",
            use_container_width=True
        ):

            go_to("student1")
            st.rerun()

    with col2:

        if st.button(
            "💜 Discover",
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
        '<div class="section-title">📢 College Activities & Updates</div>',
        unsafe_allow_html=True
    )

    # ---------------- NOTICES ----------------

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

    # ---------------- EVENTS ----------------

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

    # ---------------- COMPETITIONS ----------------

    st.subheader("Competitions")

    competition
