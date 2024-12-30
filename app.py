import streamlit as st

# Function to calculate the total cost
def calculate_cost(filling_cost, crown_cost, control_cost, cover_control, reimbursement_rate, max_reimbursement, monthly_premium, num_fillings, num_crowns, num_controls):
    # Total procedure costs (in euros)
    total_fill_cost = filling_cost * num_fillings
    total_crown_cost = crown_cost * num_crowns
    total_control_cost = control_cost * num_controls if cover_control else 0  # Only add control costs if covered
    total_procedure_cost = total_fill_cost + total_crown_cost + total_control_cost
    
    # Reimbursement calculations
    reimbursement_for_fillings = total_fill_cost * reimbursement_rate
    reimbursement_for_crowns = total_crown_cost * reimbursement_rate
    reimbursement_for_controls = total_control_cost * reimbursement_rate if cover_control else 0
    total_reimbursement = reimbursement_for_fillings + reimbursement_for_crowns + reimbursement_for_controls
    
    # Subtract max reimbursement
    max_reimbursement_left = max_reimbursement - total_reimbursement
    if max_reimbursement_left < 0:
        total_reimbursement = max_reimbursement
    
    # Out of pocket cost (in euros)
    out_of_pocket = max(0, total_procedure_cost - total_reimbursement)
    
    # Annual premium cost (in euros)
    annual_premium = monthly_premium * 12
    
    # Total cost including out-of-pocket (in euros)
    total_cost_with_insurance = annual_premium + out_of_pocket
    
    # Total cost without insurance (paying full out-of-pocket, in euros)
    total_without_insurance = total_procedure_cost
    
    # Difference (insurance cost vs no insurance cost, in euros)
    difference = total_cost_with_insurance - total_without_insurance
    
    return total_cost_with_insurance, annual_premium, out_of_pocket, total_without_insurance, difference

# Streamlit user interface
st.title("Dental Insurance Cost Calculator (in Euros)")

# Explanation of adjustable costs
st.write("**Note:** You can adjust the average cost of fillings, crowns, and control procedures for this calculation.")

# Input fields for customizable costs
filling_cost = st.number_input("Enter the cost of a filling (€):", value=80.00, step=0.01)
crown_cost = st.number_input("Enter the cost of a crown (€):", value=900.00, step=0.01)
control_cost = st.number_input("Enter the cost of a control procedure (€):", value=50.00, step=0.01)

# Explanation of fixed costs
st.write(f"**The average cost of a filling is set to €{filling_cost}, a crown is set to €{crown_cost}, and a control procedure is set to €{control_cost}.**")

# Input fields for the number of fillings, crowns, and controls (to be used for all plans)
num_fillings = st.number_input("Enter the expected number of fillings:", value=2)
num_crowns = st.number_input("Enter the expected number of crowns:", value=1)
num_controls = st.number_input("Enter the expected number of control procedures:", value=1)

# Checkbox for coverage of control procedures (default is checked)
cover_control = st.checkbox("Does the insurance plan cover control procedures?", value=True)

# Input fields for multiple insurance plans
# Start with 3 predefined plans (max reimbursement: 250€, 500€, 1000€)
predefined_max_reimbursements = [250, 500, 1000]
num_plans = st.number_input("Number of insurance plans to compare (1-5):", min_value=1, max_value=5, value=3)

# Layout for multiple insurance plans in columns
columns = st.columns(num_plans)

plans = []
for plan_num in range(num_plans):
    with columns[plan_num]:
        st.subheader(f"Insurance Plan {plan_num + 1}")
        
        # Set default reimbursement rate to 0.75
        reimbursement_rate = st.number_input(f"Reimbursement rate (Plan {plan_num + 1}) (as a decimal):", min_value=0.0, max_value=1.0, value=0.75, step=0.01)
        
        # Predefine max reimbursement values based on plan
        max_reimbursement = st.number_input(f"Max reimbursement per year (Plan {plan_num + 1}):", 
                                           value=predefined_max_reimbursements[plan_num])
        
        # Allow decimal points for monthly premium
        monthly_premium = st.number_input(f"Monthly premium (Plan {plan_num + 1}):", value=50.00, step=0.01)
        
        # Calculate cost for the current insurance plan
        total_cost_with_insurance, annual_premium, out_of_pocket, total_without_insurance, difference = calculate_cost(
            filling_cost, crown_cost, control_cost, cover_control, reimbursement_rate, max_reimbursement, monthly_premium, num_fillings, num_crowns, num_controls
        )
        
        # Display the results (in euros), ensuring decimals
        st.write(f"**Insurance Plan {plan_num + 1} Results:**")
        st.write(f"Annual premium: €{annual_premium:,.2f}")
        st.write(f"Total cost with insurance: €{total_cost_with_insurance:,.2f}")
        st.write(f"Out of pocket expenses: €{out_of_pocket:,.2f}")
        st.write(f"Total cost without insurance: €{total_without_insurance:,.2f}")
        
        if difference < 0:
            st.write(f"**Savings with insurance:** €{-difference:,.2f}")
        else:
            st.write(f"**Extra cost with insurance:** €{difference:,.2f}")
