

SELECT
       g.gservicionom,
       t.tservicionom,
       s.servicioid,
       s.servicioclave,
       s.servicionom


FROM servicio as s


INNER JOIN tservicio t on s.tservicioid = t.tservicioid
INNER JOIN gservicio g on s.gservicioid = g.gservicioid


-- LIMIT 10


;