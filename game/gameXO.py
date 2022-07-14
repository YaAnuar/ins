class GameXO:
	def __init__():
		self.startGame()

	def startGame( self ):
		print("start game")
		self.cells = {}
		self.rowCount = 3
		self.columnCount = 3
		self.maxline = 3
		fieldx = {}
		fieldy = {}
		fieldz = {}
		for row in range(0,rowCount):
			self.fieldx.update({row: {1: [], 2: []}})
		for col in range(0,colCount):
			self.fieldy.update({col: {1: [], 2: []}})
		for zline in range(0, rowCount/columnCount):
			self.fieldz.update({zline: {1: [], 2: []}})

	def fillField(self, player, row, col, xo=1):
		self.fieldx[row][player].append(xo)
		self.fieldy[col][player].append(xo)
		if row == column:
			self.fieldz[row/col][player].append(xo)

	def addXO(self, row, column, xo, player):
		self.cells.update({[row,column]: xo})
		fillField(player,row,column, 1)

	def isEmpty(self, row, column):
		if [row, column] in self.cells.keys():
			return False
		else:
			return True
	
	def isPlayerWin(self, player, row, col):
		if len(self.fieldx[row][player]) == self.maxline:
			return True
		if len(self.fieldy[col][player]) == self.maxline:
			return True
		if row == col:
			if len(self.fieldz[row/col][player]) == self.maxline:
				return True

	def isGameOver(self):
		if len(self.cells.keys()) == self.rowCount * self.ColumnCount:
			return True
