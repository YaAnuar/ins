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
		for zline in range(0, 2):
			self.fieldz.update({zline: {1: [], 2: []}})

	def fillXYLine(self, player, row, col, zline, xo=1):
		self.fieldx[row][player].append(xo)
		self.fieldy[col][player].append(xo)
		
	def fillZline(self, player, zline1, zline2, xo=1):
		self.fieldz[zline1][player].append(xo)
		if zline2 != None:
			self.fieldz[zline2][player].append(xo)

	def addXO(self, row, column, xo, player):
		self.cells.update({[row,column]: xo})

	def isEmpty(self, row, column):
		if [row, column] in self.cells.keys():
			return False
		else:
			return True
	
	def isPlayerWin(self, player, row, col, zline):
		if len(self.fieldx[row][player]) == self.maxline:
			return True
		if len(self.fieldy[col][player]) == self.maxline:
			return True
		if zline != None:
			if len(self.fieldz[zline][player]) == self.maxline:
					return True

	def isGameOver(self):
		if len(self.cells.keys()) == self.rowCount * self.ColumnCount:
			return True
