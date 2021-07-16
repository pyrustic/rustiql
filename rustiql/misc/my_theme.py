import tkstyle
from cyberpunk_theme import Cyberpunk
from cyberpunk_theme import constant
from cyberpunk_theme.megawidget import tree
from cyberpunk_theme.megawidget import scrollbox
from cyberpunk_theme.megawidget import confirm
from cyberpunk_theme.megawidget import table
from cyberpunk_theme.widget import frame
from cyberpunk_theme.widget import label
from cyberpunk_theme.widget import entry
from cyberpunk_theme.widget import button
from cyberpunk_theme.widget import text


# ========================================
# DATABRO THEME BASED ON CYBERPUNK THEME
# ========================================
def get_theme():
    theme = Cyberpunk()
    theme.add(_get_frame_header_bar_style(),
                    pattern="*HeaderBar")
    theme.add(_get_label_header_bar_style(),
                    pattern="*HeaderBar*Label")
    theme.add(_get_entry_database_style(),
                    pattern="*HeaderBar*Entry")
    theme.add(_get_button_expander_style(),
                    pattern="*treeExpanderButton")
    theme.add(_get_button_edit_style(),
                    pattern="*buttonEdit")
    theme.add(_get_entry_tree_title_style(),
                    pattern="*treeTitle")
    theme.add(_get_frame_collapsable_style(),
                    pattern="*CollapsableFrame")
    theme.add(_get_frame_collapsable_style(),
                    pattern="*CollapsableFrame*Frame")
    theme.add(_get_text_message_style(),
                    pattern="*CollapsableFrame*textMessage")
    theme.add(_get_button_clear_x_style(),
                    pattern="*buttonClearX")
    theme.add(_get_text_editor_style(),
                    pattern="*Editor*Text")
    theme.add(_get_label_schema_title_style(),
                    pattern="*CollapsableFrame*schemaTitle")
    theme.add(_get_button_above_table_style(),
                    pattern="*CollapsableFrame*Button")
    return theme

# ========================================
#               PRIVATE
# ========================================


# header bar
def _get_frame_header_bar_style():
    style = frame.get_style()
    return style


# Label header bar
def _get_label_header_bar_style():
    style = label.get_style()
    style.background = "#005954"
    style.foreground = "#ECFFFF"
    style.font = constant.FONT_FAV_BOLD
    return style


# Entry database on header bar
def _get_entry_database_style():
    style = entry.get_style()
    style.background = "white"
    style.readonlyBackground = "#18817C"
    style.foreground = "#ECFFFF"
    return style


# Button expander
def _get_button_expander_style():
    style = button.get_style()
    style.font = constant.FONT_FAV_BOLD
    style.background = constant.COLOR_BLACK
    style.foreground = "gray"
    style.highlightThickness = 0
    style.borderWidth = 0
    style.activeBackground = "white"
    style.activeForeground = constant.COLOR_BLACK
    style.padX = 3
    style.padY = 1
    return style


# Button edit
def _get_button_edit_style():
    style = _get_button_expander_style()
    return style


# Tree title (sql previously executed)
def _get_entry_tree_title_style():
    style = entry.get_style()
    style.readonlyBackground = constant.COLOR_BLACK
    style.font = constant.FONT_FAV_BOLD
    style.foreground = "#CFCFCF"
    style.relief = "flat"
    return style


# Collapsable frame
def _get_frame_collapsable_style():
    style = frame.get_style()
    style.background = constant.COLOR_BLACK
    return style


# Text message success
def _get_text_message_style():
    style = text.get_style()
    style.foreground = "white"
    style.background = constant.COLOR_BLACK
    style.highlightThickness = 0
    style.relief = "flat"
    return style


# button clear x
def _get_button_clear_x_style():
    style = button.get_style()
    style.anchor = "w"
    style.borderWidth = 0
    style.padX = 1
    style.padY = 0
    style.relief = "flat"
    style.foreground = "gray"
    style.highlightThickness = 0
    return style


# text editor
def _get_text_editor_style():
    style = text.get_style()
    style.background = "#005954"
    style.foreground = "white"
    style.insertBackground = "#CFCFCF"
    style.highlightThickness = 0
    style.highlightColor = "#005954"
    return style


# label schema
def _get_label_schema_title_style():
    style = label.get_style()
    style.foreground = "#E0D7D7"
    style.font = constant.FONT_FAV_BOLD
    return style


# buttons above table
def _get_button_above_table_style():
    style = button.get_style()
    style.background = constant.COLOR_BLACK
    style.foreground = "#486B6B"
    style.highlightBackground = "#486B6B"
    style.relief = "flat"
    return style
