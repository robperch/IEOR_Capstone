---- CREATING RAW TABLE POSTING DATA INTO AWS DB  x

CREATE TABLE IF NOT EXISTS raw (
   appointment_id varchar(255),
   appointment_date varchar(255),
   appointment_start_time varchar(255),
   appointment_end_time varchar(255),
   appointment_creation varchar(255),
   appointment_status varchar(255),
   doctor varchar(255),
   medical_specialty varchar(255),
   clinic varchar(255),
   patient_id int,
   patient_birth_date varchar(255),
   appointment_status_simple varchar(255));

INSERT INTO raw (
   appointment_id,
   appointment_date,
   appointment_start_time,
   appointment_end_time,
   appointment_creation,
   appointment_status,
   doctor,
   medical_specialty,
   clinic,
   patient_id,
   patient_birth_date,
   appointment_status_simple) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);