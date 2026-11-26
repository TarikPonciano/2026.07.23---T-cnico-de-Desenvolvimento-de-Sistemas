import { number, select, input } from "@inquirer/prompts";

// Imprima hello world 5 vezes
for (let i = 0; i < 5; i++){
    console.log("Hello World")
}

// Imprima seu nome 10 vezes

const nome = await input({message:"DIGITE SEU NOME: "})

for (let i = 0; i < 10; i++){
    console.log("SEJA BEM VINDO, ",nome)
}


// Faça a soma de 10 a 100

let soma = 0 

for(let i = 10; i <= 100; i++){
    soma += i
}

console.log(soma)