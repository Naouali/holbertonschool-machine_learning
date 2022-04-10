-- Safe divide function
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$

CREATE FUNCTION SafeDiv ( a INT, b INT)
RETURNS FLOAT

BEGIN
    DECLARE rsl FLOAT;
    SET rsl = IF (b = 0, 0, a / b);
    RETURN rsl;
END $$
DELIMITER ;