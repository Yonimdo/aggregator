import re

templates = {}
default_template = "<{param}>{value}</{param_end}>"
match = re.compile(r"^(\w+)(\s)")


def get_html_templtate(*args, template_parameter="", template=default_template, **kwargs):
    if template_parameter == "":
        return " ".join(args)
    else:
        if template != default_template:
            templates[template_parameter] = template.replace('\n', ' ')
    try:
        end = match.search(template_parameter)
        end = end.group(1) if end else template_parameter
        return templates.get(template_parameter,
                             default_template.format(param=template_parameter,
                                                     param_end=end
                                                     , value="{}")).format(
            *args, **kwargs)
    except KeyError:
        # heppands when args or kwargs is empty
        print("{} templates created didn't return a template because no args/kwargs.".format(template_parameter))


# fast assertion area (when prod should cp to Unit test?)
# -------------------------------------------------------
assert get_html_templtate("asd", "sdfdasf") == "asd sdfdasf"
assert get_html_templtate("1", "sdfdasf", template_parameter="b",
                          template="<b>{}</b><can>{}</cab>") == "<b>1</b><can>sdfdasf</cab>"
assert get_html_templtate("2", template_parameter="can", template="<can>{}</cab>") == "<can>2</cab>"
assert get_html_templtate("3", "sdfdasf", template_parameter="can",
                          template="<sdfdasf>{}</sdfdasf>") == "<sdfdasf>3</sdfdasf>"
assert get_html_templtate("4", "4a", template_parameter="b") == "<b>4</b><can>4a</cab>"
assert get_html_templtate("5", template_parameter="can") == "<sdfdasf>5</sdfdasf>"
assert get_html_templtate("6") == "6"
assert get_html_templtate(name='7', template_parameter="b", template="<b>{name}</b>") == "<b>7</b>"
# ---------------------------------------------------------------------
templates = {}  # #cleans the templates area after assertion..(my bad...)

if __name__ == '__main__':
    print(
        "this is a cache templating area... only one function 'get_html_templtate' that recive "
        " ('1', 'sdfdasf', template_parameter='b', template='<b>{}</b><can>{}</cab>')")
    print("and outputs")
    print(get_html_templtate("1", "sdfdasf", template_parameter="b", template="<b>{}</b><can>{}</cab>"))
    print(
        "this is a dynamic area... after first insertion we can use the same template like so ('1 a ', 'moody', template_parameter='b')")
    print(get_html_templtate("1 a ", "moody", template_parameter="b"))
    print("from now on we can use b .. but we will have insertion Error if we will try it without the same args.")
    print("if you using 'template' param  know what you are doing.")
    print("if you want quick wrap use the  'template_parameter' get_html_templtate('1 b', template_parameter='can') .")
    print("this will output")
    print(get_html_templtate("1 b", template_parameter="can"))
    print("and more 'template_parameter' get_html_templtate('1 c', template_parameter='b class='as'') .")
    print(get_html_templtate("1 c", template_parameter="b class='as'"))
    print(
        "Note that 'b' and 'b class='as'' are different templates if we want a surtcut ('1 d', template_parameter='b', template='<b class'as'>{}<b>') ")
    print(get_html_templtate("1 d", template_parameter="b", template="<b class'as'>{}<b>"))
    print(
        "or a better shortcut  (kwargs={'name': 'title'},  template_parameter='b', template='<b class'as'>{name}<b>') ")
    print(get_html_templtate(name='title', template_parameter="b", template="<b class'as'>{name}<b>"))
