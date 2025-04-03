def test_index(client):
    """Test the index page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200

def test_submit_feedback(client):
    """Test submitting feedback."""
    response = client.post('/submit', data={
        'customer': 'sk',
        'project': 'rate-it-out',
        'rating': '5',
        'comments': 'u can do better!'
    })
    assert b'Thank You!' in response.data  # Assuming success.html has the string "Thank You!"

