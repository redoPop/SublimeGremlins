# Sublime Gremlins

A **Sublime Text 3** plugin to help identify invisible and ambiguous Unicode whitespace characters (zero width spaces, no-break spaces, and similar.) I call these characters gremlins, and Sublime Gremlins highlights them in the following ways:

![](https://github.com/redoPop/SublimeGremlins/raw/master/doc-images/screenshot.png)

1. The line containing the character is marked in the gutter.
2. A colored border marks the character within the line.
3. When the cursor reaches the character, the status bar displays its Unicode code position and name.

Sublime Gremlins also adds items to the command palette and edit menu, and provides some optional key bindings:

### Command palette items

Sublime Gremlins adds the following items to your command palette:

* **Gremlins: Find All** selects (with multiple cursors) all gremlins in the current view.
* **Gremlins: Find Next** selects the next gremlin from the current cursor position.
* **Gremlins: Highlight All** highlights all gremlins in the current view (happens automatically by default).
* **Gremlins: Name Current Character** Displays the Unicode code point and name of the character at the current cursor position, whether or not it's a gremlin.

### Edit menu items

Sublime Gremlins adds a couple of items to the bottom of Sublime's Find menu:

* **Find Next Gremlin** selects the next gremlin from the current cursor position.
* **Find All Gremlins** selects (with multiple cursors) all gremlins in the current view.

### Key bindings

Sublime Gremlins doesn't add any key bindings by default, but it does provide some example key bindings so [you can add your own](http://docs.sublimetext.info/en/latest/reference/key_bindings.html) if you want.

Open the list of example key bindings by selecting **Preferences ▸ Package Settings ▸ Gremlins ▸ Example Key Bindings** from the menu, then copy any key bindings you'd like to use into your personal key bindings file!
