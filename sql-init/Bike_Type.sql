--
-- Crezione database
--

CREATE DATABASE IF NOT EXISTS bike;

--
-- Struttura della tabella Bike_Type
--

CREATE TABLE Bike_Type (
  ID_Type int(11) NOT NULL,
  Descri varchar(50) NOT NULL,
  Defect_Coefficient float DEFAULT NULL
);

--
-- Dump dei dati per la tabella Bike_Type
--

INSERT INTO Bike_Type (ID_Type, Descri, Defect_Coefficient) VALUES
(1, 'Mountain Bike', 0.003),
(2, 'Racing Bike', 0.007),
(3, 'Electric Bike', 0.005),
(4, 'City Bike', 0.002);

--
-- PRIMARY KEY per le tabella Bike_Type
--

ALTER TABLE Bike_Type
  ADD PRIMARY KEY (ID_Type);

--
-- AUTO_INCREMENT per la tabella Bike_Type
--

ALTER TABLE Bike_Type
  MODIFY ID_Type int(11) NOT NULL AUTO_INCREMENT;

