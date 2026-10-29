import streamlit as st

st.set_page_config(page_title="My Python Calculator", page_icon="🧮")

st.title("🧮 My Python Calculator")
st.caption("Made with Python ❤️")

if "expression" not in st.session_state:
    st.session_state.expression = ""

st.subheader("Display")
st.code(st.session_state.expression or "0", language=None)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", ".", "+"],
]

for row in buttons:
    cols = st.columns(4)
    for col, value in zip(cols, row):
        if col.button(value, use_container_width=True):
            if value == "C":
                st.session_state.expression = ""
            else:
                st.session_state.expression += value
            st.rerun()

if st.button("= Calculate", use_container_width=True):
    try:
        expression = st.session_state.expression
        allowed = "0123456789+-*/.() "

        if not expression or any(c not in allowed for c in expression):
            raise ValueError

        result = eval(expression, {"__builtins__": {}}, {})
        st.session_state.expression = str(result)
        st.rerun()

    except Exception:
        st.error("Invalid calculation!")

