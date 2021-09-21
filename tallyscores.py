from openpyxl import PatternFill, Font

def color_fill(ws, score, row_num):
  line = ws.cell(row=row_num, column=2).split(' ')
  score_split = score.split(' ')

  # cycle through four pick columns; odd = common, even = spread
  for col in range(5, 9):
    pick_cell = ws.cell(row=row_num, column=col)

    # common pick
    if pick_cell % 2 == 1:
      pick_cell_split = pick_cell.split(' ')

      # if pick team == winning team, color cell green
      if pick_cell_split[0] == score_split[0]:
        pick_cell.fill = PatternFill("solid", fgColor="009051")
        spread = score_split[1].split('-')

        # if game spread == pick spread, spread font == yellow
        if spread[0] - spread[1] == pick_cell_split[2]:
          pick_cell.font = Font(color="FFFB00")
      # else color cell red    
      else:
        pick_cell.fill = PatternFill("solid", fgColor="FF7E79")

    # against line
    else:
      return