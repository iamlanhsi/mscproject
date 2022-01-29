from input import ARROW_DOWN, ARROW_LEFT, ARROW_RIGHT, ARROW_UP, C_x_, C_, M_
MAX_UNICODE = 0x110000

def is_bound(cmd):
  return cmd in binding_table

def is_insertable(cmd):
  return cmd < MAX_UNICODE

binding_table = {
  C_('D'):        "show-version",
  C_x_(C_('S')):  "save-buffer",
  C_('W'):        "split-window",
  C_x_(C_('B')) : "list-buffer",
  C_x_(C_('C')) : "editor-exit",
  ARROW_DOWN:     "next-line",
  C_('N'):        "next-line",
  ARROW_UP:       "previous-line",
  C_('P'):        "prev-line",
  ARROW_RIGHT:    "right-char",
  C_('F'):        "right-char",
  ARROW_LEFT:     "left-char",
  C_('B'):        "left-char",
  C_x_("O"):      "other-window"
}
