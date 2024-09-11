create database sistemavendas;

use sistemavendas;


CREATE TABLE cliente (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(40) NOT NULL,
    sobrenome VARCHAR(40),
    cpf VARCHAR(15),
    rg VARCHAR(15),
    celular VARCHAR(15),
    telefone VARCHAR(15),
    email VARCHAR(50),
    obs VARCHAR(100),
    cep VARCHAR(12),
    endereco VARCHAR(40),
    numero VARCHAR(5),
    bairro VARCHAR(40),
    cidade VARCHAR(40),
    estado VARCHAR(2),
    INDEX (nome)
);



CREATE TABLE fornecedor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_fantasia VARCHAR(80) NOT NULL,
    razao_social VARCHAR(80),
    cnpj VARCHAR(20),
    insc_estadual VARCHAR(20),
    telefone VARCHAR(20),
    email VARCHAR(80),
    site VARCHAR(80),
    obs VARCHAR(100),
    cep VARCHAR(12),
    endereco VARCHAR(50),
    numero VARCHAR(5),
    bairro VARCHAR(40),
    cidade VARCHAR(40),
    estado VARCHAR(2),
    INDEX (nome_fantasia)
);

CREATE TABLE categoria_produto (
    id INT PRIMARY KEY AUTO_INCREMENT,
    categoria_produto VARCHAR(50),
    INDEX (categoria_produto)
);

CREATE TABLE marca_produto (
    id INT PRIMARY KEY AUTO_INCREMENT,
    marca_produto VARCHAR(50),
    INDEX (marca_produto)
);

CREATE TABLE produto (
    id INT PRIMARY KEY AUTO_INCREMENT,
    produto VARCHAR(80),
    imagem LONGBLOB,
    categoria INT,
    marca INT,
    estoque_minimo INT DEFAULT 0,
    estoque_maximo INT DEFAULT 0,
    qtde INT DEFAULT 0,
    valor_compra DECIMAL(9, 2) DEFAULT '0.00',
    valor_unitario DECIMAL(9, 2) DEFAULT '0.00',
    valor_atacado DECIMAL(9, 2) DEFAULT '0.00',
    qtde_atacado INT DEFAULT 5,
    obs VARCHAR(80),
    INDEX (produto),
    FOREIGN KEY (categoria) REFERENCES categoria_produto(id),
    FOREIGN KEY (marca) REFERENCES marca_produto(id)
);

CREATE TABLE categoria_a_pagar (
    id INT PRIMARY KEY AUTO_INCREMENT,
    categoria_a_pagar VARCHAR(80),
    INDEX (categoria_a_pagar)
);

CREATE TABLE categoria_a_receber (
    id INT PRIMARY KEY AUTO_INCREMENT,
    categoria_a_receber VARCHAR(50),
    INDEX (categoria_a_receber)
);

CREATE TABLE forma_de_pagamento (
    id INT PRIMARY KEY AUTO_INCREMENT,
    forma_pagamento VARCHAR(50),
    INDEX (forma_pagamento)
);

CREATE TABLE status_pagamento (
    id INT PRIMARY KEY AUTO_INCREMENT,
    status_pagamento VARCHAR(50),
    INDEX (status_pagamento)
);

CREATE TABLE status_entrega (
    id INT PRIMARY KEY AUTO_INCREMENT,
    status_entrega VARCHAR(50),
    INDEX (status_entrega)
);

CREATE TABLE compra (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_fornecedor INT,
    data_emissao DATE,
    prazo_entrega DATE,
    data_entrega DATE,
    categoria INT,
    desconto DECIMAL(9, 2) DEFAULT '0.00',
    frete DECIMAL(9, 2) DEFAULT '0.00',
    valor_total DECIMAL(9, 2) DEFAULT '0.00',
    valor_pago DECIMAL(9, 2) DEFAULT '0.00',
    valor_pendente DECIMAL(9, 2) DEFAULT '0.00',
    entrega INT DEFAULT 2,
    pagamento INT DEFAULT 2,
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedor(id),
    FOREIGN KEY (categoria) REFERENCES categoria_a_pagar(id),
    FOREIGN KEY (entrega) REFERENCES status_entrega(id),
    FOREIGN KEY (pagamento) REFERENCES status_pagamento(id)
);

CREATE TABLE relacao_compra (
    id VARCHAR(25) PRIMARY KEY,
    id_compra INT,
    id_produto INT,
    qtde DECIMAL(9, 2) DEFAULT '0.00',
    valor_unitario DECIMAL(9, 2) DEFAULT '0.00',
    valor_total DECIMAL(9, 2) DEFAULT '0.00',
    obs VARCHAR(50),
    FOREIGN KEY (id_compra) REFERENCES compra(id),
    FOREIGN KEY (id_produto) REFERENCES produto(id)
);

CREATE TABLE nivel (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nivel VARCHAR(40)
);


CREATE TABLE usuario (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(80),
    cpf VARCHAR(15),
    rg VARCHAR(15),
    celular VARCHAR(15),
    telefone VARCHAR(15),
    email VARCHAR(50),
    obs VARCHAR(100),
    cep VARCHAR(12),
    endereco VARCHAR(40),
    numero VARCHAR(5),
    bairro VARCHAR(40),
    cidade VARCHAR(40),
    estado VARCHAR(2),
    usuario VARCHAR(40),
    senha VARCHAR(40),
    nivel INT,
    ativo INT,
    INDEX (nome),
    INDEX (usuario),
    FOREIGN KEY (nivel) REFERENCES nivel(id)
);


CREATE TABLE venda (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    data_emissao DATE,
    prazo_entrega DATE,
    data_entrega DATE,
    categoria INT,
    desconto DECIMAL(9, 2) DEFAULT '0.00',
    frete DECIMAL(9, 2) DEFAULT '0.00',
    valor_total DECIMAL(9, 2) DEFAULT '0.00',
    valor_recebido DECIMAL(9, 2) DEFAULT '0.00',
    valor_pendente DECIMAL(9, 2) DEFAULT '0.00',
    entrega INT DEFAULT 2,
    pagamento INT DEFAULT 2,
    vendedor INT,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id),
    FOREIGN KEY (categoria) REFERENCES categoria_a_receber(id),
    FOREIGN KEY (entrega) REFERENCES status_entrega(id),
    FOREIGN KEY (pagamento) REFERENCES status_pagamento(id),
    FOREIGN KEY (vendedor) REFERENCES usuario(id)
);

CREATE TABLE relacao_venda (
    id VARCHAR(25) PRIMARY KEY,
    id_venda INT,
    id_produto INT,
    qtde DECIMAL(9, 2) DEFAULT '0.00',
    valor_unitario DECIMAL(9, 2) DEFAULT '0.00',
    valor_total DECIMAL(9, 2) DEFAULT '0.00',
    obs VARCHAR(80),
    FOREIGN KEY (id_venda) REFERENCES venda(id),
    FOREIGN KEY (id_produto) REFERENCES produto(id)
);

CREATE TABLE empresa (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_fantasia VARCHAR(80),
    razao_social VARCHAR(80),
    cnpj VARCHAR(20),
    insc_estadual VARCHAR(20),
    telefone VARCHAR(20),
    email VARCHAR(80),
    site VARCHAR(80),
    obs VARCHAR(80),
    cep VARCHAR(12),
    endereco VARCHAR(50),
    numero VARCHAR(5),
    bairro VARCHAR(40),
    cidade VARCHAR(40),
    estado VARCHAR(2),
    titulo VARCHAR(50),
    subtitulo VARCHAR(80),
    logo LONGBLOB
);

CREATE TABLE conta_a_pagar (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_compra INT,
    id_fornecedor INT,
    descricao VARCHAR(100),
    obs VARCHAR(100),
    categoria INT,
    data_vencimento DATE,
    valor DECIMAL(9, 2) DEFAULT '0.00',
    forma_pagamento INT,
    data_pagamento DATE,
    valor_pago DECIMAL(9, 2) DEFAULT '0.00',
    pagamento INT DEFAULT 2,
    FOREIGN KEY (id_compra) REFERENCES compra(id),
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedor(id),
    FOREIGN KEY (categoria) REFERENCES categoria_a_pagar(id),
    FOREIGN KEY (forma_pagamento) REFERENCES forma_de_pagamento(id),
    FOREIGN KEY (pagamento) REFERENCES status_pagamento(id)
);

CREATE TABLE conta_a_receber (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_venda INT,
    id_cliente INT,
    descricao VARCHAR(100),
    obs VARCHAR(100),
    categoria INT,
    data_vencimento DATE,
    valor DECIMAL(9, 2) DEFAULT '0.00',
    forma_pagamento INT,
    data_recebimento DATE,
    valor_recebido DECIMAL(9, 2) DEFAULT '0.00',
    pagamento INT DEFAULT 2,
    FOREIGN KEY (id_venda) REFERENCES venda(id),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id),
    FOREIGN KEY (categoria) REFERENCES categoria_a_receber(id),
    FOREIGN KEY (forma_pagamento) REFERENCES forma_de_pagamento(id),
    FOREIGN KEY (pagamento) REFERENCES status_pagamento(id)
);

select * from nivel;






