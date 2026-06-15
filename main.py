import streamlit as st
from utils.converter import convert_currency

st.set_page_config(
    page_title="Currency Converter",
    page_icon="💱",
    layout="centered"
)

st.title("💱 Currency Converter")
st.write("Convert currencies in real-time using the latest exchange rates.")

currencies = [
    "USD",
    "INR",
    "EUR",
    "GBP",
    "JPY",
    "AUD",
    "CAD",
    "CHF",
    "CNY",
    "SGD"
]

amount = st.number_input(
    "Enter Amount",
    min_value=0.0,
    value=1.0
)

col1, col2 = st.columns(2)

with col1:
    from_currency = st.selectbox(
        "From Currency",
        currencies,
        index=0
    )

with col2:
    to_currency = st.selectbox(
        "To Currency",
        currencies,
        index=1
    )

if st.button("Convert Currency"):
    
    if from_currency == to_currency:
        st.warning("Please select different currencies.")
    
    else:
        result = convert_currency(
            amount,
            from_currency,
            to_currency
        )

        if isinstance(result, str):
            st.error(result)

        else:
            st.success(
                f"{amount:,.2f} {from_currency} = "
                f"{result:,.2f} {to_currency}"
            )

            st.metric(
                label="Converted Amount",
                value=f"{result:,.2f} {to_currency}"
            )