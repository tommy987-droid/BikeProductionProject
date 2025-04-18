--
-- Struttura della tabella `Task_Cost`
--

CREATE TABLE Task_Cost (
  ID_Task int(11) NOT NULL,
  Description varchar(150) NOT NULL
);

--
-- Dump dei dati per la tabella Task_Cost
--

INSERT INTO Task_Cost (ID_Task, Description) VALUES
(1, 'Assemblaggio del telaio'),
(2, 'Installazione della forcella'),
(3, 'Gruppo manubrio e cambio'),
(4, 'Installazione della leva del freno'),
(5, 'Gruppo ruota (raggi e cerchio)'),
(6, 'Installazione di pneumatici e camere d aria'),
(7, 'Installazione del deragliatore e della catena'),
(8, 'Regolazione del cambio'),
(9, 'Calibrazione del sistema frenante'),
(10, 'Installazione manubrio e manopole'),
(11, 'Installazione pedali e guarnitura'),
(12, 'Installazione di sella e reggisella'),
(13, 'Controllo qualità e regolazioni'),
(14, 'Imballaggio ed etichettatura');

--
-- PRIMARY KEY per le tabella Task_Cost
--
ALTER TABLE Task_Cost
  ADD PRIMARY KEY (ID_Task);

--
-- AUTO_INCREMENT per la tabella Task_Cost
--

ALTER TABLE Task_Cost
  MODIFY ID_Task int(11) NOT NULL AUTO_INCREMENT;