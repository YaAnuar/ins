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
		self.fields.update({"fieldx": {1: [], 2: []}})
		self.fields.update({"fieldy": {1: [], 2: []}})
		self.fields.update({"fieldz": {1: [], 2: []}})

	def fillField(self, player, xo=1):
		self.fields["fieldx"][player].append(xo)
		self.fields["fieldy"][player].append(xo)
		if row == column:
			self.fields["fieldz"][player].append(xo)

	def addXO(self, row, column, xo, player):
		self.cells.update({[row,column]: xo})
		fillField(player, 1)

	def isEmpty(self, row, column):
		if [row, column] in self.cells.keys():
			return False
		else:
			return True
	
	def isPlayerWin(self, player):
		if len(self.fields["fieldx"][player]) == self.maxline:
			return True
		if len(self.fields["fieldy"][player]) == self.maxline:
			return True
		if len(self.fields["fieldz"][player]) == self.maxline:
			return True

	def isGameOver(self):
		if len(self.cells.keys()) == self.rowCount * self.ColumnCount:
			return True

