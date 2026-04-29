# populate_licenciatura_ucs.py
# python manage.py shell < portfolio/loaderCurso.py

import requests
from portfolio.models import Licenciatura, UnidadeCurricular, Docente

Licenciatura.objects.all().delete()
UnidadeCurricular.objects.all().delete()

schoolYear = '202526'

courses = [
  457, # meisi
  6347, # mcid
  6614, # mcid-sig
  260, # lei
  1504, # di
  12, # lig
  2531, # leirt
  6638, #licma
  6634, #lcid
]

course = 260

API_COURSE = "https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail"
API_UC = "https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetSIGESCurricularUnitDetails"

headers = {"content-type": "application/json"}

payload = {
    "language": "PT",
    "courseCode": course,
    "schoolYear": schoolYear
}

response = requests.post(API_COURSE, json=payload, headers=headers)
data = response.json()

licenciatura, _ = Licenciatura.objects.update_or_create(
    nome=data.get("courseName", f"Curso {course}"),
    defaults={
        "grau": data.get("diplomaDegree", ""),
        "ects_totais": int(data.get("totalECTS") or 0),
        "duracao": str(data.get("duration") or ""),
        "url_site": data.get("url", "")
    }
)

for uc in data.get("courseFlatPlan", []):

    uc_code = uc["curricularIUnitReadableCode"]

    payload_uc = {
        "language": "PT",
        "curricularIUnitReadableCode": uc_code
    }

    response_uc = requests.post(API_UC, json=payload_uc, headers=headers)
    uc_data = response_uc.json()

    uc_obj, _ = UnidadeCurricular.objects.get_or_create(
        nome=uc_data.get("curricularUnitName") or uc.get("name") or uc_code,
        licenciatura=licenciatura,
        defaults={
            "ects": int(uc_data.get("ects") or uc.get("ects") or 0),
            "descricao": uc_data.get("programme") or uc_data.get("programContents") or "",
            "ano": int(uc.get("curricularYear") or 1),
            "semestre": uc.get("semester") or ""
        }
    )

    for doc in uc_data.get("teachers") or []:
        nome = doc.get("name")
        if not nome:
            continue

        docente, _ = Docente.objects.get_or_create(
            nome=nome,
            defaults={
                "email": doc.get("email")
            }
        )

        uc_obj.docentes.add(docente)

    uc_obj.save()

    print(f"{uc_code} — {uc_obj.nome}")