class sessionRequest:
  def __init__(self,id,listener_id,customer_id, expiry_at,updated_at,created_at):
    self.id = id
    self.listener_id=listener_id
    self.customer_id = customer_id
    self.expiry_at=expiry_at
    self.updated_at = updated_at
    self.created_at = created_at
