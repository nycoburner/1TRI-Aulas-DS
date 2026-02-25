/* A escola adota uma recuperação para cada avaliação, 
que substitui a nota do aluno caso seja maior que 
sua nota anterior.
Dada as seguintes notas, calcule a média simples 
do aluno e diga se ele está aprovado ou reprovado, 
levando em consideração a substituição de notas. */

const av1 = 6.0;
const av2 = 2.0;
const recup1 = 4.0;
const recup2 = 10.0;
let nota1;
let nota2;
let media;

if(recup1 >= av1 ) {
    console.log("Recuperação 1 é maior")
    nota1 = recup1
}
else {
    console.log ("Av1 é maior")
    nota1 = av1
}

if (recup2 >= av2) {
    console.log ("Recuperação 2 é maior")
    nota2 = recup2
}
else {
    console.log("Av2 é maior")
    nota2 = av2
}
media = (nota1 + nota2) / 2
console.log ("A media do aluno é:" + media)
if (media >= 6) {
    console.log ("Parabens! você foi aprovado!" + media)
}
else {
    console.log ("Desculpa mas está reprovado" + media)
}
