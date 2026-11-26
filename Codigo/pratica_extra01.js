// Criar um programa de menu de atendimento. O programa deve exibir as informações na tela com base no menu de exemplo abaixo e permitir que o usuário escolha uma nova opção após cada escolha. Se o usuário escolher uma opção inválida, deverá aparecer uma mensagem na tela e permitir que escolha uma nova opção.

// Menu de Opções:

// 1. Conhecer novas promoções
// 2. Receber Segunda Via do Boleto
// 3. Falar com um atendente

// 0. Sair

import {select, input} from "@inquirer/prompts"

while (true){
    const op = await select({
        message:"MENU DE OPÇÕES:",
        choices: [
            {name:"1. Conhecer novas promoções", value: 1},
            {name:"2. Receber Segunda Via do Boleto", value: 2},
            {name:"3. Falar com um atendente", value: 3},
            {name:"0. SAIR", value: 0}
        ]
    })

    if (op === 1){
        console.log("CONHECENDO PROMOÇÕES!")
    } else if (op === 2){
        console.log("EMITINDO SEGUNDA VIA DO BOLETO!")
    } else if (op === 3){
        console.log("FALANDO COM ATENDENTE")
    } else if (op === 0){
        console.log("SAINDO DO PROGRAMA...")
        break
    } else{
        console.log("VOCÊ ESCOLHEU UMA OPÇÃO INVÁLIDA!")
    }

    await input({message:"TECLE ENTER PARA CONTINUAR"})

}