import streamlit as st
import math
from datetime import datetime

st.set_page_config(page_title="Our Calculator", page_icon="🧮", layout="centered")

# --- Login simulation (simple) ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "123":
            st.session_state.logged_in = True
            st.success("Welcome Admin!")
        elif username == "user" and password == "123":
            st.session_state.logged_in = True
            st.success("Welcome User!")
        else:
            st.error("Invalid credentials")
    st.stop()

# --- Main Calculator ---
st.title("WELCOME TO OUR CALCULATOR!")
if st.button("LET'S GO!"):
    st.session_state.show_menu = True

if "show_menu" in st.session_state and st.session_state.show_menu:
    choice = st.selectbox("Choose material type:", ["WOOD", "IRON", "CONTAINER", "RAW MATERIALS"])

    if choice == "WOOD":
        tons = st.number_input("Enter weight (tons)", min_value=0.0, step=0.5)
        if st.button("CALCULATE", key="wood"):
            trucks = math.ceil(tons / 40) if tons > 0 else 1
            price = trucks * 200_000
            st.write(f"**{trucks} TRUCKS**")
            st.write(f"Price = {price:,} IQD")

    elif choice == "IRON":
        tons = st.number_input("Enter weight (tons)", min_value=0.0, step=0.5)
        if st.button("CALCULATE", key="iron"):
            trucks = math.ceil(tons / 40) if tons > 0 else 1
            price = trucks * 150_000
            st.write(f"**{trucks} TRUCKS**")
            st.write(f"Price = {price:,} IQD")

    elif choice == "CONTAINER":
        containers = st.number_input("Enter number of containers", min_value=0, step=1)
        if st.button("CALCULATE", key="container"):
            price = containers * 200_000
            st.write(f"**{containers} CONTAINERS**")
            st.write(f"Price = {price:,} IQD")

    elif choice == "RAW MATERIALS":
        models = st.number_input("Enter number of models", min_value=0, step=1)
        if st.button("CALCULATE", key="raw"):
            price = models * 75_000
            st.write(f"**{models} MODELS**")
            st.write(f"Price = {price:,} IQD")

# --- Footer ---
st.caption(f"Calculation system - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
