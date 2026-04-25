import os
import json
import django

# Configuração do ambiente
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings') # Ajusta 'config' para o teu projeto
django.setup()

from portfolio.models import TFC, Docente, Tecnologia

def load_tfcs(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        # Limpeza básica do ano (remover espaços e converter)
        ano_limpo = int(item['ano'].strip())
        
        # Criar ou obter o TFC
        tfc, created = TFC.objects.get_or_create(
            titulo=item['titulo'],
            defaults={
                'autores': ", ".join(item['autores']),
                'email': item.get('email'),
                'ano': ano_limpo,
                'resumo': item['resumo'],
                'imagem': item.get('imagem'),
                'pdf': item.get('pdf'),
            }
        )

        # Tratar Orientadores (ManyToManyField)
        for nome_orientador in item.get('orientadores', []):
            # Procura ou cria o docente pelo nome
            docente, _ = Docente.objects.get_or_create(nome=nome_orientador.strip())
            tfc.orientadores.add(docente)

        # Tratar Tecnologias (ManyToManyField)
        for nome_tec in item.get('tecnologias', []):
            # Limpeza: remove pontos finais e espaços (ex: " Python." -> "Python")
            nome_tec_limpo = nome_tec.strip().replace('.', '')
            tecnologia, _ = Tecnologia.objects.get_or_create(nome=nome_tec_limpo)
            tfc.tecnologias.add(tecnologia)

        if created:
            print(f"Adicionado: {tfc.titulo}")
        else:
            print(f"Já existia: {tfc.titulo}")

if __name__ == "__main__":
    # Certifica-te de que a pasta 'data' existe e o ficheiro está lá
    load_tfcs('data/TFCs.json')