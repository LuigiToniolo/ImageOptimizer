from PIL import Image
import os

def otimizar_imagens(diretorio_entrada, diretorio_saida, largura_maxima, qualidade):
    # Verifique se o diretório de saída existe; se não, crie-o
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)

    for arquivo in os.listdir(diretorio_entrada):
        if arquivo.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Abra a imagem
            imagem = Image.open(os.path.join(diretorio_entrada, arquivo))

            # Redimensione a imagem para a largura máxima especificada
            largura_original, altura_original = imagem.size
            if largura_original > largura_maxima:
                nova_altura = int(altura_original * (largura_maxima / largura_original))
                imagem = imagem.resize((largura_maxima, nova_altura))

            # Converta a imagem para o formato WEBP
            nome_arquivo, extensao = os.path.splitext(arquivo)
            caminho_webp = os.path.join(diretorio_saida, nome_arquivo + ".webp")
            imagem.save(caminho_webp, format="WEBP", quality=qualidade)

def main():
    diretorio_entrada = "imagensEntrada"
    diretorio_saida = "ImagensSaida"

    if not os.path.exists(diretorio_entrada):
        print(f"O diretório '{diretorio_entrada}' não existe. Coloque suas imagens na pasta e execute o programa novamente.")
        return

    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)

    while True:
        try:
            largura_maxima = int(input("Digite a largura máxima desejada em pixels: "))
            qualidade = int(input("Digite a qualidade da imagem (0-100): "))

            otimizar_imagens(diretorio_entrada, diretorio_saida, largura_maxima, qualidade)

            print(f"Imagens otimizadas e convertidas para WEBP com largura máxima de {largura_maxima}px e qualidade {qualidade}.")
            for arquivo in os.listdir(diretorio_saida):
                if arquivo.endswith('.webp'):
                    imagem = Image.open(os.path.join(diretorio_saida, arquivo))
                    largura, altura = imagem.size
                    print(f"Dimensão da imagem '{arquivo}': Largura: {largura}px, Altura: {altura}px")
            break
        except ValueError:
            print("Valores inválidos. Tente novamente.")

if __name__ == "__main__":
    main()

