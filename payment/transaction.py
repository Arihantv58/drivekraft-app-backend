


class transaction:
  def __init__(self,id,transaction_id, user_id,psychologist_id,session_request_id,seconds_chatted,amount_deducted,created_at,updated_at):
    self.id = id
    self.transaction_id = transaction_id
    self.user_id = user_id
    self.psychologist_id = psychologist_id
    self.session_request_id = session_request_id
    self.seconds_chatted = seconds_chatted
    self.amount_deducted = amount_deducted
    self.created_at = created_at
    self.updated_at = updated_at

