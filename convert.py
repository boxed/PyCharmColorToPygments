from io import StringIO

with open(filename_goes_here) as f:
    xml = f.read()



from lxml import etree
tree = etree.parse(StringIO(xml))

keys = {}

def walk(node, path, skip_path=False):
    if 'name' in node.attrib:
        if not skip_path:
            if path:
                path += '.'
            path += node.attrib['name']

    if node.tag == 'option' and 'value' in node.attrib:
        keys[path] = f"#{node.attrib['value'].rjust(6, '0')}"

    for child in node.getchildren():
        walk(child, path=path)

walk(tree.getroot(), path='', skip_path=True)

for k, v in keys.items():
    print(k, v)


print(f"""
    background_color = "{keys['TEXT.BACKGROUND']}"

    styles = {{
        Whitespace:                "#bbbbbb",
        Comment:                   "{keys['DEFAULT_LINE_COMMENT.FOREGROUND']}",
        Comment.Preproc:           "{keys['DEFAULT_LINE_COMMENT.FOREGROUND']}",

        Keyword:                   "{keys['DEFAULT_KEYWORD.FOREGROUND']}",
        Keyword.Pseudo:            "nobold",
        Keyword.Type:              "nobold #B00040",

        Operator:                  "{keys['DEFAULT_BRACES.FOREGROUND']}",
        Operator.Word:             "{keys['DEFAULT_BRACES.FOREGROUND']}",
        Punctuation:               "{keys['DEFAULT_BRACES.FOREGROUND']}",

        Name:                      "{keys['TEXT.FOREGROUND']}",
        Name.Builtin:              "{keys['TEXT.FOREGROUND']}",
        Name.Function:             "{keys['TEXT.FOREGROUND']}",
        Name.Class:                "{keys['TEXT.FOREGROUND']}",
        Name.Namespace:            "{keys['TEXT.FOREGROUND']}",
        Name.Exception:            "{keys['TEXT.FOREGROUND']}",
        Name.Variable:             "{keys['TEXT.FOREGROUND']}",
        Name.Constant:             "{keys['TEXT.FOREGROUND']}",
        Name.Label:                "{keys['TEXT.FOREGROUND']}",
        Name.Entity:               "{keys['TEXT.FOREGROUND']}",
        Name.Attribute:            "{keys['TEXT.FOREGROUND']}",
        Name.Tag:                  "{keys['TEXT.FOREGROUND']}",
        Name.Decorator:            "{keys['DEFAULT_BRACES.FOREGROUND']}",

        String:                    "{keys['DEFAULT_STRING.FOREGROUND']}",
        String.Doc:                "{keys['DEFAULT_LINE_COMMENT.FOREGROUND']}",
        String.Interpol:           "{keys['DEFAULT_STRING.FOREGROUND']}",
        String.Escape:             "{keys['DEFAULT_STRING.FOREGROUND']}",
        String.Regex:              "{keys['DEFAULT_STRING.FOREGROUND']}",
        String.Symbol:             "{keys['DEFAULT_STRING.FOREGROUND']}",
        String.Other:              "{keys['DEFAULT_STRING.FOREGROUND']}",
        Number:                    "{keys['DEFAULT_NUMBER.FOREGROUND']}",

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#A00000",
        Generic.Inserted:          "#008400",
        Generic.Error:             "#E40000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #000080",
        Generic.Output:            "#717171",
        Generic.Traceback:         "#04D",

        Error:                     "border:#FF0000"
    }}
""")
