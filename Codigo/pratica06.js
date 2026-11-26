import {number} from "@inquirer/prompts"

const numero = await number({message:"Digite um número de 1 a 10: ", min:1, max:10})

for (let i = 1; i <= 10; i++){
    const resultado = numero * i
    console.log(`${numero} X ${i} = ${resultado}`)
}