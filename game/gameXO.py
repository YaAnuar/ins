class GameXO:
	def __init__():
		self.startGame()

	def startGame( self ):
		print("start game")
		self.cells = {}
		self.rowCount = 3
		self.columnCount = 3
		self.fieldx = {}
		self.fieldx[1] = []
		self.fieldx[2] = []
		self.fieldy = {}
		self.fieldy[1] = []
		self.fieldy[2] = []
		self.fieldz = {}
		self.fieldz[1] = []
		self.fieldz[2] = []

	def fillField(self, player):
		self.fieldx[player].append(player)
		self.fieldy[player].append(player)
		if row == column:
			self.fieldz[player].append(player)

	def addXO(self, row, column, xo, player):
		self.cells.update([row,column]: xo)
		fillField(player)

	def isEmpty(self, row, column):
		if [row, column] in self.cells.keys():
			return False
		else:
			return True
	
	def isPlayerWin(self, player):
		if player in fieldx.keys():
			if len(self.fieldx[player]) == 3:
				return "Player №"+str(player)+"won"
		if player in fieldy.keys():
			if len(self.fieldy[player]) == 3:
				return "Player №"+str(player)+"won"
		if player in fieldz.keys():   
			if len(self.fieldz[player]) == 3:
				return "Player №"+str(player)+"won" 

    def isGameOver(self):
    	len(self.cells.keys()) == self.rowCount * self.ColumnCount:
    		return True

