CREATE TABLE pacientes (
cod_pac integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nome_pac varchar (255) NOT NULL,
cpf_pac char(11) NOT NULL,
fone_pac varchar(20) DEFAULT 'N/A',
CONSTRAINT fk_pacientes_convenios FOREIGN KEY (cod_conv) REFERENCES convenios(cod_conv)
);

CREATE TABLE medicos (
cod_med integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
cre_med char(5) NOT NULL,
nome_med varchar (255) NOT NULL,
especialidade_med varchar (255) NOT NULL
);

CREATE TABLE convenios (
cod_conv integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nome_conv varchar (255) NOT NULL,
fone_conv varchar(20) DEFAULT 'N/A'
);

CREATE TABLE consultas (
cod_cons integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
data_cons date,
hora_cons time,
diagnostico_cons varchar (255) NOT NULL,
cod_pac integer,
cod_med integer,
CONSTRAINT fk_consultas_pacientes FOREIGN KEY (cod_pac) REFERENCES pacientes(cod_pac),
CONSTRAINT fk_consultas_medicos FOREIGN KEY (cod_med) REFERENCES medicos(cod_med),
CONSTRAINT ck_hora_valida CHECK (hora_cons BETWEEN "07:00" AND "19:00"),
UNIQUE(data_cons, hora_cons, cod_med)
);
