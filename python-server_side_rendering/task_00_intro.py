def generate_invitations(template, attendees):
    # 1. Vérifications de base
    if not isinstance(template, str):
        print("Invalid input: template must be a string")
        return

    if not isinstance(attendees, list):
        print("Invalid input: attendees must be a list")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 2. Génération des invitations
    keys = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template  # template est déjà le texte, pas un chemin

        for key in keys:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            else:
                value = str(value)

            placeholder = "{" + key + "}"
            content = content.replace(placeholder, value)

        filename = f"output_{index}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
