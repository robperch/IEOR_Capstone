---- EXTRACTING ALL AGENDA ENTRIES IN THE SYSTEM


SELECT cita.citaid,
       citafecha,
       citahorad,
       citahorah,
--        c.cestatusobs,
       SUBSTRING(c.cestatusobs, '\((.+?)\)') AS fecha_creacion,
       citaestado,
       u.usuarionomfull,
       u.usuarioest,
       especialidad.especialidadnom,
       sucursal.sucursalnom,
       p.pacientenomfull

FROM cita


INNER JOIN usuario u ON cita.citadoctorid = u.usuarioid
INNER JOIN servicio ON cita.servicioid = servicio.servicioid
INNER JOIN especialidad ON u.usuarioespecialidadid = especialidad.especialidadid
INNER JOIN sucursal ON cita.citasucursalid = sucursal.sucursalid
LEFT JOIN paciente p ON cita.pacienteid = p.pacienteid
INNER JOIN citaestatus c ON cita.citaid = c.citaid AND cita.citaanio = c.citaanio


WHERE citafecha >= '2022-04-12'
  AND citafecha <= '2022-04-12'
--   AND c.cestatusobs::tsvector @@ 'Creado'::tsquery
  AND c.cestatusobs ~* '\yCreado\y'
  AND usuarionomfull LIKE '%PIEDRAS%'

ORDER BY citafecha

;