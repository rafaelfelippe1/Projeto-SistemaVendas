-- Tabela Cliente
INSERT INTO cliente (nome, sobrenome, cpf, rg, celular, telefone, email, obs, cep, endereco, numero, bairro, cidade, estado)
VALUES
('João', 'Silva', '123.456.789-00', 'MG-12.345.678', '(31) 91234-5678', '(31) 1234-5678', 'joao.silva@email.com', 'Cliente preferencial', '30130-010', 'Rua A', '100', 'Centro', 'Belo Horizonte', 'MG'),
('Maria', 'Souza', '987.654.321-00', 'SP-98.765.432', '(11) 98765-4321', '(11) 4321-8765', 'maria.souza@email.com', 'Cliente novo', '04001-001', 'Avenida B', '50', 'Jardins', 'São Paulo', 'SP'),
('Carlos', 'Pereira', '456.789.123-00', 'RJ-45.678.912', '(21) 91234-8765', '(21) 1234-8765', 'carlos.pereira@email.com', 'Nenhuma observação', '20010-000', 'Rua C', '200', 'Botafogo', 'Rio de Janeiro', 'RJ');

-- Tabela Categoria de Produtos
INSERT INTO categoria_produto (categoria_produto) VALUES
('Eletrônicos'),
('Roupas'),
('Alimentos');

-- Tabela Marca Produtos
INSERT INTO marca_produto (marca_produto) VALUES
('Samsung'),
('Nike'),
('Nestlé');

-- Tabela Produtos
INSERT INTO produto (produto, imagem, categoria, marca, estoque_minimo, estoque_maximo, qtde, valor_compra, valor_unitario, valor_atacado, qtde_atacado, obs) VALUES
('Smartphone Galaxy S20', NULL, 1, 1, 10, 100, 50, 3000.00, 3500.00, 3400.00, 5, 'Smartphone topo de linha'),
('Tênis Air Max', NULL, 2, 2, 5, 50, 20, 250.00, 300.00, 290.00, 3, 'Tênis confortável e estiloso'),
('Chocolate ao Leite', NULL, 3, 3, 50, 200, 100, 2.00, 3.00, 2.80, 10, 'Chocolate cremoso e saboroso');

-- Tabela Categoria a Pagar
INSERT INTO categoria_a_pagar (categoria_a_pagar) VALUES
('Fornecedores'),
('Serviços'),
('Impostos');

-- Tabela Categoria a Receber
INSERT INTO categoria_a_receber (categoria_a_receber) VALUES
('Clientes'),
('Vendas'),
('Comissões');

-- Tabela Forma de Pagamento
INSERT INTO forma_de_pagamento (forma_pagamento) VALUES
('Dinheiro'),
('Cartão de Crédito'),
('Boleto');

-- Tabela Status Pagamento
INSERT INTO status_pagamento (status_pagamento) VALUES
('Pendente'),
('Pago'),
('Cancelado');

-- Tabela Status Entrega
INSERT INTO status_entrega (status_entrega) VALUES
('Aguardando Entrega'),
('Em Transito'),
('Entregue');

-- Tabela Compras
INSERT INTO compra (id_fornecedor, data_emissao, prazo_entrega, data_entrega, categoria, desconto, frete, valor_total, valor_pago, valor_pendente, entrega, pagamento) VALUES
(1, '2024-09-01', '2024-09-10', '2024-09-08', 1, 100.00, 50.00, 3050.00, 3050.00, 0.00, 3, 2),
(2, '2024-09-05', '2024-09-15', NULL, 2, 25.00, 10.00, 275.00, 0.00, 275.00, 1, 1);

-- Tabela Relação de Itens Comprados
INSERT INTO relacao_compra (id, id_compra, id_produto, qtde, valor_unitario, valor_total, obs) VALUES
('RC001', 1, 1, 50, 3500.00, 175000.00, 'Compra em grande quantidade'),
('RC002', 2, 2, 20, 300.00, 6000.00, 'Compra para estoque');

-- Tabela Vendas
INSERT INTO venda (id_cliente, data_emissao, prazo_entrega, data_entrega, categoria, desconto, frete, valor_total, valor_recebido, valor_pendente, entrega, pagamento, vendedor) VALUES
(1, '2024-09-01', '2024-09-10', '2024-09-08', 1, 50.00, 10.00, 3000.00, 3000.00, 0.00, 3, 2, 1),
(2, '2024-09-05', '2024-09-15', NULL, 2, 10.00, 5.00, 275.00, 0.00, 275.00, 1, 1, 2);

-- Tabela Relação de Itens Vendidos
INSERT INTO relacao_venda (id, id_venda, id_produto, qtde, valor_unitario, valor_total, obs) VALUES
('RV001', 1, 1, 10, 3500.00, 35000.00, 'Venda para cliente VIP'),
('RV002', 2, 2, 5, 300.00, 1500.00, 'Venda rápida');

-- Tabela Empresa
INSERT INTO empresa (nome_fantasia, razao_social, cnpj, insc_estadual, telefone, email, site, obs, cep, endereco, numero, bairro, cidade, estado, titulo, subtitulo, logo) VALUES
('Tech Solutions', 'Tech Solutions LTDA', '12.345.678/0001-90', '123.456.789.123', '(11) 1234-5678', 'contato@techsolutions.com.br', 'www.techsolutions.com.br', 'Empresa de tecnologia', '01000-000', 'Av. Paulista', '1000', 'Centro', 'São Paulo', 'SP', 'Sua Tecnologia', 'Inovação e qualidade', NULL);

-- Tabela Contas a Pagar
INSERT INTO conta_a_pagar (id_compra, id_fornecedor, descricao, obs, categoria, data_vencimento, valor, forma_pagamento, data_pagamento, valor_pago, pagamento) VALUES
(1, 1, 'Pagamento da compra de eletrônicos', 'Pagamento à vista', 1, '2024-09-10', 3050.00, 2, '2024-09-08', 3050.00, 2),
(2, 2, 'Pagamento da compra de tênis', 'Pagamento com desconto', 2, '2024-09-15', 275.00, 1, NULL, 0.00, 1);

-- Tabela Contas a Receber
INSERT INTO conta_a_receber (id_venda, id_cliente, descricao, obs, categoria, data_vencimento, valor, forma_pagamento, data_recebimento, valor_recebido, pagamento) VALUES
(1, 1, 'Recebimento da venda de smartphones', 'Recebido em parcela única', 1, '2024-09-10', 3000.00, 2, '2024-09-08', 3000.00, 2),
(2, 2, 'Recebimento da venda de tênis', 'Recebido com desconto', 2, '2024-09-15', 275.00, 1, NULL, 0.00, 1);

-- Tabela Nível
INSERT INTO nivel (nivel) VALUES
('Administrador'),
('Gerente'),
('Funcionário');

-- Tabela Usuários
INSERT INTO usuario (nome, cpf, rg, celular, telefone, email, obs, cep, endereco, numero, bairro, cidade, estado, usuario, senha, nivel, ativo) VALUES
('Ana Silva', '123.456.789-00', 'MG-12.345.678', '(31) 91234-5678', '(31) 1234-5678', 'ana.silva@email.com', 'Admin', '30130-010', 'Rua A', '100', 'Centro', 'Belo Horizonte', 'MG', 'ana', 'senha123', 1, 1),
('Carlos Souza', '987.654.321-00', 'SP-98.765.432', '(11) 98765-4321', '(11) 4321-8765', 'carlos.souza@email.com', 'Gerente de Vendas', '04001-001', 'Avenida B', '50', 'Jardins', 'São Paulo', 'SP', 'carlos', 'senha456', 2, 1);

 -- caso apresente erro na hora de inserir os dados dentro da tabela compra rodar as sequintes querys
SELECT * FROM fornecedor WHERE id IN (1, 2);

INSERT INTO fornecedor (nome_fantasia, razao_social, cnpj, insc_estadual, telefone, email, site, obs, cep, endereco, numero, bairro, cidade, estado) VALUES
('Fornecedor A', 'Fornecedor A LTDA', '12.345.678/0001-91', '123.456.789.123', '(11) 1111-1111', 'contato@fornecedorA.com.br', 'www.fornecedorA.com.br', 'Fornecedor principal', '01000-001', 'Rua X', '200', 'Centro', 'São Paulo', 'SP'),
('Fornecedor B', 'Fornecedor B LTDA', '12.345.678/0001-92', '123.456.789.124', '(11) 2222-2222', 'contato@fornecedorB.com.br', 'www.fornecedorB.com.br', 'Fornecedor secundário', '02000-002', 'Rua Y', '300', 'Bela Vista', 'São Paulo', 'SP');

select * from sistemavendas.usuario;

DESCRIBE usuario;

SHOW COLUMNS FROM usuario;

-- Insere dados na tabela usuario
INSERT INTO usuario (nome, cpf, rg, celular, telefone, email, obs, cep, endereco, numero, bairro, cidade, estado, usuario, senha, nivel, ativo) VALUES
('Ana Silva', '123.456.789-00', 'MG-12.345.678', '(31) 91234-5678', '(31) 1234-5678', 'ana.silva@email.com', 'Admin', '30130-010', 'Rua A', '100', 'Centro', 'Belo Horizonte', 'MG', 'ana', 'senha123', 1, 1),
('Carlos Souza', '987.654.321-00', 'SP-98.765.432', '(11) 98765-4321', '(11) 4321-8765', 'carlos.souza@email.com', 'Gerente de Vendas', '04001-001', 'Avenida B', '50', 'Jardins', 'São Paulo', 'SP', 'carlos', 'senha456', 2, 1),
('Maria Oliveira', '456.789.123-00', 'RJ-98.765.432', '(21) 98765-4321', '(21) 4321-8765', 'maria.oliveira@email.com', 'Analista', '22220-000', 'Avenida C', '150', 'Copacabana', 'Rio de Janeiro', 'RJ', 'maria', 'senha789', 1, 1),
('José Santos', '321.654.987-00', 'SP-12.345.678', '(11) 12345-6789', '(11) 9876-5432', 'jose.santos@email.com', 'Coordenador', '04001-002', 'Rua D', '200', 'Vila Mariana', 'São Paulo', 'SP', 'jose', 'senha101', 2, 0);



