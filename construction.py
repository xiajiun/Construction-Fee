import streamlit as st

# Constants for the prices
base_price_per_sqft = 100  # Example base price per square foot
bedroom_price = 5000  # Additional price per bedroom
luxury_feature_price = 10000  # Additional price per luxury feature

# Function to calculate construction fee and breakdown
def calculate_construction_fee_breakdown(square_feet, bedrooms, luxury_features):
    # Calculate costs
    square_feet_cost = square_feet * base_price_per_sqft
    bedroom_cost = bedrooms * bedroom_price
    luxury_feature_cost = luxury_features * luxury_feature_price
    total_fee = square_feet_cost + bedroom_cost + luxury_feature_cost
    
    return total_fee, square_feet_cost, bedroom_cost, luxury_feature_cost

# Streamlit app
def main():
    st.title("Housing Construction Fee Estimator")

    # Display the base prices at the top
    st.markdown("""
        ## Base Prices
        - **Base Price per Square Foot:** RM`{}` per sqft
        - **Bedroom Price:** RM`{}` per bedroom
        - **Luxury Feature Price:** RM`{}` per feature
    """.format(base_price_per_sqft, bedroom_price, luxury_feature_price))

    # User inputs
    with st.form("input_form"):
        square_feet = st.number_input("Size of the house in square feet:", min_value=100.0, value=1000.0, step=100.0)
        bedrooms = st.number_input("Number of bedrooms:", min_value=1, value=3, step=1)
        luxury_features = st.number_input("Number of luxury features (e.g., pool, spa, etc.):", min_value=0, value=0, step=1)
        
        submitted = st.form_submit_button("Calculate Construction Fee")
        
    if submitted:
        # Calculate fee and breakdown
        total_fee, square_feet_cost, bedroom_cost, luxury_feature_cost = calculate_construction_fee_breakdown(square_feet, bedrooms, luxury_features)
        
        # Layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Total Cost for Each Item:")
            st.text(f"Square Feet: RM{square_feet_cost:,.2f}")
            st.text(f"Bedrooms: RM{bedroom_cost:,.2f}")
            st.text(f"Luxury Features: RM{luxury_feature_cost:,.2f}")
        
        with col2:
            st.subheader("Breakdown:")
            st.text(f"Square Feet Cost (RM{base_price_per_sqft} per sqft):")
            st.text(f"    RM{square_feet_cost:,.2f} for {square_feet} sqft")
            st.text(f"Bedrooms Cost (RM{bedroom_price} per bedroom):")
            st.text(f"    RM{bedroom_cost:,.2f} for {bedrooms} bedrooms")
            st.text(f"Luxury Features Cost (RM{luxury_feature_price} per feature):")
            st.text(f"    RM{luxury_feature_cost:,.2f} for {luxury_features} features")
        
        # Display the estimated total below everything
        st.subheader("Estimated Total Construction Fee:")
        st.success(f"RM{total_fee:,.2f}")

if __name__ == "__main__":
    main()
