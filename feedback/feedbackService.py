from flask import request,jsonify
import feedback.feedbackDao as feedback
def updateFeedback():
    sessionId = request.form.get('session_requests_id')
    feedback = request.form.get('feedback')
    rating = request.form.get('rating')

    feedback.addFeedback(sessionId,feedback,rating)
    return jsonify({
        "status": "success"
    })