


class paymentOrder:
  def __init__(self,id,order_id, payment_id,signature,amount,userId,paymentGateway,created_at,updated_at):
    self.id = id
    self.order_id = order_id
    self.payment_id = payment_id
    self.signature = signature
    self.amount = amount
    self.userId = userId
    self.paymentGateway = paymentGateway
    self.created_at = created_at
    self.updated_at = updated_at

