import {input, number, select, confirm} from "@inquirer/prompts";

const nome = await input({message:"Digite o seu nome completo: ", required: true, validate: (valor) => {
    let palavras = valor.trim().split(" ")
    

    if (palavras.length >= 2){
        return true
    }else{
        return "DIGITE NOME E SOBRENOME"
    }
}})

const idade = await number({message: "Digite sua idade: ", required: true, min:14, max:99})

const curso = await select({message: "Escolha o seu curso: ", choices: ["Desenvolvimento de Sistemas", "Informática", "Redes"]})

const turno = await select({message: "Escolha o seu turno:", choices:["Manhã", "Tarde", "Noite"]})

const bolsista = await confirm({message:"Digite se você é bolsista ou não (y/n): "})


console.log(`
----------------------
    FICHA DO ALUNO

Nome: ${nome}
Idade: ${idade} anos
Curso: ${curso}
Turno: ${turno}
Bolsista: ${(bolsista==true)?"Sim":"Não"}
    
----------------------`)

