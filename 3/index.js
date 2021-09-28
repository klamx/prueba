const str = 'hello world, big WoRld';
// const str =
//   'Hola que tal soy el chico de las poesias que tal hola hola que tal soy el poesias chico chico';
const re = /[^A-Za-z\s]/;
const newStr = str.toLowerCase().replace(re, '').split(' ');

const contadorPalabras = (newStr) => {
  return newStr.reduce((x, y) => {
    if (x[y]) x[y]++;
    else x[y] = 1;

    return x;
  }, {});
};

console.log(contadorPalabras(newStr));
