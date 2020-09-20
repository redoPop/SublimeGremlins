# Sublime Gremlins
A **Sublime Text 3** plugin to help identify invisible and ambiguous Unicode whitespace characters (zero width spaces, no-break spaces, and similar.) I call these characters gremlins, and Sublime Gremlins highlights them in the following ways:

![](https://github.com/redoPop/SublimeGremlins/raw/master/doc-images/screenshot.png)

1. The line containing the character is marked in the gutter.
2. A colored border marks the character within the line.
3. When the cursor reaches the character, the status bar displays its Unicode code position and name.

This plugin also adds commands to identify and select (for removal/replacement) any gremlins in the current document.

## Installation
Sublime Gremlins is available on [Package Control:](https://packagecontrol.io/)

1. Open Sublime Text's command palette
2. Select the "Package Control: Install Package" command
3. Search & select the ["Gremlins"](https://packagecontrol.io/packages/Gremlins) package

If you prefer, install via git:
```
git clone https://github.com/redoPop/SublimeGremlins.git \
  "~/Library/Application Support/Sublime Text 3/Packages/Gremlins"
```

## Command palette
Sublime Gremlins adds the following to your command palette:

* **Gremlins: Find All** selects (with multiple cursors) all gremlins in the current view.
* **Gremlins: Find Next** selects the next gremlin from the current cursor position.
* **Gremlins: Highlight All** highlights all gremlins in the current view (happens automatically by default).
* **Gremlins: Name Current Character** Displays the Unicode code point and name of the character at the current cursor position, whether or not it's a gremlin.

## Find menu
Sublime Gremlins adds a couple of items to the bottom of Sublime's Find menu:

* **Find Next Gremlin** selects the next gremlin from the current cursor position.
* **Find All Gremlins** selects (with multiple cursors) all gremlins in the current view.

## Key bindings
Sublime Gremlins doesn't add any key bindings by default, but it does provide some example key bindings so [you can add your own](http://docs.sublimetext.info/en/latest/reference/key_bindings.html) if you want.

Select **Preferences ▸ Package Settings ▸ Gremlins ▸ Key Bindings** from the menu. This will open a two-pane view with Gremlins' example key bindings on the left and your personal key bindings file on the right. Copy over any key bindings you want to use.
