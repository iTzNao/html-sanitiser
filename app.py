def sanitise(input_string: str) -> str:
    input_string = re.sub(r"<script.*?>.*?</script>", "", input_string, flags=re.DOTALL)
    input_string = re.sub(r"<[^>]+>", "", input_string)
    input_string = (
        input_string.replace("&", "&amp")
        .replace("<", "&lt")
        .replace(">", "&gt")
        .replace('"', "&quot")
        .replace("'", "&#x27")
    )

    return input_string
