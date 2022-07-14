class GameXO:
	## ONLY 3x3 field
	def __init__():
		self.startGame()

	def startGame( self, rowCount=3,columnCount=3, maxLine=3 ):
		self.gameStart = True  
		self.cells = {}
		self.rowCount = rowCount
		self.columnCount = columnCount
		self.maxline = maxLine
		fieldx = {}
		fieldy = {}
		fieldz = {}
		for row in range(0,rowCount):
			self.fieldx.update({row: {1: [], 2: []}})
		for col in range(0,colCount):
			self.fieldy.update({col: {1: [], 2: []}})
		for zline in range(0, 2):
			self.fieldz.update({zline: {1: [], 2: []}})

	def fillXYLine(self, player, row, col, xo=1):
		if self.gameStart:
			self.fieldx[row][player].append(xo)
			self.fieldy[col][player].append(xo)
		
	def fillZline(self, player, zline1, zline2, xo=1):
		if self.gameStart:
			if zline1 != None:
				self.fieldz[zline1][player].append(xo)
			if zline2 != None:
				self.fieldz[zline2][player].append(xo)

	def addXO(self, row, column, xo, player):
		if self.gameStart:
			self.cells.update({[row,column]: xo})

	def isEmpty(self, row, column):
		if [row, column] in self.cells.keys():
			return False
		else:
			return True
	
	def isPlayerWin(self, player, row, col, zline1=None, zline2=None):
		if len(self.fieldx[row][player]) == self.maxline or len(self.fieldy[col][player]) == self.maxline:
			self.gameStart = False
			return True
		if zline1 != None:
			if len(self.fieldz[zline1][player]) == self.maxline:
					self.gameStart = False
					return True
		if zline2 != None:
			if len(self.fieldz[zline2][player]) == self.maxline:
					self.gameStart = False
					return True


	def isGameStarted(self):
		return self.gameStart

	def isGameOver(self):
		if self.gameStart:
			if len(self.cells.keys()) == self.rowCount * self.ColumnCount:
				self.gameStart = False
				return True

