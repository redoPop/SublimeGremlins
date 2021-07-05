import os
import re
import sublime
import sublime_plugin
import unicodedata

'''
---------------------------------------------------------------------
Globals
'''

# Zero-width characters
SPACELESS_GREMLINS = str.join('', [
	'\u007F-\u009F',
	'\u00AD',
	'\u200B-\u200F',
	'\u2028-\u202E',
	'\u2060-\u206F',
	'\u3164',
	'\uFE00-\uFE0F',
	'\uFEFF',
])

# Dodgy ~single-ish spaces
SPACEY_GREMLINS = str.join('', [
	'\u00A0',
	'\u2000-\u200A',
	'\u202F',
	'\u205F',
	'\u2800',
	'\u3000',
])

ALL_GREMLINS = (SPACELESS_GREMLINS + SPACEY_GREMLINS)
ALL_GREMLINS_EX = '[' + ALL_GREMLINS + ']+'
ALL_GREMLINS_RE = re.compile('^[' + ALL_GREMLINS + ']$')

PACKAGE_DIR = os.path.splitext(os.path.basename(os.path.dirname(__file__)))[0]
GUTTER_ICON = 'Packages/' + PACKAGE_DIR + '/icons/white.png'
MAX_DOC_SIZE = 1048576
REGIONS_KEY = 'gremlins-highlights'
STATUS_KEY = 'gremlins-info'

'''
---------------------------------------------------------------------
Helpers
'''

def cursor_position(view):
	return view.sel()[0].a

def char_at_cursor(view):
	return view.substr(cursor_position(view))

def settings():
	return sublime.load_settings('Gremlins.sublime-settings')

def find_all_gremlins(view):
	return view.find_all(ALL_GREMLINS_EX)

def highlight_all_gremlins(view):
	view.add_regions(
		REGIONS_KEY,
		find_all_gremlins(view),
		settings().get('gremlins_region_scope', 'invalid'),
		GUTTER_ICON,
		sublime.DRAW_NO_FILL
	)

'''
---------------------------------------------------------------------
Commands
'''

# Abstract base class for gremlin-finding commands
class GremlinsBaseFindCommand(sublime_plugin.TextCommand):
	def find_all_gremlins(self):
		return find_all_gremlins(self.view)

	def find_next_gremlin(self, from_position):
		region = self.view.find(ALL_GREMLINS_EX, from_position)
		if (not region and from_position):
			region = self.find_next_gremlin(0)
		return region

	def select_regions(self, regions):
		if (not regions):
			return
		self.view.sel().clear()
		if (type(regions) is list):
			self.view.sel().add_all(regions)
			self.view.show(regions[0])
		else:
			self.view.sel().add(regions)
			self.view.show(regions)

# Select all of the gremlins in the current view.
class GremlinsFindAllCommand(GremlinsBaseFindCommand):
	def run(self, edit):
		self.select_regions(self.find_all_gremlins())

# Select the next gremlin from the current view.
class GremlinsFindNextCommand(GremlinsBaseFindCommand):
	def run(self, edit):
		self.select_regions(self.find_next_gremlin(
			cursor_position(self.view) + 1
		))

# Highlight all the gremlins in the current view.
class GremlinsHighlightAllCommand(GremlinsBaseFindCommand):
	def run(self, edit):
		highlight_all_gremlins(self.view)

# Use the status bar to show the name of whichever character
# is currently under the user's cursor.
class GremlinsNameCurrentCommand(sublime_plugin.WindowCommand):
	last_named_position = None

	def run(self, **args):
		view = self.window.active_view()
		position = cursor_position(view)
		char = char_at_cursor(view)
		message = ''

		if ALL_GREMLINS_RE.match(char):
			message += '\U0001f440 '
		elif args.get('clearStatusIfNotGremlin'):
			if position != self.last_named_position:
				view.erase_status(STATUS_KEY)
			return

		message += u'U+{:04X}'.format(ord(char))

		try:
			name = unicodedata.name(char)
			message += ' (' + name + ')'
		except:
			pass

		self.last_named_position = position
		view.set_status(STATUS_KEY, message)

# Edit the key bindings file
class GremlinsEditKeyBindingsCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.run_command('edit_settings', {
			'base_file': '${packages}/' + PACKAGE_DIR + '/Example.sublime-keymap',
			'user_file': '${packages}/User/Default (${platform}).sublime-keymap',
			'default': '[\n\t$0\n]\n',
		})

# Edit the settings file
class GremlinsEditSettingsCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.run_command('edit_settings', {
			'base_file': '${packages}/' + PACKAGE_DIR + '/Gremlins.sublime-settings',
			'default': '// Settings in here override those in "Gremlins.sublime-settings"\n{\n\t$0\n}\n',
		})

'''
---------------------------------------------------------------------
Listeners
'''

# Highlight all the gremlins in the current view.
class GremlinsHighlighterListener(sublime_plugin.EventListener):
	def highlight_all_gremlins(self, view):
		if view.size() <= MAX_DOC_SIZE:
			highlight_all_gremlins(view)

	def on_activated_async(self, view):
		self.highlight_all_gremlins(view)

	def on_clone_async(self, view):
		self.highlight_all_gremlins(view)

	def on_load_async(self, view):
		self.highlight_all_gremlins(view)

	def on_modified_async(self, view):
		self.highlight_all_gremlins(view)

# Use the status bar to display the name of the gremlin
# currently under the user's cursor.
class GremlinsNamerListener(sublime_plugin.EventListener):
	def name_current_gremlin(self, view):
		if view.window():
			view.window().run_command('gremlins_name_current', {
				"clearStatusIfNotGremlin": True
			})

	def on_activated_async(self, view):
		self.name_current_gremlin(view)

	def on_selection_modified_async(self, view):
		self.name_current_gremlin(view)
