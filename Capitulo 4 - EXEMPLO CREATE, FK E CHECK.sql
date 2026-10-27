CREATE TABLE PACIENTE (
	COD_PACIENTE INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	NOME_PACIENTE VARCHAR(255) NOT NULL,
	ESPECIE_PACIENTE VARCHAR(255) NOT NULL DEFAULT 'Silvestre',
	RACA_PACIENTE VARCHAR(255) DEFAULT 'SRD',
	IDADE_PACIENTE INTEGER DEFAULT 0,
	PESO_PACIENTE NUMERIC(5, 2) DEFAULT 0,
	CONSTRAINT CK_ESPECIE_LISTA CHECK (
		ESPECIE_PACIENTE IN ('Gato', 'Cachorro', 'Silvestre')
	),
	CONSTRAINT CK_IDADE_VALIDA CHECK (IDADE_PACIENTE >= 0),
	CONSTRAINT CK_PESO_VALIDO CHECK (PESO_PACIENTE >= 0)
);

-- Em caso de esquecimento
-- ALTER TABLE PACIENTE
-- ADD CONSTRAINT CK_ESPECIE_LISTA CHECK (
-- 	ESPECIE_PACIENTE IN ('Gato', 'Cachorro', 'Silvestre')
-- );

-- ALTER TABLE PACIENTE
-- ADD CONSTRAINT CK_IDADE_VALIDA CHECK (IDADE_PACIENTE >= 0);

-- ALTER TABLE PACIENTE
-- ADD CONSTRAINT CK_PESO_VALIDO CHECK (PESO_PACIENTE >= 0);


CREATE TABLE veterinario (
cod_veterinario integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nome_veterinario varchar(255) NOT NULL,
especialidade_veterinario varchar(255) NOT NULL
);

CREATE TABLE consulta(
cod_consulta integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
data_consulta date NOT NULL DEFAULT CURRENT_DATE,
paciente_cod integer NOT NULL,
veterinario_cod integer NOT NULL,
CONSTRAINT fk_consulta_paciente FOREIGN KEY (paciente_cod) REFERENCES
paciente (cod_paciente),
CONSTRAINT fk_consulta_veterinario FOREIGN KEY (veterinario_cod) REFERENCES
veterinario (cod_veterinario)

);

-- ALTER TABLE consulta
-- ADD CONSTRAINT fk_consulta_paciente FOREIGN KEY (paciente_cod) REFERENCES
-- paciente (cod_paciente)
SELECT * FROM paciente;

INSERT INTO paciente (nome_paciente)
VALUES ('Toshy');

INSERT INTO veterinario (nome_veterinario, especialidade_veterinario)
VALUES ('Jones Manoel', 'Cachorro');

INSERT INTO consulta (paciente_cod, veterinario_cod)
VALUES (1, 1);


INSERT INTO paciente (nome_paciente, especie_paciente, peso_paciente, idade_paciente)
VALUES ('Leo', 'Silvestre', -120, 3)