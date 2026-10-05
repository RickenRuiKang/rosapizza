import streamlit as st
from starter import ZONES, TIME_BLOCKS, COSTS

from rosa_logic import late_order_cost, best_promise

st.title("Rosa's Pizza – Promised Delivery Time")
st.write(
    "Pick a zone and time block, adjust the costs, and find the promised "
    "delivery time that gives the highest net profit."
)

# Zone and time block
zone = st.selectbox("Zone", ZONES)
time_block = st.selectbox("Time block", TIME_BLOCKS)

# Range of promises to try
low, high = st.slider("Promised delivery times to try (minutes)", 5, 120, (5, 100))
step = st.number_input("Step (minutes)", min_value=1, max_value=30, value=5)

# Cost assumptions (defaults come from the starter COSTS)
margin = st.number_input(
    "Profit margin per order ($)", min_value=0.0, value=float(COSTS["margin"]), step=0.5
)
churn_orders = st.number_input(
    "Estimated churn per late order (future orders lost)",
    min_value=0.0, value=float(COSTS["churn_orders"]), step=0.1,
)
refund = st.number_input(
    "Refund cost per late order ($)", min_value=0.0, value=float(COSTS["refund"]), step=0.5
)

costs = {"margin": margin, "churn_orders": churn_orders, "refund": refund}

if st.button("Find recommended promise"):
    promises = list(range(low, high + 1, int(step)))
    best_time, best_profit = best_promise(zone, time_block, promises, costs)

    st.success(f"Recommended promised delivery time: **{best_time} minutes**")
    col1, col2 = st.columns(2)
    col1.metric("Net profit at this promise", f"${best_profit:,.2f}")
    col2.metric("Cost per late order", f"${late_order_cost(costs):,.2f}")
