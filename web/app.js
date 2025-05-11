// Ligar ao Python através do Eel
const button = document.getElementById("obter-dados");
const dadosElement = document.getElementById("dados");

button.addEventListener("click", async () => {
    const dados = await eel.obter_dados()();  // Chama a função Python
    dadosElement.innerText = dados;  // Exibe os dados no HTML
});