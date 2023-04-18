USE parking;

DELIMITER //
CREATE TRIGGER ingresa_carro
AFTER INSERT ON `central_carrosdentro`
FOR EACH ROW
BEGIN

    IF EXISTS(SELECT * FROM `central_registrohistorico` WHERE car_placa = NEW.placa) THEN
        UPDATE `central_registrohistorico` SET status = 1 WHERE car_placa = NEW.placa ;
    ELSE 
        INSERT INTO `central_registrohistorico` (car_placa) VALUES (NEW.placa);
    END IF;

END; //

DELIMITER ;


