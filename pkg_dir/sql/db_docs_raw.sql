-- SCRIPT TO OBTAIN ALL DOCTORS STORED IN THE DATABASE


SELECT usuarioid,
--        puestoid,
       usuarionomfull,
       e.especialidadnom,
       usuarioest
--        puestoid

FROM usuario


LEFT JOIN especialidad e on usuario.usuarioespecialidadid = e.especialidadid


WHERE puestoid = 'MEDICO'
-- WHERE usuarionomfull ILIKE '%silv%'
--   AND puestoid = 'MEDICO'


ORDER BY
         usuarioest,
         usuarionomfull


;