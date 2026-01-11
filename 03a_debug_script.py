#!/usr/bin/env python3
"""
Assignment 01 Part 3a: Debug BMI Health Risk Calculator

This script has THREE bugs to find and fix using VS Code debugger.
Use breakpoints, Variables panel, Watch expressions, and Debug Console.

Add comments explaining each fix when you're done.
"""


def calculate_bmi(weight_kg, height_cm):
    """Calculate BMI from weight (kg) and height (cm)."""
    height_m = height_cm / 100
    # BUG 1: Used weight/height instead of weight/(height**2)
    # FIX: Added exponent for correct BMI formula
    bmi = weight_kg / (height_m ** 2)
    return bmi

print("Debugging Assignment 01 Part 3a: BMI Health Risk Calculator")
print(f"calculate_bmi(70, 175) = {calculate_bmi(70, 175):.2f} (Expected ~22.86)")

def get_risk_level(bmi):
    """Determine health risk level based on BMI."""
    if bmi < 18.5:
        risk_lvl = "Moderate risk (underweight)"
    elif bmi < 25:
        risk_lvl = "Low risk (normal)"
    elif bmi < 30:
        risk_lvl = "Moderate risk (overweight)"
    else:
        risk_lvl = "High risk (obese)"
    # BUG 2: Incorrect risk levels assigned
    # FIX: Corrected the risk level strings to match BMI categories
    return risk_lvl


def analyze_patient_data(patients):
    """Analyze BMI and risk for multiple patients."""
    print("\nPatient Analysis:")
    print("-" * 60)

    results = []
    # BUG 3: Loop iterates one less than needed
    # FIX: Changed range to include all patients
    for i in range(len(patients)):
        name, weight, height = patients[i]
        bmi = calculate_bmi(weight, height)
        risk = get_risk_level(bmi)

        results.append({
            "name": name,
            "bmi": round(bmi, 1),
            "risk": risk
        })

        print(f"{name:15} | BMI: {bmi:5.1f} | Risk: {risk}")

    return results


def main():
    """Main function to run patient analysis."""
    print("=" * 60)
    print("BMI Health Risk Calculator - Assignment 01")
    print("=" * 60)

    # Test data: (name, weight_kg, height_cm)
    test_patients = [
        ("Patient A", 68, 170),   # Should be ~23.5 BMI (normal)
        ("Patient B", 95, 180),   # Should be ~29.3 BMI (overweight)
        ("Patient C", 52, 160),   # Should be ~20.3 BMI (normal)
        ("Patient D", 102, 175),  # Should be ~33.3 BMI (obese)
    ]

    print(f"\nAnalyzing {len(test_patients)} patients...")
    results = analyze_patient_data(test_patients)

    print("\n" + "=" * 60)
    print(f"Analysis complete: {len(results)} patients processed")
    print("=" * 60)

    # Summary statistics
    avg_bmi = sum(r["bmi"] for r in results) / len(results)
    print(f"\nAverage BMI: {avg_bmi:.1f}")

    high_risk = sum(1 for r in results if "High" in r["risk"])
    print(f"High risk patients: {high_risk}")


if __name__ == "__main__":
    main()
