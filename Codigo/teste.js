import {input} from '@inquirer/prompts';

const nome = await input({message:"Digite o seu nome:"})

console.log(`SEJA BEM VINDO, ${nome}`)

