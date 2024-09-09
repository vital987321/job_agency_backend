

BACKEND:
    [ ] Vacancies Environment
        [x] Expand Vacancy Filter for Staff
        [x] For Vacancy model add Add active and inactive status.
        [x] Vacancy component does not show deactivated vacancy (single vacancy) in admin area.
            probably similar isue for user area. Check VacancyListDjangoFilterBackend
    [ ] permitions to admin environment
    [x] Admin can see only his own applications. Fix it.
    [x] Add Review model to backend.
        [ ] Permissions to Review
    [ ] Permissions
        [ ] Only Stuff to admin flow pages
        [ ] Application
            [ ] Anonimous user
                [ ] crud (has no access to applications)
            [ ] User 
                [ ] has acces to it's own applications only CRuD
            [ ] Staff 
                [ ] CRUD or CRuD. has access to all applications
        [ ] Vacancies
            [ ] Anonimous & User
                [ ] see only activated vacancies
                [ ] cRud
                [ ] does not see partner/company fields
            [ ] Staff
                [ ] sees activated and deactevated vacancies
                [ ] CRUD
                [ ] sees partner/company fields
        [ ] User data
            [ ] Anonimous
                [ ] does not see users data
                [ ] Crud 
            [ ] User
                [ ] sees only it's own data cRUD
                [ ] consider deleting user profile
            [ ] Staff 
                [ ] sees all users. CRUD or cRUD
        [ ] Review
            [ ] Anonimous
                [ ] sees all reviews. cRud
            [ ] User
                [ ] sees all reviews. cRud
                [ ] it's own. CRUD
                [ ] May have only one review
            [ ] Staff
                [ ] all reviews cRuD
                [ ] it's own CRUD
                [ ] May have only one review
        [ ] Partner
            [ ] Anonimous crud
            [ ] User crud
            [ ] Staff CRUD
        [ ] Sector
            [ ] Anonimous cRud
            [ ] User cRud
            [ ] Staff CRUD