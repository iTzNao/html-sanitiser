from re import sub, DOTALL

def sanitise(input_string: str) -> str:
    input_string = sub(r"<script.*?>.*?</script>", "", input_string, flags=DOTALL)
    input_string = sub(r"<[^>]+>", "", input_string)
    input_string = (
        input_string.replace("&", "&amp")
        .replace("<", "&lt")
        .replace(">", "&gt")
        .replace('"', "&quot")
        .replace("'", "&#x27")
    )

    return input_string
