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
| Deliverable | Description  | Responsibility | Week |
| :-----: | :-----: | :-----: | :-----: |
| Narrative | Describe the business scenario | Jakub Pazej | 3 |
| Software Lifecycle | Describe and justify the chosen software lifecycle | Jakub Pazej | 4 |
| Establish Roles| Specify the roles people will need to fill to complete this project | Group | 3 |
| Requirements | Functional Requirements, Use Case Diagram, Use Case Description, Non, Functional Requirements, Tactics to Support Quality Attributes, GUI Screenshots | Jordan, Eoin, Aleks, Jakub | 5 |
| System Architecture | Package Diagram, Justify Architectural Decisions | Marcin, Jordan | 6 |
| Analysis Sketches | Candidate Classes, Analysis Class Diagram, Collaboration Diagram, Communication Diagrams, Entity Relationship Diagram | Marcin, Jordan | 7 |
| Code | Code Implementation | Group | 4-14 |
| Design | Architectural Diagram, Class Diagram, State Chart | Marcin, Aleks | - |
| Added Value | Design Patterns, GitHub, Database | Jordan, Eoin | - |
| Critique | Overview, Design, Implementation | Jakub,Eoin | - |
| References | List of sources | Group | - |

## Quickstart Guide

1. To install the prerequisite dependencies to be able to run our project  run the command below.

	`pip install .`
2.  To run the simulation enter the following command.

	`python3 session.py`
2.  To run the frontside grapher enter the following command.

	`python3 app.py`
3. Open the generated IP address to see the frontend.

 
