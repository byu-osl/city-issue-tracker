import service
import serviceattr
import keyword
import keywordservicemapper
import serviceattrval
import servicerequest
import agency
import user
import subscriptions
import citmodel
import note

CITModel = citmodel.CITModel

Service = service.Service
ServiceAttribute = serviceattr.ServiceAttribute
ServiceAttributeValue = serviceattrval.ServiceAttributeValue
ServiceRequest = servicerequest.ServiceRequest
Agency = agency.Agency
User = user.User
Note = note.Note

Keyword = keyword.Keyword
keywordMapping = keywordservicemapper.keywordMapping
KeywordMapping = keywordservicemapper.keywordMapping #TODO: Remove capital KeywordMapping after the views.py has changed to use lowercase
subscriptions = subscriptions.subscriptions

