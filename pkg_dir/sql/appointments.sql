---- EXTRACTING ALL AGENDA ENTRIES IN THE SYSTEM


SELECT cita.citaid as appointment_id,
       citafecha as appointment_date,
       citahorad as appointment_start_time,
       citahorah as appointment_end_time,
       SUBSTRING(c.cestatusobs, '\((.+?)\)') as appointment_creation,
       citaestado as appointment_status,
       u.usuarionomfull as doctor,
       especialidad.especialidadnom as medical_specialty,
       sucursal.sucursalnom as clinic,
       p.pacienteid as patient_id,
       p.pacientefnac as patient_birth_date

FROM cita


INNER JOIN usuario u ON cita.citadoctorid = u.usuarioid
INNER JOIN servicio ON cita.servicioid = servicio.servicioid
INNER JOIN especialidad ON u.usuarioespecialidadid = especialidad.especialidadid
INNER JOIN sucursal ON cita.citasucursalid = sucursal.sucursalid
LEFT JOIN paciente p ON cita.pacienteid = p.pacienteid
INNER JOIN citaestatus c ON cita.citaid = c.citaid AND cita.citaanio = c.citaanio


WHERE citafecha >= '2023-12-15'
  AND citafecha <= '2023-12-31'
  AND c.cestatusobs ~* '\yCreado\y'
  AND citaestado not in (
                         'CANCELA_EMPLEADO',
                         'CANCELA_PACIENTE',
                         'BLOQUEADO',
                         'DISPONIBLE',
                         'TRIAGE',
                         'TRIAGE_COMPLETO',
                         'LISTA_ESPERA',
                         'VALIDA_DATOS'
                        )
;