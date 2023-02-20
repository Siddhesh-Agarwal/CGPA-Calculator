import streamlit as st
import numpy as np

st.set_page_config(
    page_title="CGPA Calculator",
    page_icon="📊",
)


grade_to_point = {
    "O": 10,
    "A+": 9,
    "A": 8,
    "B+": 7,
    "B": 6,
    "C": 5,
}
grades = list(grade_to_point.keys())


def calculate_cgpa(
    grade: np.array,
    credit: np.array,
    previous_cgpa: float = 0,
    previous_credit: float = 0,
):
    # grade = np.array([grade_to_point[g] for g in grade])
    total_credit = credit.sum() + previous_credit
    total_grade = (grade * credit).sum() + previous_cgpa * previous_credit
    return total_grade / total_credit


st.title("CGPA Calculator")

st.markdown(
    "This is a simple CGPA calculator that calculates your CGPA based on your grades and credits"
)

st.latex(r"CGPA = \frac{\sum_{i=1}^{n} (grade_i * credit_i)}{\sum_{i=1}^{n} credit_i}")

cols = st.columns(2)
previous_cgpa = cols[0].number_input(
    label="Previous CGPA",
    min_value=0.0,
    value=0.0,
    step=0.01,
)
previous_credit = cols[1].number_input(
    label="Previous Credit",
    min_value=0.0,
    value=0.0,
    step=0.5,
)
number_of_subjects = st.number_input(
    label="Number of Subjects",
    min_value=1,
    max_value=10,
    value=5,
)


grade = np.array([0] * number_of_subjects)
credit = np.array([0] * number_of_subjects)
for i in range(number_of_subjects):
    st.subheader(f"Subject #{i+1}")
    cols = st.columns(2)
    grade[i] = grade_to_point[
        cols[0].selectbox(
            label=f"Grade",
            options=grades,
            key=f"selectbox_{i}",
        )
    ]

    credit[i] = cols[1].number_input(
        label=f"Credit",
        min_value=1.0,
        max_value=10.0,
        value=4.0,
        step=0.5,
        key=f"number_input_{i}",
    )

if st.button("Calculate"):
    st.info(f"Your semester GPA is {calculate_cgpa(grade, credit):.2f}")
    st.success(
        f"Your Cumulative GPA is {calculate_cgpa(grade, credit, previous_cgpa, previous_credit):.2f}"
    )


st.markdown("Made with ❤️ by [Siddhesh Agarwal](https://github.com/Siddhesh-Agarwal)")
st.write(
    """
    <style>
        footer {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
