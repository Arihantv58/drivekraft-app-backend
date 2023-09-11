class sessionRequest:
  def __init__(self,id,listener_id,is_cancelled,customer_id,status, expiry_at,updated_at,created_at):
    self.id = id
    self.listener_id=listener_id
    self.is_cancelled=is_cancelled
    self.customer_id = customer_id
    self.status = status
    self.expiry_at=str(expiry_at)
    self.updated_at = str(updated_at)
    self.created_at = str(created_at)