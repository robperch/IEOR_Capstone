---- EXTRACTING ALL AGENDA ENTRIES IN THE SYSTEM


SELECT cita.citaid as appointment_id,
       citafecha as appointment_date,
       citahorad as appointment_start_time,
       citahorah as appointment_end_time,
--        SUBSTRING(c.cestatusobs, '\((.+?)\)') as appointment_creation,
       c.cestatusobs,
       citaestado as appointment_status,
       u.usuarionomfull as doctor,
       e.especialidadnom as medical_specialty,
       su.sucursalnom as clinic,
       p.pacienteid as patient_id,
       p.pacientefnac as patient_birth_date

FROM cita


INNER JOIN usuario u ON cita.citadoctorid = u.usuarioid
INNER JOIN servicio se ON cita.servicioid = servicio.servicioid
INNER JOIN especialidad e ON u.usuarioespecialidadid = especialidad.especialidadid
INNER JOIN sucursal su ON cita.citasucursalid = sucursal.sucursalid
LEFT JOIN paciente p ON cita.pacienteid = p.pacienteid
INNER JOIN citaestatus c ON cita.citaid = c.citaid AND cita.citaanio = c.citaanio


WHERE citafecha >= '2000-11-03'
  AND citafecha <= '2021-01-01'
--   AND c.cestatusobs ~* '\yCreado\y'
--   AND citaestado not in (
--                          'CANCELA_EMPLEADO',
--                          'CANCELA_PACIENTE',
--                          'BLOQUEADO',
--                          'DISPONIBLE',
--                          'TRIAGE',
--                          'TRIAGE_COMPLETO',
--                          'LISTA_ESPERA',
--                          'VALIDA_DATOS'
--                         )

ORDER BY
    citafecha DESC

;

select * from servicio limit 10;