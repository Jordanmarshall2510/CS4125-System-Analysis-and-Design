![](https://gamma1.ul.ie/LabStats/Images/Image-UniversityOfLimerick.png)

# Smart City

**Table of Contents**
- [Smart City](#smart-city)
  * [Narrative](#narrative)
  * [Project Roles](#project-roles)
  * [Project Plan](#project-plan)
  * [Quickstart Guide](#quickstart-guide)

## Narrative
Smart City is a project that our team envisioned to simulate a futuristic smart city, a city in the near future where the majority of modes of transportation are electric and humanity is sourcing most of its power from renewable resources.

The goal of our project is to allow the user to change the amounts of renewables that generate electricity (i.e. Solar, Wind) and the amounts of things that spend it (i.e. houses, cars, public infrastructure etc.). This will allow the user to see what amount of renewables they would need to support a city of different sizes, or see how many electricity spenders they could support with different numbers of electricity generators.

The user will be able to change multiple conditions for the simulation, that would include conditions like weather, time, season, average energy spent by one family home and more.
This will allow the user to play around with the simulation and see how that impacts the simulated city.

## Project Roles
| Role | Description  | Designated Team Member |
| :-----: | :-----: | :-----: |
| Project Manager | Sets up meetings, creates project plan, tracks progress | Jordan Marshall |
| Documentation Manager | Responsible for sourcing relevant supporting documentation from each member and composing it in the report | Jakub Pazej |
| Business Analyst / Requirements Engineer | Responsible for requirements | Eoin McDonough |
| Architect | Defines system architecture | Marcin Sek |
| Systems Analyst | Creates conceptual class model | Jakub Pazej |
| Designer | Responsible for recovering design time blueprints | Eoin McDonough |
| Technical Lead | Leads implementation effort | Marcin Sek |
| Programmers |  | Everyone |
| Tester | Coding automated tests | Jordan Marshall |
| Dev Ops | Responsible for development infrastructure | Aleksandr Jakusevs |

## Project Plan
| Deliverable | Description  | Responsibility |
| :-----: | :-----: | :-----: |
| Narrative | Describe the business scenario | Jakub Pazej |
| Software Lifecycle | Describe and justify the chosen software lifecycle | Jakub Pazej |
| Establish Roles| Specify the roles people will need to fill to complete this project | Group |
| Requirements | Functional Requirements, Use Case Diagram, Use Case Description, Non, Functional Requirements, Tactics to Support Quality Attributes, GUI Screenshots | Jordan, Eoin, Aleks, Jakub |
| System Architecture | Package Diagram, Justify Architectural Decisions | Marcin, Jordan |
| Analysis Sketches | Candidate Classes, Analysis Class Diagram, Collaboration Diagram, Communication Diagrams, Entity Relationship Diagram | Marcin, Jordan |
| Code | Code Implementation | Group |
| Design | Architectural Diagram, Class Diagram, State Chart | Marcin, Aleks |
| Added Value | Design Patterns, GitHub, Database | Jordan, Eoin |
| Critique | Overview, Design, Implementation | Jakub,Eoin |
| References | List of sources | Group |

## Coding Standard
Our codebase follows the PEP-8 coding convention for Python. More can be learned via the PEP-8 section in References.

## References
### Python
| Description | Link |
| :-----: | :-----: |
| Official Page | https://www.python.org/ |
| API Reference Manual | https://docs.python.org/3/c-api/index.html |
| PEP 8 - Style Guide | https://www.python.org/dev/peps/pep-0008/ |
| Dash | https://dash.plotly.com/introduction |

### SQLite Database
| Description | Link |
| :-----: | :-----: |
| Official Page | https://sqlite.org/index.html |
| Quickstart | https://sqlite.org/quickstart.html |
| Tutorial / Reference Sheet | https://www.tutorialspoint.com/sqlite/index.htm |

### MYSQL Database
| Description | Link |
| :-----: | :-----: |
| Official Page | https://dev.mysql.com/ |
| Quickstart | https://dev.mysql.com/doc/mysql-getting-started/en/ |
| Tutorial / Reference Sheet | https://www.tutorialspoint.com/mysql/index.htm |

## Guides
### Quickstart

1. To install the prerequisite dependencies to be able to run our project  run the command below.

	`pip install .`
2. To run the simulation enter the following command.

	`python3 session.py`
3. To run the frontside grapher enter the following command.

	`python3 app.py`
4. Open the generated IP address to see the frontend.

### Setting up database

1. Make sure mysql is installed and running on your system (Use MYSQL references for support)

2. Open mysql

3. Run quickstart.sql or do the steps below

4. Create a database for the simulation using the following query

	`CREATE DATBASE [suggested name: smart_city];`
5. Create a user for the simulation with privileges to the database created using the following queries

	`
		CREATE USER [Name] IDENTIFIED BY [Password];
		GRANT ALL PRIVILEGES ON smart_city.* TO [NAME];
		FLUSH PRIVILEGES;
	`
6. Create user and generators tables using the following queries

	`
		CREATE TABLE users (
			id INT NOT NULL AUTO_INCREMENT,
			user_type varchar(16) NOT NULL,
			power_used INTEGER not NULL,
			time TIMESTAMP,
			PRIMARY KEY(id)
		);

		CREATE TABLE generators (
			id INT NOT NULL AUTO_INCREMENT,
			generator_type varchar(16) NOT NULL,
			power_generated INTEGER not NULL,
			time TIMESTAMP,
			PRIMARY KEY(id)
		);
	`

### Running simulation remotely

1. Setup database using guide above

2. Install the prerequisite dependencies to be able to run our project run

	`pip install .`
3. To run the simulation use this command

	`python3 session.py`