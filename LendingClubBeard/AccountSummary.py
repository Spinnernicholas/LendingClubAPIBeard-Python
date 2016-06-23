class AccountSummary:
  investorId = None
  availableCash = None
  accruedInterest = None
  outstandingPrincipal = None
  accountTotal = None
  totalNotes = None
  totalPortfolios = None
  infundingBalance = None
  receivedInterest = None
  receivedPrincipal = None
  receivedLateFees = None
  def __init__(self, account):
    self.account = account
  def load(self, data):
    self.investorId = data['investorId']
    self.availableCash = data['availableCash']
    self.accruedInterest = data['accruedInterest']
    self.outstandingPrincipal = data['outstandingPrincipal']
    self.accountTotal = data['accountTotal']
    self.totalNotes = data['totalNotes']
    self.totalPortfolios = data['totalPortfolios']
    self.infundingBalance = data['infundingBalance']
    self.receivedInterest = data['receivedInterest']
    self.receivedPrincipal = data['receivedPrincipal']
    #[Nullable]
    if 'receivedLateFees' in data:
      self.receivedLateFees = data['receivedLateFees']
  def update(self):
    self.load(self.account.getSummaryRaw())