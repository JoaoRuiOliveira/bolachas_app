import eel

# Inicializar a aplicação web (passar a pasta com os ficheiros HTML/JS)
eel.init('web')

# Função simples em Python para interagir com o frontend
@eel.expose  # Torna a função acessível ao JavaScript
def obter_dados():
    # Aqui podemos buscar dados dos CSV ou qualquer outra lógica
    return "Dados de bolachas aqui!"

# Iniciar a app com o ficheiro HTML principal
eel.start('index.html', size=(1000, 600))  # Tamanho da janela da app