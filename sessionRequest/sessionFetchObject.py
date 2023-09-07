class sessionFetchObject:
  def __init__(self,id,listener_id,customer_id,expiry_at,status,customer_firebase_id,username,is_cancelled,updated_at,created_at):
    self.id = id
    self.listener_id=listener_id
    self.is_cancelled=is_cancelled
    self.customer_id = customer_id
    self.status = status
    self.customer_firebase_id = customer_firebase_id
    self.username = username
    self.expiry_at=str(expiry_at)
    self.updated_at = str(updated_at)
    self.created_at = str(created_at)

