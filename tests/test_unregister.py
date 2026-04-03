def test_unregister_success(client):
    """Test successful student unregistration"""
    # Arrange
    email = "remove@mergington.edu"
    activity = "Chess Club"

    # First signup the student
    client.post(f"/activities/{activity}/signup?email={email}")

    # Act - unregister
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "Unregistered" in data["message"]
    assert email in data["message"]

    # Verify participant was removed
    response = client.get("/activities")
    activities = response.json()
    assert email not in activities[activity]["participants"]


def test_unregister_not_signed_up(client):
    """Test unregister fails when student not signed up"""
    # Arrange
    email = "notsigned@mergington.edu"
    activity = "Chess Club"

    # Act - attempt to unregister without being signed up
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "not signed up" in data["detail"]


def test_unregister_activity_not_found(client):
    """Test unregister fails for non-existent activity"""
    # Arrange
    email = "test@mergington.edu"
    activity = "NonExistent Activity"

    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "Activity not found" in data["detail"]