const str = '[()()(){[][]}{([]{})}]';
// const str = '([(]{)})';

const validacionParesEstructurados = (str) => {
  let stack = [];
  const pares = {
    '[': ']',
    '(': ')',
    '{': '}',
  };
  const paresKeys = Object.keys(pares);
  const newStr = str.split('');

  for (let item of newStr) {
    if (paresKeys.includes(item)) {
      stack.push(item);
    } else {
      if (item === pares[stack[stack.length - 1]]) {
        stack.pop();
      } else {
        return 'Error: la cadena está mal estructurada';
      }
    }
  }

  return stack.length === 0 && 'La cadena esta estructurada correctamente';
};

console.log(validacionParesEstructurados(str));
