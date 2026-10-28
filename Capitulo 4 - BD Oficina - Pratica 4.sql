DROP TABLE IF EXISTS itens_os;
DROP TABLE IF EXISTS ordens_servico;
DROP TABLE IF EXISTS veiculos;
DROP TABLE IF EXISTS pecas;
DROP TABLE IF EXISTS mecanicos;
DROP TABLE IF EXISTS clientes;

CREATE TABLE clientes(
    cod_cliente integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome_cliente varchar(100) NOT NULL,
    cpf_cliente char(11) NOT NULL UNIQUE CHECK(LENGTH(cpf_cliente) == 11),
    telefone_cliente char(11) NOT NULL
);

CREATE TABLE mecanicos();

CREATE TABLE pecas();

CREATE TABLE veiculos();

CREATE TABLE ordem_servicos(
    cod_os integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    data_os date,
    descricao_os text,
    cod_veiculo integer NOT NULL,
    cod_mecanico integer NOT NULL,
    CONSTRAINT fk_os_veiculo FOREIGN KEY (cod_veiculo) REFERENCES veiculos (cod_veiculo),
    CONSTRAINT fk_os_mecanico FOREIGN KEY (cod_mecanico) REFERENCES mecanicos (cod_mecanico)
);

CREATE TABLE itens_os();