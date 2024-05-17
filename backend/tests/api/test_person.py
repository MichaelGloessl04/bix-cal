def test_person(client_resources, crud_session_in_memory):
    from crud.models import Person, User

    client, resources = client_resources
    crud, session = crud_session_in_memory
    
    resources['crud'] = crud
    
    people = [
        {
            'creator_id': 1,
            'name': 'John',
            'surname': 'Doe',
        },
        {
            'creator_id': 1,
            'name': 'Jane',
            'surname': 'Doe',
        }
    ]
    
    user = {
        'username': 'admin',
        'email': 'admin@example.com',
    }

    with session() as s:
        s.add(User(**user))
        s.commit()
        for person in people:
            s.add(Person(**person))
        s.commit()

    response = client.get('/person/')
    assert response.status_code == 200
    assert response.json() == people
