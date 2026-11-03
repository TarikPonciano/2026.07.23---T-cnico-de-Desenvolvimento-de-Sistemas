-- 1. Todos os produtos com o nome da categoria, em
-- ordem alfabética, inclusive os que não têm categoria.

SELECT pr.cod_produto, pr.nome_produto, cat.nome_categoria 
FROM produtos pr
LEFT JOIN categorias cat ON pr.cod_categoria = cat.cod_categoria 
ORDER BY cat.nome_categoria ASC;

-- 2. Os pedidos com o nome e a cidade do cliente, do
-- mais antigo ao mais recente

SELECT ped.cod_pedido, cli.nome_cliente, cli.cidade_cliente, ped.data_pedido, ped.status
FROM pedidos ped
JOIN clientes cli ON cli.cod_cliente = ped.cod_cliente
ORDER BY ped.data_pedido ASC;

-- 3. Os itens do pedido 100: produto, quantidade e preço
-- pago

SELECT ped.cod_pedido, pr.nome_produto, ip.qtd, ip.preco_unit, CONCAT('R$ ', (ip.qtd * ip.preco_unit)) AS "Total R$" , ped.data_pedido
FROM itens_pedido ip
JOIN produtos pr ON pr.cod_produto = ip.cod_produto
JOIN pedidos ped ON ped.cod_pedido = ip.cod_pedido
WHERE ped.cod_pedido = 100;

-- 4. Tudo o que a Mariana Costa comprou: pedido, data e
-- produto. Dica: 4 tabelas.

SELECT cli.nome_cliente, ped.cod_pedido, ped.data_pedido, pr.nome_produto, ip.qtd ,ip.preco_unit
FROM clientes cli
JOIN pedidos ped ON ped.cod_cliente = cli.cod_cliente
JOIN itens_pedido ip ON ip.cod_pedido = ped.cod_pedido
JOIN produtos pr ON pr.cod_produto = ip.cod_produto
WHERE cli.nome_cliente = 'Mariana Costa';

-- 5. Os pedidos cancelados, com o nome do cliente e os
-- produtos.

SELECT ped.cod_pedido, cli.nome_cliente, pr.nome_produto, ped.status
FROM clientes cli
JOIN pedidos ped ON ped.cod_cliente = cli.cod_cliente
JOIN itens_pedido ip ON ip.cod_pedido = ped.cod_pedido
JOIN produtos pr ON pr.cod_produto = ip.cod_produto
WHERE ped.status = 'cancelado';

-- 6. Os clientes que nunca fizeram pedido.

SELECT DISTINCT cli.nome_cliente
FROM clientes cli
LEFT JOIN pedidos ped ON ped.cod_cliente = cli.cod_cliente
WHERE ped.cod_pedido is null;

-- 7. Os produtos que nunca foram vendidos.


-- 8. Os pedidos sem nenhum item
