import {number} from "@inquirer/prompts"

const secreto = 7

let tentativas = 0

while (true) {
    const palpite = await number({message:"Digite um número de 1 a 20:", min: 1, max: 20})
    tentativas += 1

    if (palpite === secreto){
        console.log("Você acertou!")
        console.log(`Você usou ${tentativas} tentativas.`)
        break
    }

    if (palpite > secreto){
        console.log("O número secreto é menor que seu palpite.")
    }else{
        console.log("O número secreto é maior que seu palpite.")
    }

    if (tentativas >= 3){
        console.log("Suas tentativas chegaram ao fim!")
        break
    }
}