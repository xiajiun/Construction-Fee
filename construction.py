import streamlit as st

# Function to calculate construction fee and breakdown
def calculate_construction_fee_breakdown(square_feet, bedrooms, luxury_features):
    base_price_per_sqft = 100  # Example base price per square foot
    bedroom_price = 5000  # Additional price per bedroom
    luxury_feature_price = 10000  # Additional price per luxury feature
    
    # Calculate total fee
    square_feet_cost = square_feet * base_price_per_sqft
    bedroom_cost = bedrooms * bedroom_price
    luxury_feature_cost = luxury_features * luxury_feature_price
    total_fee = square_feet_cost + bedroom_cost + luxury_feature_cost
    
    # Return the total fee and the breakdown
    return total_fee, square_feet_cost, bedroom_cost, luxury_feature_cost

# Streamlit app
def main():
    st.title("Housing Construction Fee Estimator")

    # User inputs
    square_feet = st.number_input("Size of the house in square feet:", min_value=100.0, value=1000.0, step=100.0)
    bedrooms = st.number_input("Number of bedrooms:", min_value=1, value=3, step=1)
    luxury_features = st.number_input("Number of luxury features (e.g., pool, spa, etc.):", min_value=0, value=0, step=1)
    
    # Button to calculate fee
    if st.button("Calculate Construction Fee"):
        # Calculate fee and breakdown
        total_fee, square_feet_cost, bedroom_cost, luxury_feature_cost = calculate_construction_fee_breakdown(square_feet, bedrooms, luxury_features)
        
        # Display fee and breakdown
        st.success(f"The estimated construction fee is: ${total_fee:,.2f}")
        st.markdown(f"**Breakdown:**")
        st.markdown(f"- Square Feet Cost: ${square_feet_cost:,.2f} (${base_price_per_sqft} per sqft)")
        st.markdown(f"- Bedrooms Cost: ${bedroom_cost:,.2f} (${bedroom_price} per bedroom)")
        st.markdown(f"- Luxury Features Cost: ${luxury_feature_cost:,.2f} (${luxury_feature_price} per feature)")

# Constants for display
base_price_per_sqft = 100  # Example base price per square foot
bedroom_price = 5000  # Additional price per bedroom
luxury_feature_price = 10000  # Additional price per luxury feature

if __name__ == "__main__":
    main()
