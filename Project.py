
import streamlit as st

st.set_page_config(
    page_title="My Student App",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 My Student App")
st.write("Profile, calculator, grades, and quiz maker")

# ============================================================
# PROFILE
# ============================================================

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

st.divider()
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
    <div style="
        background: #1f2937;
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: right;
        font-size: 36px;
        font-weight: 600;
        margin-bottom: 16px;
        min-height: 52px;
        overflow-x: auto;
        white-space: nowrap;
    ">
        {st.session_state.calc_display}
    </div>
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

st.divider()
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

st.divider()
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

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0


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

    st.session_state.quiz_started = False
    st.session_state.quiz_finished = False
    st.session_state.quiz_score = 0


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


if not st.session_state.quiz_started:

    if st.button(
        "🚀 Start Quiz",
        type="primary",
        use_container_width=True,
        key="start_quiz_button"
    ):

        quiz_is_valid = True

        for question in st.session_state.quiz_questions:

            if not question["question"].strip():
                quiz_is_valid = False
                break

            if not question["a"].strip():
                quiz_is_valid = False
                break

            if not question["b"].strip():
                quiz_is_valid = False
                break

            if not question["c"].strip():
                quiz_is_valid = False
                break

            if not question["d"].strip():
                quiz_is_valid = False
                break

        if quiz_is_valid:

            st.session_state.quiz_started = True
            st.session_state.quiz_finished = False
            st.session_state.quiz_score = 0

            st.rerun()

        else:

            st.error(
                "Please fill in every question and "
                "all four answers."
            )


if st.session_state.quiz_started:

    st.divider()

    st.header("🎯 Take Your Quiz")

    st.write(
        f"Total Questions: "
        f"**{len(st.session_state.quiz_questions)}**"
    )

    for index, question in enumerate(
        st.session_state.quiz_questions
    ):

        st.markdown(
            f"### Question {index + 1}"
        )

        st.write(
            f"**{question['question']}**"
        )

        st.radio(
            "Choose your answer:",
            ["A", "B", "C", "D"],
            format_func=lambda letter, q=question: (
                f"{letter}. {q[letter.lower()]}"
            ),
            key=f"user_answer_{index}"
        )

        if index < len(
            st.session_state.quiz_questions
        ) - 1:

            st.divider()

    if st.button(
        "✅ Submit Quiz",
        type="primary",
        use_container_width=True,
        key="submit_quiz_button"
    ):

        score = 0

        for index, question in enumerate(
            st.session_state.quiz_questions
        ):

            selected = st.session_state.get(
                f"user_answer_{index}"
            )

            if selected == question["correct"]:
                score += 1

        st.session_state.quiz_score = score
        st.session_state.quiz_finished = True

        st.rerun()


if (
    st.session_state.quiz_started
    and st.session_state.quiz_finished
):

    st.divider()

    st.header("🏆 Quiz Results")

    total = len(st.session_state.quiz_questions)

    score = st.session_state.quiz_score

    percentage = (score / total) * 100

    if percentage >= 90:

        grade = "A"
        message = "Excellent work! 🌟"

    elif percentage >= 80:

        grade = "B"
        message = "Great job! 🎉"

    elif percentage >= 70:

        grade = "C"
        message = "Good job! 👍"

    elif percentage >= 60:

        grade = "D"
        message = "Keep practicing! 📚"

    else:

        grade = "F"
        message = "Keep trying! You can improve! 💪"

    st.metric(
        "Score",
        f"{score} / {total}"
    )

    st.metric(
        "Percentage",
        f"{percentage:.1f}%"
    )

    st.metric(
        "Grade",
        grade
    )

    st.success(message)

    st.subheader("📋 Answer Review")

    for index, question in enumerate(
        st.session_state.quiz_questions
    ):

        selected = st.session_state.get(
            f"user_answer_{index}"
        )

        correct = question["correct"]

        st.write(
            f"**Question {index + 1}: "
            f"{question['question']}**"
        )

        if selected == correct:

            st.success(
                f"✅ Correct! "
                f"{correct}. "
                f"{question[correct.lower()]}"
            )

        else:

            st.error(
                f"❌ Your answer: "
                f"{selected}"
            )

            st.info(
                f"Correct answer: "
                f"{correct}. "
                f"{question[correct.lower()]}"
            )

    if st.button(
        "🔄 Take Quiz Again",
        use_container_width=True,
        key="again_button"
    ):

        st.session_state.quiz_started = False
        st.session_state.quiz_finished = False
        st.session_state.quiz_score = 0

        st.rerun()


st.divider()
st.caption("Made with Python + Streamlit 🐍")
