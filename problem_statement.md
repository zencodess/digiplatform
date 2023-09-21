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

Tasks:
1. Create Django models for the required entities for the digital platform.
2. Fill the models with any information you think may be relevant.
3. Add required relations between the models to ensure DB-level enforcement of the constraints
mentioned in the workflow.
