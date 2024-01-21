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
       especialidad.especialidadnom as medical_specialty

FROM cita


INNER JOIN usuario u ON cita.citadoctorid = u.usuarioid
INNER JOIN especialidad ON u.usuarioespecialidadid = especialidad.especialidadid
INNER JOIN citaestatus c ON cita.citaid = c.citaid AND cita.citaanio = c.citaanio


WHERE citafecha >= '2023-12-01'
  AND citafecha <= '2023-12-02'
;