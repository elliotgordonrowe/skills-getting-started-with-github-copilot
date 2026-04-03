def test_get_activities(client):
    """Test retrieving all activities"""
    # Arrange - fixtures handle setup

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

    # Check structure of one activity
    activity = data["Chess Club"]
    assert "description" in activity
    assert "schedule" in activity
    assert "max_participants" in activity
    assert "participants" in activity
    assert isinstance(activity["participants"], list)


def test_root_redirect(client):
    """Test root endpoint redirects to static index"""
    # Arrange - fixtures handle setup

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200  # TestClient follows redirects
    # Verify it serves the HTML content
    assert "Mergington High School" in response.text
    assert "<!DOCTYPE html>" in response.text