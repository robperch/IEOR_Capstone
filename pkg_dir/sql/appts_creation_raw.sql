---- EXTRACTING ALL AGENDA ENTRIES IN THE SYSTEM


SELECT
       citafecha,
       citahorad,
       citahorah,
       SUBSTRING(c.cestatusobs, '\((.+?)\)') AS fecha_creacion,
       citaestado,
       u.usuarioid,
       u.usuarionomfull,
       especialidad.especialidadnom,
       sucursal.sucursalnom,
       p.pacientenomfull

FROM cita


INNER JOIN usuario u ON cita.citadoctorid = u.usuarioid
INNER JOIN servicio ON cita.servicioid = servicio.servicioid
INNER JOIN especialidad ON u.usuarioespecialidadid = especialidad.especialidadid
INNER JOIN sucursal ON cita.citasucursalid = sucursal.sucursalid
LEFT JOIN paciente p on cita.pacienteid = p.pacienteid
LEFT JOIN citaestatus c ON cita.citaid = c.citaid AND cita.citaanio = c.citaanio


WHERE citafecha >= '2022-04-09'
  AND citafecha <= '2022-04-10'
  AND c.cestatusobs ~* '\yCreado\y'
--   AND ((usuarionomfull LIKE $3) OR (usuarionomfull LIKE $4))

;