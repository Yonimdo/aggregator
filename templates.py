KEYS = ''
templates = {}
default_template = "<{param}>{value}<{param}/>"


def get_html_templtate(*args, template_parameter="", template=default_template, **kwargs):
    if template_parameter == "":
        return " ".join(args)
    else:
        if template != default_template:
            templates[template_parameter] = template
    try:
        return templates.get(template_parameter,
                             default_template.format(param=template_parameter, value="{}")).format(*args, **kwargs)
    except KeyError:
        print("{} created".format(template_parameter))


assert get_html_templtate("asd", "sdfdasf") == "asd sdfdasf"
assert get_html_templtate("1", "sdfdasf", template_parameter="b",
                          template="<b>{}</b><can>{}</cab>") == "<b>1</b><can>sdfdasf</cab>"
assert get_html_templtate("2", template_parameter="can", template="<can>{}</cab>") == "<can>2</cab>"
assert get_html_templtate("3", "sdfdasf", template_parameter="can",
                          template="<sdfdasf>{}</sdfdasf>") == "<sdfdasf>3</sdfdasf>"
assert get_html_templtate("4", "4a", template_parameter="b") == "<b>4</b><can>4a</cab>"
assert get_html_templtate("5", template_parameter="can") == "<sdfdasf>5</sdfdasf>"
assert get_html_templtate("6") == "6"




if __name__ == '__main__':
    print(get_html_templtate("1", "sdfdasf", template_parameter="b", template="<b>{}</b><can>{}</cab>"))
    print(get_html_templtate("2", template_parameter="can", template="<can>{}</cab>"))
    print(get_html_templtate("3", "sdfdasf", template_parameter="can", template="<sdfdasf>{}</sdfdasf>"))
    print(get_html_templtate("4", "4a", template_parameter="b"))
    print(get_html_templtate("5", template_parameter="can"))
    print(get_html_templtate("6"))
