def dict_to_xml(data: dict) -> str:
    xml = f'<?xml version="1.0" ?>\n'
    xml += f'<fii>\n'
    for key, value in data.items():
        xml += f'<{key}>{value}</{key}>\n'
    xml += f'</fii>'

    return xml