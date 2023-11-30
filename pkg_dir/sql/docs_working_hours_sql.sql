---- COUNTING THE NUMBER OF HOURS THAT EACH DOCTOR WORKS IN A GIVEN PERIOD


SELECT DISTINCT ON (concat_ws('-', citafecha, citahorad, citahorah, usuario.usuarionomfull))
       citafecha,
       citahorad,
       citahorah,
--        concat_ws('-', citahorad, citahorah) AS horario,
       usuario.usuarioid,
       citaestado,
       usuario.usuarionomfull,
       especialidad.especialidadnom,
       sucursal.sucursalnom

--        COUNT(*)
--        paciente.pacientenomfull

FROM cita


INNER JOIN usuario ON cita.citadoctorid = usuario.usuarioid
INNER JOIN servicio ON cita.servicioid = servicio.servicioid
INNER JOIN especialidad ON usuario.usuarioespecialidadid = especialidad.especialidadid
INNER JOIN sucursal ON cita.citasucursalid = sucursal.sucursalid
-- INNER JOIN paciente on cita.pacienteid = paciente.pacienteid


WHERE citafecha >= '2021-08-05'
  AND citafecha <= '2021-08-06'
  AND usuarionomfull LIKE '%SAID%'
--   AND citaestado <> 'CANCELA_PACIENTE'


-- GROUP BY citafecha,
--          usuarionomfull


-- ORDER BY (concat_ws('-', citafecha, citahorad, citahorah)),
--          usuario.usuarionomfull

LIMIT 10

;