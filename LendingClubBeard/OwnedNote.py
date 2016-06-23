class OwnedNote:
  detailed = False
  #Simple Fields
  loanStatus = None
  loanId = None
  noteId = None
  grade = None
  loanAmount = None
  noteAmount = None
  interestRate = None
  orderId = None
  loanLength = None
  issueDate = None
  orderDate = None
  loanStatusDate = None
  paymentsReceived = None
  #Detailed Fields
  portfolioName = None
  accruedInterest = None
  purpose = None
  portfolioId = None
  orderId = None
  creditTrend = None
  currentPaymentStatus = None
  canBeTraded = None
  paymentsReceived = None
  nextPaymentDate = None
  principalPending = None
  interestPending = None
  interestReceived = None
  principalReceived = None
  applicationType = None
  def __init__(self, account):
    self.account = account
  def isDetailed(self):
    return self.detailed
  def loadSimple(self, data):
    self.datailed = False
    self.loanStatus = data['loanStatus']
    self.loanId = data['loanId']
    self.noteId = data['noteId']
    self.grade = data['grade']
    self.loanAmount = data['loanAmount']
    self.noteAmount = data['noteAmount']
    self.interestRate = data['interestRate']
    self.orderId = data['orderId']
    self.loanLength = data['loanLength']
    #[Nullable]
    if 'issueDate' in data:
      self.issueDate = data['issueDate']
    self.orderDate = data['orderDate']
    #[Nullable]
    if 'loanStatusDate' in data:
      self.loanStatusDate = data['loanStatusDate']
    self.paymentsReceived = data['paymentsReceived']
  def loadDetailed(self, data):
    self.loadSimple(data)
    detailed = True
    #[Nullable]
    if 'portfolioName' in data:
      self.portfolioName = data['portfolioName']
    self.accruedInterest = data['accruedInterest']
    self.purpose = data['purpose']
    #[Nullable]
    if 'portfolioId' in data:
      self.portfolioId = data['portfolioId']
    self.orderId = data['orderId']
    self.creditTrend = data['creditTrend']
    #[Nullable]
    if 'currentPaymentStatus' in data:
      self.currentPaymentStatus = data['currentPaymentStatus']
    self.canBeTraded = data['canBeTraded']
    #[Nullable]
    if 'nextPaymentDate' in data:
      self.nextPaymentDate = data['nextPaymentDate']
    self.principalPending = data['principalPending']
    self.interestPending = data['interestPending']
    self.interestReceived = data['interestReceived']
    self.principalReceived = data['principalReceived']
    #[Nullable]
    if 'applicationType' in data:
      self.applicationType = data['applicationType']