# vivpro_assignment
1. Clone Project
2. Move to project directory run:
  pip install -e .
  This will install dependencies
3. alembic -c development.ini revision --autogenerate -m "init"  - Revision
4. alembic -c development.ini upgrade head - Upgrade to that revision
5.Initialize Database: This will flatten the json to required format 
  initialize_vivpro_assignment_db development.ini
6. pserve development.ini --reload
7. API examples
  i. To get playlist
    GET: http://localhost:6543/get-playlist
    - used template to display response
  ii. To get details of required song based on title
    GET: http://localhost:6543/get-playlist/{title}
    to display selected record
  iii. Update star rating 
    PUT: http://localhost:6543/add-rating
    {
    "title": "Again",
    "star_rating": 5
    }
  
