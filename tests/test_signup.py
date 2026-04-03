def test_signup_success(client):
    """Test successful student signup"""
    # Arrange
    email = "newstudent@mergington.edu"
    activity = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "Signed up" in data["message"]
    assert email in data["message"]

    # Verify participant was added
    response = client.get("/activities")
    activities = response.json()
    assert email in activities[activity]["participants"]


def test_signup_duplicate(client):
    """Test signup fails when student already signed up"""
    # Arrange
    email = "dup@mergington.edu"
    activity = "Chess Club"

    # First signup (succeeds)
    client.post(f"/activities/{activity}/signup?email={email}")

    # Act - attempt duplicate signup
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "already signed up" in data["detail"]


def test_signup_activity_not_found(client):
    """Test signup fails for non-existent activity"""
    # Arrange
    email = "test@mergington.edu"
    activity = "NonExistent Activity"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "Activity not found" in data["detail"]