import streamlit as st

# Function to calculate construction fee
def calculate_construction_fee(square_feet, bedrooms, luxury_features):
    base_price_per_sqft = 100  # Example base price per square foot
    bedroom_price = 5000  # Additional price per bedroom
    luxury_feature_price = 10000  # Additional price per luxury feature
    
    # Calculate total fee
    total_fee = (square_feet * base_price_per_sqft) + (bedrooms * bedroom_price) + (luxury_features * luxury_feature_price)
    return total_fee

# Streamlit app
def main():
    st.title("Housing Construction Fee Estimator")

    # User inputs
    square_feet = st.number_input("Size of the house in square feet:", min_value=100.0, value=1000.0, step=100.0)
    bedrooms = st.number_input("Number of bedrooms:", min_value=1, value=3, step=1)
    luxury_features = st.number_input("Number of luxury features (e.g., pool, spa, etc.):", min_value=0, value=0, step=1)
    
    # Button to calculate fee
    if st.button("Calculate Construction Fee"):
        # Calculate fee
        fee = calculate_construction_fee(square_feet, bedrooms, luxury_features)
        
        # Display fee
        st.success(f"The estimated construction fee is: ${fee:,.2f}")

if __name__ == "__main__":
    main()

