def test_status_code_200(client):
    """Test that the client returns a 200 status code."""
    resp = client.get("/")
    assert resp.status_code == 200
