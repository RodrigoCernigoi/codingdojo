document.getElementById('btnEnviar').addEventListener('click', async () => {
  const entrada = document.getElementById('entradaNumeros').value;
  const resultado = document.getElementById('resultado');

  if (!entrada) {
    resultado.textContent = 'Por favor, insira uma lista de números.';
    return;
  }

  const numeros = entrada.split(',').map(n => parseInt(n.trim(), 10));

  if (numeros.some(isNaN)) {
    resultado.textContent = 'Entrada inválida. Certifique-se de digitar apenas números separados por vírgula.';
    return;
  }

  try {
    const response = await fetch('http://localhost:5000/ordenar', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ lista: numeros }) // <- lista correta
    });

    if (!response.ok) {
      throw new Error('Erro ao se comunicar com a API.');
    }

    const data = await response.json();
    resultado.textContent = 'Lista ordenada: ' + data.ordenada.join(', '); // <- chave corrigida
  } catch (error) {
    resultado.textContent = 'Erro: ' + error.message;
  }
});
