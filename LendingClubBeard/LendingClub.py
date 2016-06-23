import requests
from Account import Account

class LendingClub:
  baseURL = 'https://api.lendingclub.com/api/investor/v1/'
  apis = {
    'Loan Listing': 'loans/listing'
  }
  lastRequest = None
  response = None
  status = None
  def __init__(self, authorization):
    self.headers = {
      'Authorization': authorization,
      'Accept': 'application/json',
      'Content-type': 'application/json'
    }
  def makeRequest(self, url):
    self.lastRequest = url
    response = requests.get(self.baseURL + url, headers=self.headers)
    self.status = response.status_code
    if response.status_code == requests.codes.ok:
      return response
    else:
      response.raise_for_status()
  def getLoanListing(self):
    r = self.makeRequest(self.apis['Loan Listing'])
    if self.status == 200:
      print r.json()
  def getAccount(self, accountId):
    return Account(self, accountId)