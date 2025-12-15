from app.feedback import save_feedback, load_feedbacks

def test_save_feedback():
    save_feedback("Boa", "Teste automático")
    feedbacks = load_feedbacks()
    assert len(feedbacks) > 0
