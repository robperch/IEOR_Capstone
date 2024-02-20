SELECT
       cita.citaid as appointment_id,
       c.cestatusobs,
       citaestado as appointment_status

FROM cita

         INNER JOIN citaestatus c ON cita.citaid = c.citaid AND cita.citaanio = c.citaanio


WHERE citafecha >= '2023-01-01'
  AND citafecha <= '2023-05-01'
  AND c.cestatusobs ~ ':(.*)Confirmado'
  AND citaestado = 'NO_PRESENTO'
;



SELECT cita.citaid as appointment_id,
       citafecha as appointment_date,
       citahorad as appointment_start_time,
       citahorah as appointment_end_time,
       SUBSTRING(c.cestatusobs, '\((.+?)\)') as appointment_creation,
       c.cestatusobs,
       citaestado as appointment_status,
       u.usuarionomfull as doctor,
<<<<<<< HEAD
       especialidad.especialidadnom as medical_specialty
=======
       e.especialidadnom as medical_specialty,
       su.sucursalnom as clinic,
       p.pacienteid as patient_id,
       p.pacientefnac as patient_birth_date
>>>>>>> 6bf1c0ba778a955d39fb37a3fa37429d1136d67d

FROM cita


INNER JOIN usuario u ON cita.citadoctorid = u.usuarioid
<<<<<<< HEAD
INNER JOIN especialidad ON u.usuarioespecialidadid = especialidad.especialidadid
=======
INNER JOIN servicio se ON cita.servicioid = servicio.servicioid
INNER JOIN especialidad e ON u.usuarioespecialidadid = especialidad.especialidadid
INNER JOIN sucursal su ON cita.citasucursalid = sucursal.sucursalid
LEFT JOIN paciente p ON cita.pacienteid = p.pacienteid
>>>>>>> 6bf1c0ba778a955d39fb37a3fa37429d1136d67d
INNER JOIN citaestatus c ON cita.citaid = c.citaid AND cita.citaanio = c.citaanio


WHERE citafecha >= '2023-12-01'
  AND citafecha <= '2023-12-02'
;


-- All appts
SELECT cita.citaid as appointment_id,
       citafecha as appointment_date,
       citahorad as appointment_start_time,
       citahorah as appointment_end_time,
--        SUBSTRING(c.cestatusobs, '\((.+?)\)') as appointment_creation,
       citaestado as appointment_status,
       u.usuarionomfull as doctor,
       especialidad.especialidadnom as medical_specialty,
       sucursal.sucursalnom as clinic

FROM cita


         INNER JOIN usuario u ON cita.citadoctorid = u.usuarioid
         INNER JOIN servicio ON cita.servicioid = servicio.servicioid
         INNER JOIN especialidad ON u.usuarioespecialidadid = especialidad.especialidadid
         INNER JOIN sucursal ON cita.citasucursalid = sucursal.sucursalid
         LEFT JOIN paciente p ON cita.pacienteid = p.pacienteid
         INNER JOIN citaestatus c ON cita.citaid = c.citaid AND cita.citaanio = c.citaanio


WHERE citafecha >= '2020-01-01'
  AND citafecha <= '2020-12-31'
--   AND (c.cestatusobs ~* '\yCreado\y') OR (c.cestatusobs ~* '\yCreado\y')
--   AND citaestado not in (
--                          'CANCELA_EMPLEADO',
--                          'CANCELA_PACIENTE',
--                          'BLOQUEADO',
--                          'DISPONIBLE',
--                          'TRIAGE',
--                          'TRIAGE_COMPLETO',
--                          'LISTA_ESPERA',
--                          'VALIDA_DATOS'
<<<<<<< HEAD
--     )
;
=======
--                         )

ORDER BY
    citafecha DESC

;

select * from servicio limit 10;
>>>>>>> 6bf1c0ba778a955d39fb37a3fa37429d1136d67d
