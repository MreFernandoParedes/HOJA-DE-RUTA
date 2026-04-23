import json
import os

RUTA = os.path.join(os.path.dirname(__file__), "..", "data", "demos.json")


def _leer():
    with open(RUTA, encoding="utf-8") as f:
        return json.load(f)


def _guardar(data):
    with open(RUTA, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_proyecto():
    return _leer()["proyecto"]


def get_secciones():
    return _leer()["secciones"]


def get_seccion(id):
    for s in get_secciones():
        if s["id"] == id:
            return s
    return None


def actualizar_estado(id, estado):
    data = _leer()
    for s in data["secciones"]:
        if s["id"] == id:
            s["estado"] = estado
    _guardar(data)
