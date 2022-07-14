class GameXO:
	def __init__():
		self.startGame()

	def startGame( self ):
		print("start game")
		self.cells = {}
		self.rowCount = 3
		self.columnCount = 3
		self.maxline = 3
		self.fields = {}
		self.fieldx = {}
		self.fieldx[1] = []
		self.fieldx[2] = []
		self.fieldy = {}
		self.fieldy[1] = []
		self.fieldy[2] = []
		self.fieldz = {}
		self.fieldz[1] = []
		self.fieldz[2] = []

	def fillField(self, player, xo=1):
		self.fieldx[player].append(xo)
		self.fieldy[player].append(xo)
		if row == column:
			self.fieldz[player].append(xo)

	def addXO(self, row, column, xo, player):
		self.cells.update({[row,column]: xo})
		fillField(player)

	def isEmpty(self, row, column):
		if [row, column] in self.cells.keys():
			return False
		else:
			return True
	
	def isPlayerWin(self, player):
		if player in self.fieldx.keys():
			if len(self.fieldx[player]) == self.maxline:
				return True
		if player in self.fieldy.keys():
			if len(self.fieldy[player]) == self.maxline:
				return True
		if player in self.fieldz.keys():   
			if len(self.fieldz[player]) == self.maxline:
				return True 

	def isGameOver(self):
		if len(self.cells.keys()) == self.rowCount * self.ColumnCount:
			return True

