import streamlit as st

# Question (a)

st.title("Cafe Order Calculator")

# Input Section 

Customer_name=st.text_input("Customer Name", )

Item_Selected=st.write("Food Item:")
option_package = st.selectbox(
    "Select Food Item",
    ["Croissants", "Muffins", "Scones",  "Cookies", "Banana Bread", "Avocado Toast", "Bagel", "Yogurt Bowls"])

quantity_input = st.number_input("Quantity", min_value=0, value=1)
price_input = st.number_input("Price per item", min_value=0.0, value=0.0, step=0.20)

#User Defined Function 

def subtotal(quantity, price):
    return quantity * price

def discount(Sub_total):
    discount_amount = 0.0
    if Sub_total >= 50.0:
        discount_amount = Sub_total * 0.10
    return discount_amount

def cost(SUB_total, Discount):
    return SUB_total - Discount


if st.button("Calculate Total"):
    try:
        if not Customer_name:
            st.error("Please enter a customer name.")
        elif quantity_input <= 0:
            st.error("Please enter a quantity greater than 0.")
        elif price_input <= 0:
            st.error("Please enter a price greater than 0.")
        else:
            calculate_subtotal = subtotal (quantity_input,price_input)
            calculate_discount = discount (calculate_subtotal)
            calculate_total_cost = cost (calculate_subtotal,calculate_discount)

            # Question (b) 
            st.subheader(f"Order Summary for {Customer_name}") 
            st.write(f"Items ordered: {option_package}") 
            st.write(f"Quantity: {quantity_input}") 
            st.write(f"Price per item: RM {price_input:.2f}") 
            st.write(f"Subtotal: RM {calculate_subtotal:.2f}") 
            st.write(f"Discount: RM {calculate_discount:.2f}")             
            st.success(f"Total Cost:RM {calculate_total_cost:.2f}")

    except ValueError as e:
        st.error(f"Please enter valid values. Error: {e}")