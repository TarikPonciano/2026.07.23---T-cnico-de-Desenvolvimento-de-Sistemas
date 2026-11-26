import { number, select } from "@inquirer/prompts";

const listaFormaPagamento = [
  { name: "Cartão de Crédito", value: 1 },
  { name: "Pix (-5%)", value: 2 },
];

const valorCompra = await number({
  message: "Digite o valor da compra: R$",
  min: 0,
  step: 0.01,
});

const formaPagamento = await select({
  message: "Escolha uma forma de pagamento: ",
  choices: listaFormaPagamento,
});

let desconto = 0

if (valorCompra >= 50){
    desconto = 0.1
} else if (valorCompra > 20 && valorCompra < 50){
    desconto = 0.05
} else{
    desconto = 0
}

if (formaPagamento === 2){
    desconto += 0.05
}

const valorFinal = valorCompra * (1-desconto)

console.log(`Valor Total da Compra: ${valorFinal.toLocaleString("pt-BR",{style:"currency", currency:"BRL"})}`)
