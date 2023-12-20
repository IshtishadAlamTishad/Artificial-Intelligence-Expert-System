P_heartDiseaseConditions = {
    ('Young', 'Normal', 'Normal'): 0.15,
    ('Young', 'Normal', 'High'): 0.24,
    ('Young', 'High', 'Normal'): 0.011,
    ('Young', 'High', 'High'): 0.6655,
    ('Old', 'Normal', 'Normal'): 0.03,
    ('Old', 'Normal', 'High'): 0.0005,
    ('Old', 'High', 'Normal'): 0.1021,
    ('Old', 'High', 'High'): 0.8088,
}
P_age = {'Young': 0.45, 'Old': 0.65}
P_cholesterol = {'Normal': 0.5, 'High': 0.5}
P_blood_pressure = {'Normal': 0.6, 'High': 0.4}
age_condition = 'Old'
cholesterol_condition = 'High'
blood_pressure_condition = 'Normal'
denominator = 0
for age in ['Young', 'Old']:
    for cholesterol in ['Normal', 'High']:
        for blood_pressure in ['Normal', 'High']:
            probability = (
                    P_heart_disease_given_conditions[(age, cholesterol, blood_pressure)]
                    * P_age[age]
                    * P_cholesterol[cholesterol]
                    * P_blood_pressure[blood_pressure]
            )
            denominator += probability

numerator = P_heart_disease_given_conditions[(age_condition, cholesterol_condition, blood_pressure_condition)]
heart_disease_probability = numerator/denominator

print(f'Probability of Heart Disease: {heart_disease_probability:.4f}')

