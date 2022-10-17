# Galaxy Express

This is the galaxy-express service. This is a template service meant to be used as a take home exercise when interviewing contractors.

# Instructions

Write an app using python meeting the requirements laid out below. You may use whatever other open source libraries you see fit to get the job done. 
Before getting started on the challenge, let’s get some logistics out of the way: 
You should create a private fork of this repository on Github and add your interviewer(s) to your repository.
Remember to commit often and use descriptive commit messages ([see #5 - Imperative Mood](https://cbea.ms/git-commit/)).
When you are complete with the challenge, request a review on the pull request from your interviewer(s).

# The Problem

The year is 2142 and humans have begun colonizing the Moon, Mars, and a few brave people even moved to Venus. Due to political disputes, interplanetary package delivery was often difficult, expensive, and often lost. 

Seeing an opportunity, Zap decided to start a package delivery service called Galaxy Express. Despite some initial success, customers soon started complaining about missing or receiving duplicate packages. 

Suspecting a technical issue Zap hired you to rewrite the company’s delivery software, which was originally written by the delivery boy.

# Requirements

You will implement three HTTP endpoints to fulfill the needs of our delivery system:

## Send Package

We need an endpoint to send a package. This endpoint should accept the following data:

* Timestamp - The time at which the deliver was initiated.
* Sender ID - An ID of the individual sending the package.
* Recipient ID - An ID of the individual that the package is being sent to.
* Package ID - An ID of the package being delivered.
* Package Type - A string indicating the type of package being delivered. This will be `marketing` or `personal`.

## Update Preferences

Some individuals wish to opt-out of types of packages. We need an endpoint that will allow an individual to update their preferences. This endpoint should accept the following data:

* Timestamp - The time at which the preferences were updated.
* Recipient ID - An ID of the individual that the preferences are being updated for.
* Personal Preference - A boolean indicating whether or not the individual wants to receive personal deliveries.
* Marketing Preference - A boolean indicating whether or not the individual wants to receive marketing deliveries.

If a user is sent a package that they do not want to receive then it should be dropped.

## Get Statistics

Zap likes to keep an eye on some metrics for the business. We need an that will return the following information:

* Packages Delivered - The total number of packages delivered.
* Packages Dropped - The total number of packages dropped.

## Business Rules

* Due to difficulty of interstellar communication, requests may be malformed or invalid. These requests should be dropped.
* Due to difficulty sending packages, a sender may try resending the same
package multiple times. A send request is uniquely identified by package_id
that is constant between retries. The recipient should receive the package at
most one time despite multiple attempts.
* A recipient who has declined to receive a package type should not get that
package. By default, recipients can receive every package type.

## Other Requirements

* Tests - please write tests as you see fit
* Extensible in case we want to deliver different package types

# Other Notes

Anything not specifically outlined above is free for you to implement however you want. There is not a single correct answer, but your interviewer will be looking for you to have formed consistent opinions about your project that you can justify. Some things to consider:

* How should I design my APIs?
* How should I structure my code? (feel free to add or move as many files as you want!)
* How can I cleanly test my code?

Please do not worry about any sort of account creation, authentication or authorization controls on the endpoints. That is out of scope for the project.

# Development

## Up and Running

The service has a docker compose file to make development easier. First, make sure you have docker installed and then run the service by running:
```console
docker compose up
```

Endpoints may then be interacted with by hitting port 9090 on your local machine:
```console
curl localhost:9090/health
```

This sevice is implemented using [baseplate.py](https://baseplate.readthedocs.io/en/stable/). Please refer to the docs for any baseplate.py specific questions.

## Database

SQLAlchemy is used to interact with a SQLite database. There are some convenience functions for working with the database:

* `make migratedb` - Migrate the DB to match the current models.
* `make dropdb` - Drop the DB.
* `make resetdb` - Drop the DB and then migrate it.

Don't worry about improving the database choice or migration setup as part of your work. This is left simple to reduce scope of the project.

## Tests and Debugging

Tests may be run with `make test`.

An interactive baseplate shell can be obtained with `make shell`.

## Code Structure

* `configs` - This is where the configuration file for the service lives.
* `galaxy_express` - This is the actual implementation of the service.
    * `__init__.py` - This is where we find the entry point to our service: `make_wsgi_app()`. The implementation for the service also lives here: `GalaxyExpressService`. The service contains two endpoints:
        * `is_healthy` - This is a simple health check endpoint that always returns true. It may be used as an example of how to wire up your endpoints.
        * `example` - This is purely just an example and shows how to query the database using the SQLAlchemy client. Feel free to delete this.
    * `models.py` - This file contains an example model and some helper functions for setting up the database. Feel free to delete the example model and restructure the file however you'd like.
* `tests` - This is where the tests for the service will live. There's only one example test in there, but feel free to delete it and structure things however you would like. Tests are currently invoked using pytest.

Feel free to restructure the app however you see appropriate and bring in any libraries that make sense.

# Interviewer Instructions

Download this repository as a ZIP file and send it over to the candidate. Review the pull request on their private repo when you are added.
