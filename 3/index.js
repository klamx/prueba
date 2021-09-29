const str = 'hello world, big WoRld';
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
