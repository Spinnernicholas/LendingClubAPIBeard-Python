from AccountSummary import AccountSummary
from OwnedNote import OwnedNote

class Account:
  baseURL = 'accounts/{accountId}/'
  apis = {
    'Summary': 'summary',
    'Available Cash': 'availablecash',
    'Transfer Funds': 'funds/add',
    'Pending Transfers': 'funds/pending',
    'Cancel Transfers': 'funds/cancel',
    'Notes Owned': 'notes',
    'Detailed Notes Owned': 'detailednotes',
    'Portfolios': 'portfolios',
    'Submit Order': 'orders'
  }
  def __init__(self, lendingClub, accountId):
    self.api = lendingClub
    self.accountId = accountId
  def makeRequest(self, url):
    return self.api.makeRequest(self.baseURL.format(accountId=self.accountId) + url)
  def getSummaryRaw(self):
    r = self.makeRequest(self.apis['Summary'])
    return r.json()
  def getSummary(self):
    summary = AccountSummary(self)
    summary.load(self.getSummaryRaw())
    return summary
  def getAvailableCashRaw(self):
    r = self.makeRequest(self.apis['Available Cash'])
    return r.json()
  def getAvailableCash(self):
    return self.getAvailableCashRaw()['availableCash']
  def getPendingTransfersRaw(self):
    r = self.makeRequest(self.apis['Pending Transfers'])
    return r.json()
#  def getPendingTransfers(self):
  def getOwnedNotesRaw(self):
    r = self.makeRequest(self.apis['Notes Owned'])
    return r.json()['myNotes']
  def getOwnedNotes(self):
    notes = []
    for rawNote in self.getOwnedNotesRaw():
      note = OwnedNote(self)
      note.loadSimple(rawNote)
      notes.append(note)
    return notes
  def getDetailedOwnedNotesRaw(self):
    r = self.makeRequest(self.apis['Detailed Notes Owned'])
    return r.json()['myNotes']
  def getDetailedOwnedNotes(self):
    notes = []
    for rawNote in self.getDetailedOwnedNotesRaw():
      note = OwnedNote(self)
      note.loadDetailed(rawNote)
      notes.append(note)
    return notes
  def getPortfoliosRaw(self):
    r = self.makeRequest(self.apis['Portfolios'])
    return r.json()
#  def getPortfolios(self):