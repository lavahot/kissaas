# KiSSaaS

This is the repository for Kindness In Simple Sentences As A Service (KiSSaaS). It is intended to be a proving ground for my skills as a DevOps Engineer. The scope of this project is to create a full deployment of an arbitrary web service, complete with: Web service (flask app), database (Postgres via SQLAlchemy), CI/CD (in GitHub Actions), IaC deployments (via Terraform targeting AWS), scalability testing (via Apache Bench), monitoring (via OpenTelemetry). System design will explore as many modern web paradigms as is reasonable. 

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
      - After registering successfully, the system will send the user a message to confirm their email address, containing a link to confirm validity. This link will be good for 24 hours.
        - nfr: The system will keep track of open validations in a token system. It will cull tokens that expire after the 24 hour TTL.
    - Users can upvote or downvote a message up to three times. That is, their "vote" for a given message can be in the range -3:3 inclusive. (A La Uservoice)
    - Users by default will have their message post and comment activity featured on a publically viewable view.

  - Moderation
    - Some users may be moderators, which grant them certain abilities
      - moderators can delete messages (should they be trolling, botting, or otherwise offensive)
      - moderators can delete comments (should they be trolling, botting, or otherwise offensive)
      - moderators can temporarily ban particular users from posting/commenting for an infraction. 
        - Mod bans last at most 24 hours.
    - Users may report messages for unruly behavior and moderators will recieve these reports and prompted to take action.
  
  - Admins
    - People who are accountable have Spider-Man-level abilities:
      - the ability to create/delete/update user accounts.
      - permanently ban users

  - Messages
    - Messages can be created by registered users by clicking the "submit kindness" button in the header of every page.
    - They consist of text fields of max 255 characters long.
    - They can be moderated or deleted.

## Things to worry about (in no particular order)
- 🤖 Robots
- 💗 Scaling issues
- 🔒 Security issues (vulnerabilities in design and dependencies) 
- 💸 Funding the actual running of the site
- 👹 Trolls
- 🤡 Gaming of the system
- 📝 Other people's data (GDPR, COPPA, etc. )
- 📑 Legal mumbo jumbo (Terms of service, Privacy policy)
