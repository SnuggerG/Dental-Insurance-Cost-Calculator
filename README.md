# Dental-Insurance-Cost-Calculator

This project is a **Dental Insurance Cost Calculator** built using **Streamlit**. It allows users to evaluate the cost of dental insurance compared to out-of-pocket expenses based on their expected dental procedures. This tool can help you decide if dental insurance is financially beneficial.

## Features

- Customize average costs for dental procedures: fillings, crowns, and control visits.
- Input expected number of procedures for the year.
- Compare up to 5 different insurance plans with:
  - Varying reimbursement rates.
  - Different maximum annual reimbursement limits.
  - Customizable monthly premiums.
- Calculates and displays:
  - Total cost with insurance.
  - Annual premium costs.
  - Out-of-pocket expenses.
  - Total cost without insurance.
  - Savings or extra cost with insurance.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/dental-insurance-calculator.git
   cd dental-insurance-calculator
   ```
2. Install the required Python dependencies:
   ```bash
   pip install streamlit
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open the provided URL in your browser to access the application.

## How to Use

1. Adjust the cost of dental procedures (fillings, crowns, and controls) to match your region.
2. Input your expected number of fillings, crowns, and control visits for the year.
3. Indicate whether control procedures are covered by the insurance plan.
4. Select the number of insurance plans to compare (1-5).
5. For each plan, specify:
   - Reimbursement rate (e.g., 0.75 for 75%).
   - Maximum annual reimbursement (in euros).
   - Monthly premium (in euros).
6. View the results for each plan, including annual premium costs, total costs with and without insurance, out-of-pocket expenses, and potential savings or extra costs with insurance.

## Example

For a scenario where:
- Fillings cost €80 each.
- Crowns cost €900 each.
- Controls cost €50 each.
- You expect 2 fillings, 1 crown, and 1 control.
- The insurance plan has a 75% reimbursement rate, a €500 max reimbursement, and a €50/month premium.

The app will calculate and display the total costs and whether the insurance plan offers savings.

## License

This project is not licensed under the MIT License. Please reach out for further details.

## Author

Created by SnuggerG. If you have any questions or suggestions, feel free to reach out!
