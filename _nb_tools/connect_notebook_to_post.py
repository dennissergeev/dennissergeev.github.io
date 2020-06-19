#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Use nbconvert with a custom template."""
import argparse
import re
from pathlib import Path
import sys

PATH_TO_FILES = Path(__file__).parent / "images"  # "../images/"

SCRIPT = Path(__file__).stem

YAML_INFO = """---
title: "{title}"
date: {year}-{month}-{day}
permalink: /blog/{year}/{month}/{day}/{slug}
{tags}
---"""

FOOTER = (
    "This post was written as an Jupyter Notebook. "
    "You can view or download it using "
    "[nbviewer](http://nbviewer.ipython.org/github/"
    "dennissergeev/dennissergeev.github.io/blob/master/_blog/_notebooks/"
    "{notebook_name})"
)

JINJA_TPL = """{{% extends 'markdown.tpl'%}}

## remove execution count
{{% block in_prompt -%}}
{{% endblock in_prompt %}}

{{% block data_html scoped %}}
<div>
{{{{ output.data['text/html'] }}}}
</div>
{{% endblock data_html %}}

{{% block data_png %}}
![png]({{{{ "{path_to_files}" + output.metadata.filenames['image/png'] | path2url }}}})
{{% endblock data_png %}}

{{% block data_jpg %}}
![jpeg]({{{{ "{path_to_files}" + output.metadata.filenames['image/jpeg'] | path2url }}}})
{{% endblock data_jpg %}}

{{% block body -%}}
{yaml_info}
{{{{ super() }}}}
{footer}
{{% endblock body %}}"""

NB_BASENAME_SYNTAX = (
    r"(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})-(?P<slug>[A-Za-z0-9]+)\.ipynb"
)


def parse_args(args=None):
    """Parse command-line arguments."""
    argprs = argparse.ArgumentParser(
        SCRIPT,
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="Example of use: coming soon",
    )

    argprs.add_argument("notebook", type=str, help="Path to notebook")

    argprs.add_argument("--title", type=str, required=True, help="Title of the blog post")
    argprs.add_argument("--tags", type=str, nargs="+", required=False, help="Tags of the blog post")
    # argprs.add_argument(
    #     "--thumbnail",
    #     type=str,
    #     default=THUMBNAIL_DEFAULT,
    #     help="Thumbnail of the blog post",
    # )

    return argprs.parse_args(args)


def main(args=None):
    """ Main entry point of the script """
    args = parse_args(args)

    nb_name = Path(args.notebook)
    assert nb_name.exists(), "this notebook does not exist"

    reg = re.compile(NB_BASENAME_SYNTAX)
    match = reg.match(nb_name.name)

    # if args.thumbnail:
    #     thumbnail = args.thumbnail
    # else:
    #     thumbnail = THUMBNAIL_DEFAULT
    if args.tags:
        tags = "tags:{'\n -'.join(args.tags)}"
    else:
        tags = ""

    yaml_info = YAML_INFO.format(title=args.title, tags=tags, **match.groupdict())
    footer = FOOTER.format(notebook_name=nb_name.name)

    jtpl = JINJA_TPL.format(
        yaml_info=yaml_info, footer=footer, path_to_files=PATH_TO_FILES
    )

    with nb_name.with_suffix("tpl").open("w") as fhandle:
        fhandle.writelines(jtpl)


if __name__ == "__main__":
    sys.exit(main())
