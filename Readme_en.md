## Centered Paper for Xed

A tiny plugin for Xed
 that turns the editor into a simple, centered "sheet of paper".

It adds wide grey margins around the editing area, leaving a white paper-like area in the middle of the window.

The plugin is intended mainly for comfortable, distraction-free writing.

## Features

Centered white paper approximately 80 characters wide

Grey area outside the paper

Thin border on both sides of the paper

Automatically adapts to window size

Automatically adapts to font changes

F10 toggles the centered-paper mode on and off

Does not modify the document contents

Does not affect saving or exporting

Works independently of document format or tools such as Pandoc

## Keyboard shortcuts
Key	Action
F10	Toggle centered paper

Other shortcuts are provided by Xed itself.

For example, a comfortable writing setup can be:

F9 — side panel / tags

F10 — centered paper

F11 — fullscreen

## Installation

1. Create the plugin directory:

mkdir -p ~/.local/share/xed/plugins/centered-paper


2. Copy these two files into it:

centered-paper/
├── centered-paper.plugin
└── centered_paper.py


The plugin file should contain:

[Plugin]
Loader=python3
Module=centered_paper


3. Then enable Centered Paper in:

Xed → Preferences → Plugins

Restart Xed

## Checking the Python file

Before starting Xed, the Python file can be checked with:

python3 -m py_compile ~/.local/share/xed/plugins/centered-paper/centered_paper.py


No output means that the Python syntax is valid.

Tested with

Xed 3.8.9

GTK 3

GtkSourceView 4

Python 3

It may work with other versions of Xed as well, but compatibility with future versions is not guaranteed.

## Notes

This plugin only changes the visual presentation of the editor.

The "paper" is not part of the document. It is drawn by the plugin and therefore has no effect on:

Markdown

HTML

LaTeX

plain text

Pandoc

printing or exporting

The document itself remains unchanged.

## Maintenance

This is a small personal-use plugin released mainly because it may be useful to other Xed users.

It was written and tested for Xed 3.8.9.

Future versions of Xed may change its plugin API or GTK integration and could therefore require changes to the plugin.

If it stops working with a newer Xed version, feel free to fork it and fix it.

Maintenance status: works for me. 🙂

## License

Copyright © 2026

This project is released under the MIT License.
