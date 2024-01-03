# IEOR Capstone Project
---
### Proposed business questions for initial exploratory data analysis
1. How has the no-show rate been behaving over the last 6 months?
    1. Throughout the entire company?
    2. Per location?
    3. Per medical specialty?
    4. Per month?
2. What is the cost associated to the no-show problem?
3. What is the distribution of medical specialities per clinic?
4. How many doctors per clinic?
5. Find out statistics regarding age, income, sex, demographic, locations for patients at each clinic.
---
### Proposed guidelines to collaborate
- When working on an issue, create a new branch named "i{n}", where 'n' refers to the issue number. For example, if you wanted to start working on issue #54, you would create a branch named "i54" to work on it.
- To link a pull request to an issue, use the keywords described in [this guide](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue).
---
### Data description
1. `appointment_id:` 
    - Description: unique identifier of an appointment
2. `appointment_date:` 
    - Description: date when the appointment will take place
3. `appointment_start_time:`
    - Description: time at which the appointment is scheduled to start
4. `appointment_end_time:`
    - Description: time at which the appointment is scheduled to end
5. `appointment_creation:`
    - Description: date when the appointment was created
6. `appointment_status:`
    - Description: label assigned with status information about the appointment
    - Values:
        The most important labels are
        - NO_PRESENTO: when the patient never arrived to the appointment
        - COMPLETADA: when the patient arrived to the appointment and the doctor was able to provide the service.
        - DISPONIBLE: an appointment space that is available for a patient to reserve.
        - MENSAJE_DEJADO: the staff was unsuccessful contacting the patient and only left a message.
        - NO_CONFIRMADO: The patient scheduled the appointment but hasn't confirmed it.
        - CONFIRMADO: The patient was contacted and confirmed the appointment.
7. `doctor:`
    - Description: name of the doctor that provided the service
8. `medical_specialty:`
    - Description: specialty related to the doctor that provided the service
9. `clinic:`
    - Description: clinic where the service took place
10. `patient_id:`
    - Description: patient's unique identifier
11. `patient_birth_date:`
    - Description: patient's birthdate

- Notes:
    - To count the number of appointments, we'll aggregate based on `appointment_status`:
        COMPLETADA + CONFIRMADO + DISPONIBLE + MENSAJE_DEJADO + NO_CONFIRMADO + NO_PRESENTO
    - The successful appointments will only be the ones that with the COMPLETADA `appointment_status`
    - To count the number of no-shows, we'll aggregate based on `appointment_status`:
        MENSAJE_DEJADO + NO_CONFIRMADO + NO_PRESENTO

- Additional potential features
    - Registered location of the patient
    - Patient's gender
    - Indication of whether the patient is new or a returning patient
    - Confirmation of appointment contact status with the patient
---
---
