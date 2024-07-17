from core.models.assignments import AssignmentStateEnum, GradeEnum


def test_get_assignments(client, h_principal):
    response = client.get(
        '/principal/assignments',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['state'] in [AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED]

def test_grade_assignment_draft_assignment(client, h_principal): # ERROR : fixture 'app' not found
    """
    failure case: If an assignment is in Draft state, it cannot be graded by principal
    """
    # Changing state to 'DRAFT' state as it is not in DRAFT state.
    # from core.models.assignments import Assignment, AssignmentStateEnum
    # with app.app_context():
    #     assignment = Assignment.get_by_id(5)
    #     assignment.state = AssignmentStateEnum.DRAFT
    #     db.session.commit()
    
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 5,
            'grade': 'DRAFT' #GradeEnum.A.value #
        },
        headers=h_principal
    )

    assert response.status_code == 400



def test_grade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.C


def test_regrade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.B.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.B
