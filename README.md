# digiplatform
A digital platform (CRM model) to offer and manage JePPIX services  

## Intro
Our Digital Platform provides customers access to services of several companies (service
providers). On the platform, there are also account managers (users with a specific role), each of them
manages her own set of service providers. A service provider may be managed by several account
managers.

## Workflow
When a new customer comes for JePPIX services, the workflow is organized in the following
way:
- An account manager registers the new user account for this customer.
- The customer creates an order. The complete order is visible to the account manager.
- The customer fills the order with services from the service providers. However, there’s a
limitation: she can add services only from those service providers which are managed by her
account manager.
- Later, the same customer may create more orders.
- Later, another account manager may also work with the same customer, and this account
manager must not see the previous orders of this customer which were managed by the first
account manager.
Note: confidentiality of orders and customer relations is extremely important!

## Models

#### Account Manager
#### Service Provider
#### Service
#### Customer
#### Ordering

## Detailing 


![Digital platform's service manager app - Entities and Relations](entity_relation_diagram.png)
## Steps to run from any computer

1. Clone the repo
3. Create a virtual environment and install requirements
4. In the project directory, use 
```
py manage.py runserver
```
4. Create your own superuser
'''
py manage.py createsuperuser
'''
Navigate to
```
localhost:8000/ and
localhost:8000/admin // using super user credentials
localhost:8000/servicemanager 
```




