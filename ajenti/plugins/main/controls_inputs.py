from ajenti.api import *
from ajenti.ui import p, UIElement


@p('value', default='', bindtypes=[str, unicode, int])
@p('type', default='text')
@plugin
class TextBox (UIElement):
    typeid = 'textbox'


@p('value', default='', bindtypes=[str, unicode])
@p('icon', default=None)
@p('placeholder', default=None)
@plugin
class Editable (UIElement):
    typeid = 'editable'


@p('text', default='')
@p('value', default=False, bindtypes=[bool])
@plugin
class CheckBox (UIElement):
    typeid = 'checkbox'


@p('items', default=[])
@p('values', default=[])
@p('value', default='', bindtypes=[str, unicode])
@plugin
class Dropdown (UIElement):
    typeid = 'dropdown'


@p('items', default=[])
@p('values', default=[])
@p('value', default='', bindtypes=[str, unicode])
@plugin
class Combobox (UIElement):
    typeid = 'combobox'