# KiSSaaS

This is the repository for Kindness In Simple Sentences As A Service (KiSSaaS). It is intended to be a proving ground for my skills as a DevOps Engineer. The scope of this project is to create a full deployment of an arbitrary web service, complete with: Web service (flask app), database (Postgres via SQLAlchemy), CI (in GitHub Actions), IaC deployments (via Terraform targeting AWS), scalability testing (via Apache Bench), monitoring (via OpenTelemetry).

## Goals

KiSSaaS is an app aimed at delivering kind and/or inspirational messages to users on demand and at scale. Operationally, it will be somewhat of a clone of sites like Digg or Reddit, albeit with a far more limited scope.

## Requirements

- Website
  - The Service shall provide a user with a message upon request.
    - A user my request a message at random by clicking on the "Inspire Me" button.
    - A user may vote up or down a message.
    - "Most Inspiring" View
      - A user may look at the most upvoted messages by clicking on "most inspiring" from anywhere on the site.
      - will show the most popular messages in decending order.
      - filters available to display messages in the last:
        - 24 hours
        - 7 days
        - 30 days
        - 1 year

  - User Accounts
    - All users may view all messages on the site, but only registered users may vote, comment, or submit new messages.
    - Users can register an account by clicking on "register" in the header of any page if they are not logged in.
      - To register, users must provide an email address, unique username, and a password
        - email addresses must be valid and unique
        - usernames must be unique and not contain spaces or other URI confusing characters.
        - passwords must meet some minimum safety spec (TBD)
        - nfr: passwords should be stored solely in encrypted form (SHA256 w/salt or whatever the current best practice is.)
  
