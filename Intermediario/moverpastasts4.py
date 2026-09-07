import os
import shutil

# Pasta que contém todos os kits
origem = r"C:\Users\suyy\Downloads\kits\kits-20260822T153233Z-1-001\kits\Elegância Corporativa"

# Pasta para onde as duas subpastas de cada kit serão movidas
destino = r"C:\Program Files (x86)\Steam\steamapps\common\The Sims 4"


def mover_conteudo(origem, destino):
    os.makedirs(destino, exist_ok=True)

    for item in os.listdir(origem):

        caminho_origem = os.path.join(origem, item)
        caminho_destino = os.path.join(destino, item)

        # Se for uma pasta
        if os.path.isdir(caminho_origem):

            # Se já existe uma pasta com o mesmo nome no destino,
            # entra nela e mescla o conteúdo
            if os.path.exists(caminho_destino):
                mover_conteudo(caminho_origem, caminho_destino)
                os.rmdir(caminho_origem)

            # Se não existe, move a pasta inteira
            else:
                shutil.move(caminho_origem, caminho_destino)

        # Se for arquivo
        else:

            # Substitui se já existir
            if os.path.exists(caminho_destino):
                os.remove(caminho_destino)

            shutil.move(caminho_origem, caminho_destino)


# Percorre cada pasta de kit
for kit in os.listdir(origem):

    caminho_kit = os.path.join(origem, kit)

    # Ignora arquivos e pega somente as pastas dos kits
    if os.path.isdir(caminho_kit):

        # Pega as duas pastas que estão dentro do kit
        for item in os.listdir(caminho_kit):

            caminho_item = os.path.join(caminho_kit, item)

            if os.path.isdir(caminho_item):

                destino_item = os.path.join(destino, item)

                # Se a pasta já existir no destino, mescla
                if os.path.exists(destino_item):
                    mover_conteudo(caminho_item, destino_item)
                    os.rmdir(caminho_item)

                # Caso contrário, move a pasta inteira
                else:
                    shutil.move(caminho_item, destino_item)

print("Tudo foi movido com sucesso!")