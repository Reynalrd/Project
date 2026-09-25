
import streamlit as st

st.set_page_config(
    page_title="My Student App",
    page_icon="🎓",
    layout="centered"
)


# ============================================================
# BACKGROUND
# ============================================================
# The background image is embedded in this file.
background_image = "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IUks5FNZdlv5+GOUaekosw26+CFJLORTWXZb+fhjlGnpKLMNuvghSSzkU1l2W/n4Y5Rp6SizDbr4IUks5FNZdlv5+GOUaekosw26+BQbueLk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ycKiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIoJez1CSr2eoSVez1CSr2eoSVez1CSr2eoSVez1CSr2eoSVez1CSr2eoSVez1CSr2eoSVez1CSr2eoSVez1CSr2eoSVez1CSr2eoSVez1CSr2eoSVez1CSwMiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERMP3mZ/t77zR5L7/7e+80eS+/+3vvNHkvv/t77zR5L7/7e+80eS+/+3vvNHkvv/t77zR5L7/7e+80eS+/+3vvNHkvv/t77zR5L7/7e+80eS+/9JD+xR0VBFVxW0WNFthd4oGKZioIquK2ixotsLvFAxTMVBFVxW0WNFthd4oGKZioIquK2ixotsLvFAxTMVBFVxW0WNFthd4oGKa6IiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERETjB/PvnVXZb72ekosq0k09JD4QpJZTuvghROYbde+oosw21k9JRZVpJp6SHwhSSyndfBCicw2699RRZhtrJ6SiyrSTT0kPhCkllO6+CFE5ht176iizDbWT0lFlWkMYai8XRHXTWn6KUIdZZofocX51k5DehvEfe0gCyG71OLR+nCfvPktY8R0e89UZDxD13z1F4uiOumtP0UoQ6yzQ/Q4vzrJyG9DeI+mm+rHiHWTbYCrJtsBVk22AqybbAVZNtgKsm2wFWTbYCrJtsBVk22AqybbAVZNtgKsm2wFWTbYCrJtsBVk22AqybbAVZNtgC33Yr1lNbxfkFhmUzmk1y24PMa3i/ILDMpnNJrltweY1vF+QWGZTOaTXLbg8xreL8gsMymc0muW3B5jW8X5BYZlM5pNctuDzGt4vyCwzKZzSa5bcHmNbxfkF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L8e41FQvlMZHAOl+PcaioXymMjgHS/HuNRUL5TGRwDpfj3GoqF8pjI4B0vx7jUVC+UxkcA6X49xqKhfKYyOAdL8e40SEIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERE4kYFGBRgUYFGBRgUYFGBRgUYFGBRgUYFGBRgUYFGBRgUYFGBRgUYFGBRgUYFGBRgUYFGBRgUYFGBRgUYFGBRgUYFGBRgUYFGBRgkKW9o/RHWTbYCrJtsBVk22AqybbAVZNtgKsm2wFWTbYCrJtsBVk22AqybbAVZNtgKsm2wFWTbYCrJtsBVk22AqybbAVZNtd4LXpC7vojaVKN32YeJNjoQaC1fglCpRu+zDxJsdCDQWr8EoVKN32YeJNjoQaC1fglCpRu+zDxJsdCDQWr8EoVKN32Yb5ERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZSapBqr0ztZ71qyhJQ191wHhrq9dOdOXhnaz3rVlCShr7rgPDXV66c6cvDO1nvWrKElDX3XAeGur10505eGdrPetWUJKGvuuA8NdXrpzpy8M7We9asvVEQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGRRSEREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIihIvEffeaPJff/b33mjyX3/2995o8l9/9vfeaPJff/b33mjyX3/2995o8l9/9vfeaPJff/b33mjyX3/2995o8l9/9vfeaPJff/b33mjyX3/298giIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERDIiIiIZERERLZEQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGREREQyIiIiGRUJizgsSK5CuQrkK5CuQrkK5CuQrkK5CuQrkK5CuQrkK5CuQrkK5CuQrkK5CuQrkK5CuQrkK5CuQrkK5CuQrkK5CuQrkK5CuQrkK6QIiIhkREREMiIiIhkREREMiIiIhkREREMiIiIhkREREMiIiIhkREREMiIiIhkREREMiIiIhkREREMiIiIhkREREO30JKvZ6hOdZZe5nqE51ll7meoTnWWXuZ6hOdZZe5nqE51ll7meoTnWWXuZ6hOdZZe5nqE51ll7meoTnWWXuZ6hOdZZe5nqE51ll7meoTnWWXuZ6hOdZZe5nqE54YhEREREMiIiIhkREREMiIiIhkREREMiIiIhkREREMiIiIhkREREMiIiIhkREREMiIiIhkREREMiIiIhkREREMiIoNbHPnWxE2OhBoLV+CUKlG77MPEmx0INBavwShUo3fZh4k2OhBoLV+CUKlG77MPEmx0INBavwShUo3fZh4k2OhBoLV93mOZoEY5mikqyxLONa4bsPbCMYzRSVZYlnGtcN2HthGMZopKssSzjWuG7D2wjGM0UlWWJZxrXDdh7YRjGaKSrLEs41rhuw9sIxjNFJVli8ogWS7Xi5OQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D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"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/webp;base64,{background_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* Make page text white */
    .stApp, .stApp p, .stApp span, .stApp label,
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
    .stApp div, .stApp li, .stApp .stMarkdown,
    .stApp [data-testid="stHeader"] {{
        color: black !important;
    }}

    /* Calculator numbers and numeric input values */
    .stApp input[type="number"],
    .stApp input[type="number"] + div,
    .stApp [data-testid="stNumberInput"] input {{
        color: black !important;
        -webkit-text-fill-color: black !important;
    }}

    /* Calculator result/output numbers */
    .stApp [data-testid="stMetricValue"],
    .stApp [data-testid="stMetricValue"] *,
    .stApp [data-testid="stMetricLabel"] {{
        color: black !important;
        -webkit-text-fill-color: black !important;
    }}



    /* Remove the white Streamlit bar above the app background */
    header[data-testid="stHeader"] {{
        display: none !important;
    }}

    [data-testid="stToolbar"] {{
        display: none !important;
    }}

    .stAppViewContainer {{
        padding-top: 0 !important;
    }}

    /* Floating back-to-menu button */
    html {{
        scroll-behavior: smooth;
    }}

    .back-menu-btn {{
        position: fixed;
        right: 24px;
        bottom: 24px;
        z-index: 9999;
        display: inline-block;
        padding: 10px 16px;
        border: 2px solid #000;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.94);
        color: #000 !important;
        text-decoration: none !important;
        font-weight: 700;
        box-shadow: 0 4px 12px rgba(0,0,0,0.18);
        transition: transform 0.2s ease, background 0.2s ease, box-shadow 0.2s ease;
    }}

    .back-menu-btn:hover {{
        background: #fff;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.22);
    }}

    /* Smooth section navigation */
    html {{
        scroll-behavior: smooth;
    }}

    .back-to-menu {{
        display: inline-block;
        margin: 8px 0 18px 0;
        padding: 8px 14px;
        border: 2px solid rgba(0, 0, 0, 0.8);
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.85);
        color: black !important;
        text-decoration: none !important;
        font-weight: 700;
        transition: all 0.2s ease;
    }}

    .back-to-menu:hover {{
        background: white;
        transform: translateY(-1px);
    }}

    /* Give anchor targets a little breathing room when scrolled to */
    [id="profile"], [id="calculator"], [id="grades"],
    [id="quiz-maker"] {{
        scroll-margin-top: 90px;
    }}

    /* Easy section navigation menu */
    .student-menu {{
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        padding: 12px;
        margin: 12px 0 20px 0;
        border: 3px solid rgba(0, 0, 0, 0.85);
        border-radius: 16px;
        background: rgba(255, 255, 255, 0.72);
        position: sticky;
        top: 8px;
        z-index: 999;
        backdrop-filter: blur(8px);
    }}

    .student-menu a {{
        color: black !important;
        text-decoration: none !important;
        font-weight: 700;
        padding: 9px 14px;
        border: 2px solid rgba(0, 0, 0, 0.7);
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.9);
        transition: transform 0.15s ease, background 0.15s ease;
    }}

    .student-menu a:hover {{
        background: white;
        transform: translateY(-1px);
    }}

    .calculator-display {{
        color: white !important;
        -webkit-text-fill-color: white !important;
    }}

    /* Main sections: calculator, grades, quiz, profile, etc. */
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        border: 4px solid rgba(0, 0, 0, 0.9) !important;
        border-radius: 20px !important;
        background: rgba(0, 0, 0, 0.28) !important;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35) !important;
    }}

    /* Give section headings a clear framed appearance */
    .stApp h2, .stApp h3 {{
        text-shadow: 0 2px 5px rgba(0, 0, 0, 0.65);
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background: rgba(255, 255, 255, 0.25);
        z-index: -1;
        pointer-events: none;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎓 My Student App")
st.write("Profile, calculator, grades, and quiz maker")


st.markdown(
    """
    <nav id="student-menu" class="student-menu" aria-label="Student app sections">
        <a href="#profile">👤 Profile</a>
        <a href="#calculator">🧮 Calculator</a>
        <a href="#grades">📚 Grades</a>
        <a href="#quiz-maker">📝 Quiz Maker</a>
    </nav>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<a class="back-menu-btn" href="#student-menu" aria-label="Back to menu">↑ Back to Menu</a>',
    unsafe_allow_html=True
)
# ============================================================
# PROFILE
# ============================================================

st.markdown('<div id="profile"></div>', unsafe_allow_html=True)

with st.expander("👤 My Profile"):

    name = st.text_input("What is your name?")

    age = st.number_input(
        "How old are you?",
        min_value=1,
        max_value=100,
        value=13,
        step=1
    )

    school = st.text_input("What school do you go to?")

    favorite_subject = st.text_input(
        "What is your favorite subject?"
    )

    hobby = st.text_input("What is your favorite hobby?")

    if st.button("✨ Create My Profile"):

        if name and school and favorite_subject and hobby:

            st.success("Profile created successfully! 🎉")

            st.write(f"### Hello, {name}!")
            st.write(f"**Age:** {age}")
            st.write(f"**School:** {school}")
            st.write(f"**Favorite subject:** {favorite_subject}")
            st.write(f"**Favorite hobby:** {hobby}")

        else:

            st.warning("Please fill in all the profile fields.")


# ============================================================
# CALCULATOR
# ============================================================

st.markdown('<div id="calculator"></div>', unsafe_allow_html=True)
st.divider()
with st.container(border=True):
    st.header("🧮 Calculator")

# Calculator state
if "calc_display" not in st.session_state:
    st.session_state.calc_display = "0"

if "calc_first" not in st.session_state:
    st.session_state.calc_first = None

if "calc_operator" not in st.session_state:
    st.session_state.calc_operator = None

if "calc_new_number" not in st.session_state:
    st.session_state.calc_new_number = True


def format_calc_result(result):
    """Format calculator results without unnecessary .0."""
    if result == int(result):
        return str(int(result))
    return str(round(result, 10))


def calculator_press(value):
    """Handle every calculator button press."""
    display = st.session_state.calc_display

    # Numbers
    if value.isdigit():
        if (
            st.session_state.calc_new_number
            or display == "0"
            or display == "Error"
        ):
            st.session_state.calc_display = value
        else:
            st.session_state.calc_display += value

        st.session_state.calc_new_number = False
        return

    # Decimal point
    if value == ".":
        if display == "Error" or st.session_state.calc_new_number:
            st.session_state.calc_display = "0."
            st.session_state.calc_new_number = False
        elif "." not in display:
            st.session_state.calc_display += "."
        return

    # Clear
    if value == "C":
        st.session_state.calc_display = "0"
        st.session_state.calc_first = None
        st.session_state.calc_operator = None
        st.session_state.calc_new_number = True
        return

    # Operators
    if value in ["+", "-", "×", "÷"]:
        try:
            current = float(st.session_state.calc_display)

            # If there is already an operation waiting, calculate it first.
            if (
                st.session_state.calc_first is not None
                and st.session_state.calc_operator is not None
                and not st.session_state.calc_new_number
            ):
                first = st.session_state.calc_first
                operator = st.session_state.calc_operator

                if operator == "+":
                    current = first + current
                elif operator == "-":
                    current = first - current
                elif operator == "×":
                    current = first * current
                elif operator == "÷":
                    if current == 0:
                        st.session_state.calc_display = "Error"
                        st.session_state.calc_first = None
                        st.session_state.calc_operator = None
                        st.session_state.calc_new_number = True
                        return
                    current = first / current

                st.session_state.calc_display = format_calc_result(current)

            st.session_state.calc_first = float(st.session_state.calc_display)
            st.session_state.calc_operator = value
            st.session_state.calc_new_number = True

        except (ValueError, TypeError):
            st.session_state.calc_display = "Error"
            st.session_state.calc_first = None
            st.session_state.calc_operator = None
            st.session_state.calc_new_number = True

        return

    # Equals
    if value == "=":
        if (
            st.session_state.calc_first is None
            or st.session_state.calc_operator is None
        ):
            return

        try:
            first = st.session_state.calc_first
            second = float(st.session_state.calc_display)
            operator = st.session_state.calc_operator

            if operator == "+":
                result = first + second
            elif operator == "-":
                result = first - second
            elif operator == "×":
                result = first * second
            elif operator == "÷":
                if second == 0:
                    st.session_state.calc_display = "Error"
                    st.session_state.calc_first = None
                    st.session_state.calc_operator = None
                    st.session_state.calc_new_number = True
                    return
                result = first / second
            else:
                return

            st.session_state.calc_display = format_calc_result(result)
            st.session_state.calc_first = None
            st.session_state.calc_operator = None
            st.session_state.calc_new_number = True

        except (ValueError, TypeError):
            st.session_state.calc_display = "Error"
            st.session_state.calc_first = None
            st.session_state.calc_operator = None
            st.session_state.calc_new_number = True


# IMPORTANT:
# Use markdown for the display instead of a disabled text_input.
# This prevents Streamlit's widget state from overriding the calculator state.
st.markdown(
    f"""
    <div class="calculator-display" style="
        background:#1f2937;
        color:white !important;
        padding:16px;
        border-radius:10px;
        text-align:right;
        font-size:34px;
        font-weight:600;
        margin-bottom:12px;
        min-height:48px;
        white-space:nowrap;
    ">{st.session_state.calc_display}</div>
    """,
    unsafe_allow_html=True
)

calculator_rows = [
    ["C", "÷", "×", "-"],
    ["7", "8", "9", "+"],
    ["4", "5", "6", "="],
    ["1", "2", "3", "."],
    ["0"]
]

for row_number, row in enumerate(calculator_rows):
    columns = st.columns(len(row))

    for column, button_value in zip(columns, row):
        with column:
            st.button(
                button_value,
                key=f"calculator_{row_number}_{button_value}",
                use_container_width=True,
                on_click=calculator_press,
                args=(button_value,)
            )


# ============================================================
# GRADE CALCULATOR
# ============================================================

st.markdown('<div id="grades"></div>', unsafe_allow_html=True)
st.divider()
with st.container(border=True):
    st.header("📚 Grade Calculator")

st.write("Add as many subjects as you want.")

if "subjects" not in st.session_state:

    st.session_state.subjects = [
        {"name": "Mathematics", "grade": 0.0},
        {"name": "Science", "grade": 0.0},
        {"name": "English", "grade": 0.0}
    ]


def add_subject():

    number = len(st.session_state.subjects) + 1

    st.session_state.subjects.append(
        {
            "name": f"Subject {number}",
            "grade": 0.0
        }
    )


def remove_subject():

    if len(st.session_state.subjects) > 1:

        st.session_state.subjects.pop()


def get_grade(score):

    if score >= 90:
        return "A", 4.0

    elif score >= 80:
        return "B", 3.0

    elif score >= 70:
        return "C", 2.0

    elif score >= 60:
        return "D", 1.0

    else:
        return "F", 0.0


for index, subject in enumerate(st.session_state.subjects):

    with st.container(border=True):

        col1, col2 = st.columns([2.5, 1])

        with col1:

            st.session_state.subjects[index]["name"] = st.text_input(
                "Subject",
                value=subject["name"],
                key=f"grade_subject_{index}"
            )

        with col2:

            st.session_state.subjects[index]["grade"] = st.number_input(
                "Grade %",
                min_value=0.0,
                max_value=100.0,
                value=float(subject["grade"]),
                step=0.5,
                key=f"grade_value_{index}"
            )


col1, col2 = st.columns(2)

with col1:

    st.button(
        "➕ Add Subject",
        use_container_width=True,
        on_click=add_subject,
        key="add_subject"
    )

with col2:

    st.button(
        "➖ Remove Subject",
        use_container_width=True,
        on_click=remove_subject,
        disabled=len(st.session_state.subjects) <= 1,
        key="remove_subject"
    )


if st.button(
    "📊 Calculate Results",
    type="primary",
    use_container_width=True,
    key="calculate_grades"
):

    grades = [
        float(subject["grade"])
        for subject in st.session_state.subjects
    ]

    average = sum(grades) / len(grades)

    overall_letter, _ = get_grade(average)

    gpas = [
        get_grade(grade)[1]
        for grade in grades
    ]

    gpa = sum(gpas) / len(gpas)

    st.subheader("📈 Your Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Percentage", f"{average:.1f}%")

    with col2:
        st.metric("GPA", f"{gpa:.2f}")

    with col3:
        st.metric("Overall Grade", overall_letter)

    st.write("### 📋 Subject Breakdown")

    for subject in st.session_state.subjects:

        subject_name = (
            subject["name"].strip()
            or "Unnamed Subject"
        )

        grade = float(subject["grade"])

        letter, points = get_grade(grade)

        st.write(
            f"**{subject_name}** — "
            f"{grade:.1f}% — "
            f"**{letter}** · {points:.1f}"
        )


# ============================================================
# QUIZ MAKER
# ============================================================

st.markdown('<div id="quiz-maker"></div>', unsafe_allow_html=True)
st.divider()
with st.container(border=True):
    st.header("📝 Quiz Maker")

st.write(
    "Create a multiple-choice quiz with "
    "between 1 and 20 questions."
)

if "quiz_questions" not in st.session_state:

    st.session_state.quiz_questions = [
        {
            "question": "",
            "a": "",
            "b": "",
            "c": "",
            "d": "",
            "correct": "A"
        }
    ]


def add_question():

    if len(st.session_state.quiz_questions) < 20:

        st.session_state.quiz_questions.append(
            {
                "question": "",
                "a": "",
                "b": "",
                "c": "",
                "d": "",
                "correct": "A"
            }
        )


def remove_question():

    if len(st.session_state.quiz_questions) > 1:

        st.session_state.quiz_questions.pop()


def reset_quiz():

    st.session_state.quiz_questions = [
        {
            "question": "",
            "a": "",
            "b": "",
            "c": "",
            "d": "",
            "correct": "A"
        }
    ]



with st.expander("🛠️ Create Your Quiz", expanded=True):

    st.write(
        f"### {len(st.session_state.quiz_questions)} / 20 Questions"
    )

    for index, question in enumerate(
        st.session_state.quiz_questions
    ):

        with st.container(border=True):

            st.markdown(
                f"### ❓ Question {index + 1}"
            )

            question["question"] = st.text_area(
                "Question",
                value=question["question"],
                placeholder="Example: What is 2 + 2?",
                key=f"question_text_{index}"
            )

            st.write("**Answer Choices**")

            question["a"] = st.text_input(
                "A",
                value=question["a"],
                key=f"answer_a_{index}"
            )

            question["b"] = st.text_input(
                "B",
                value=question["b"],
                key=f"answer_b_{index}"
            )

            question["c"] = st.text_input(
                "C",
                value=question["c"],
                key=f"answer_c_{index}"
            )

            question["d"] = st.text_input(
                "D",
                value=question["d"],
                key=f"answer_d_{index}"
            )

            question["correct"] = st.selectbox(
                "Correct Answer",
                ["A", "B", "C", "D"],
                index=["A", "B", "C", "D"].index(
                    question["correct"]
                ),
                key=f"correct_answer_{index}"
            )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.button(
            "➕ Add Question",
            use_container_width=True,
            on_click=add_question,
            disabled=len(st.session_state.quiz_questions) >= 20,
            key="add_question_button"
        )

    with col2:

        st.button(
            "➖ Remove Question",
            use_container_width=True,
            on_click=remove_question,
            disabled=len(st.session_state.quiz_questions) <= 1,
            key="remove_question_button"
        )

    with col3:

        st.button(
            "🔄 Reset Quiz",
            use_container_width=True,
            on_click=reset_quiz,
            key="reset_quiz_button"
        )



# ============================================================
# QUIZ TAKING + RESULTS
# ============================================================

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}

if "show_quiz_result" not in st.session_state:
    st.session_state.show_quiz_result = False


def start_quiz():
    questions = st.session_state.quiz_questions
    incomplete = []

    for index, question in enumerate(questions):
        if not question["question"].strip():
            incomplete.append(index + 1)
        elif not all(question[key].strip() for key in ["a", "b", "c", "d"]):
            incomplete.append(index + 1)

    if incomplete:
        st.session_state.quiz_error = (
            "Please complete Question(s) "
            + ", ".join(map(str, incomplete))
            + " before starting the quiz."
        )
        return

    st.session_state.quiz_started = True
    st.session_state.quiz_finished = False
    st.session_state.quiz_score = 0
    st.session_state.quiz_answers = {}
    st.session_state.show_quiz_result = False
    st.session_state.quiz_error = ""


def submit_quiz():
    score = 0

    for index, question in enumerate(st.session_state.quiz_questions):
        answer = st.session_state.get(f"quiz_answer_{index}")
        st.session_state.quiz_answers[index] = answer

        if answer == question["correct"]:
            score += 1

    st.session_state.quiz_score = score
    st.session_state.quiz_finished = True
    st.session_state.show_quiz_result = True


def show_result():
    if st.session_state.quiz_finished:
        st.session_state.show_quiz_result = True
    else:
        st.session_state.quiz_error = "Complete the quiz first to see your result."


st.divider()
with st.container(border=True):
    st.subheader("🎯 Take Quiz")
    st.write("Start the quiz you created and check your score when you finish.")

    action_col1, action_col2 = st.columns(2)

    with action_col1:
        st.button(
            "▶️ Start Quiz",
            use_container_width=True,
            on_click=start_quiz,
            key="start_quiz_button"
        )

    with action_col2:
        st.button(
            "🏆 Show Result",
            use_container_width=True,
            on_click=show_result,
            key="show_result_button"
        )

    if st.session_state.get("quiz_error"):
        st.warning(st.session_state.quiz_error)


if st.session_state.quiz_started:

    st.markdown("### 📝 Quiz")
    st.write("Choose one answer for each question, then submit your quiz.")

    for index, question in enumerate(st.session_state.quiz_questions):
        st.markdown(f"**Question {index + 1}. {question['question']}**")

        options = {
            "A": question["a"],
            "B": question["b"],
            "C": question["c"],
            "D": question["d"]
        }

        previous_answer = st.session_state.quiz_answers.get(index, "A")
        previous_index = ["A", "B", "C", "D"].index(previous_answer) if previous_answer in ["A", "B", "C", "D"] else 0

        st.radio(
            "Answer",
            list(options.keys()),
            index=previous_index,
            format_func=lambda letter: f"{letter}. {options[letter]}",
            key=f"quiz_answer_{index}",
            label_visibility="collapsed"
        )

    st.button(
        "✅ Submit Quiz",
        use_container_width=True,
        on_click=submit_quiz,
        key="submit_quiz_button"
    )


if st.session_state.quiz_finished and st.session_state.show_quiz_result:

    total = len(st.session_state.quiz_questions)
    score = st.session_state.quiz_score
    percentage = (score / total * 100) if total else 0

    st.divider()
    with st.container(border=True):
        st.subheader("🏆 Quiz Result")
        st.metric("Score", f"{score} / {total}")
        st.progress(percentage / 100)
        st.write(f"**Percentage: {percentage:.1f}%**")

        if percentage >= 80:
            st.success("Great job! 🎉")
        elif percentage >= 60:
            st.info("Good effort! Keep practicing. 📚")
        else:
            st.warning("Keep practicing and try again! 💪")

        st.write("### Answer Review")
        for index, question in enumerate(st.session_state.quiz_questions):
            user_answer = st.session_state.quiz_answers.get(index)
            correct_answer = question["correct"]

            if user_answer == correct_answer:
                st.success(
                    f"Question {index + 1}: Correct — {correct_answer}. "
                    f"{question[correct_answer.lower()]}"
                )
            else:
                st.error(
                    f"Question {index + 1}: Your answer: {user_answer}. "
                    f"Correct answer: {correct_answer}. "
                    f"{question[correct_answer.lower()]}"
                )
