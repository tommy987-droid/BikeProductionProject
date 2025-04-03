--
-- Struttura della tabella Production
--

CREATE TABLE Production (
  ID int(11) NOT NULL,
  ID_Batch varchar(50) NOT NULL,
  Date_Time datetime NOT NULL,
  Working_Days int(11) NOT NULL,
  ID_Bike int(11) NOT NULL,
  Time_Product int(11) NOT NULL,
  Defect varchar(50) NOT NULL
);

--
-- PRIMARY KEY per le tabella Production
--

ALTER TABLE Production
  ADD PRIMARY KEY (ID);

--
-- AUTO_INCREMENT per la tabella Production
--

ALTER TABLE Production
  MODIFY ID int(11) NOT NULL AUTO_INCREMENT;

