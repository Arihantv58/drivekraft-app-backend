class user:
  def __init__(self,id,name, emailId,contact,totalSessions,firebase_id,firebase_name,firebase_email,firebase_password,credits,is_online,is_busy):
    self.id = id
    self.name = name
    self.emailId = emailId
    self.contact = contact
    self.totalSessions = totalSessions
    self.firebase_id=firebase_id
    self.firebase_name=firebase_name
    self.firebase_email= firebase_email
    self.firebase_password=firebase_password
    self.credits=credits
    self.is_online=is_online
    self.is_busy=is_busy
