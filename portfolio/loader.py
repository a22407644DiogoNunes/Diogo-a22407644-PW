import json
from portfolio.models import Tecnologia, TFC

# como correr
# python manage.py shell
# from portfolio import loader

Tecnologia.objects.all().delete()
TFC.objects.all().delete()

with open('./data/TFCs.json', encoding='utf-8') as f:
    data = json.load(f)

    # caso seja só 1 objeto
    if isinstance(data, dict):
        data = [data]

    for item in data:

        # criar TFC
        tfc = TFC.objects.create(
            nome=item["titulo"],
            autores=", ".join(item["autores"]),
            email=item.get("email"),
            orientadores=", ".join(item["orientadores"]),
            ano=int(item["ano"].strip()),
            resumo=item["resumo"],
            imagem=item.get("imagem"),
            pdf=item.get("pdf")
        )

        # tecnologias (ManyToMany)
        for tech_nome in item.get("tecnologias") or []:
            tech_nome = tech_nome.strip().replace(".", "")

            tecnologia, created = Tecnologia.objects.get_or_create(
                nome=tech_nome,
                defaults={
                    "descricao": "",
                    "interesse_pessoal": False
                }
            )

            tfc.tecnologias.add(tecnologia)