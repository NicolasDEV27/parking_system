USE parking;

DELIMITER //
CREATE TRIGGER delete_car
AFTER DELETE ON `central_carrosdentro`
FOR EACH ROW
BEGIN

    IF OLD.placa = `central_registrohistorico`.car_placa THEN
        UPDATE `central_registrohistorico` SET status = 0 WHERE car_id = OLD.id ;
    END IF;

END; //

DELIMITER ;