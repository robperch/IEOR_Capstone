# IEOR Capstone Project
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
    - We are only interested in the appointments that were made by a particular staff member of the company to provide a service to a patient.
    - We will not consider the following cases in our dataset:
        - Appointments that were canceled by patients, as these could have been rescheduled for another patient's service.
        - Appointments created as time blocks for administrative purposes.

- Additional potential features
    - Registered location of the patient
    - Patient's gender
    - Indication of whether the patient is new or a returning patient
    - Confirmation of appointment contact status with the patient
    - Amount of times that the appointment was rescheduled
---
---
