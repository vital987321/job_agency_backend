

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
        [x] Application
            [x] Anonimous user
                [x] crud (has no access to applications)
            [x] User 
                [ ] has acces to it's own applications only CRuD
            [x] Staff 
                [x] CRUD or CRuD. has access to all applications
        [x] Vacancies
            [x] Anonimous & User
                [x] see only activated vacancies
                [x] cRud
                [x] does not see partner/company fields
            [x] Staff
                [x] sees activated and deactevated vacancies
                [x] CRUD
                [x] sees partner/company fields
        [x] User data
            [x] Anonimous
                [x] does not see users data
                [x] Crud 
            [x] User
                [x] sees only it's own data cRUD
                [x] consider deleting user profile
            [x] Staff 
                [x] sees all users. CRUD or cRUD
        [x] Review
            [x] Anonimous
                [x] sees all reviews. cRud
            [x] User
                [x] sees all reviews. cRud
                [x] it's own. CRUD
                [x] May have only one review
            [x] Staff
                [x] all reviews CRUD
                [x] May have only one review
        [x] Partner
            [x] Anonimous crud
            [x] User crud
            [x] Staff CRUD
        [x] Sector
            [x] Anonimous cRud
            [x] User cRud
            [x] Staff CRUD