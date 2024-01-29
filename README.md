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
6. `appointment_status_simplified:`
    - Description: A simplified tag that indicates the final status of the appointment.
    - Values:
        - no_show: indicates when the patient did not arrive for their appointment.
        - completed: denotes when the patient arrived for their appointment, and the doctor was able to provide the service.
        - unused: refers to appointment space that was left unused.
        - cancel_patient: indicates an appointment canceled by the patient.
        - cancel_employee: indicates an appointment canceled by the company for a specific reason, such as the patient not confirming the appointment. (Note: all appointments automatically canceled by the system are associated with the user 'citas.online')
        - blocked: refers to appointment times that were made unavailable for administrative purposes. For example, if the doctor had to leave for an emergency, their available appointments would be blocked.
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
12. metadata columns
    - Description: All columns that start with 'meta__' and end with either '$date' or '$user' are considered metadata columns. These columns contain information extracted from the appointment notes collected over time. For instance, if a staff member updates the status of an appointment to 'confirmed' to indicate that the patient has confirmed the appointment, the system records the user and the date and time when the status was changed.

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
