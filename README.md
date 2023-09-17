# HackMIT project 2023

## Introduction
Repo for HackMIT 2023 project.

<img src="https://github.com/erikbohne/hackmit-23/assets/40596752/1fba3028-caf9-4d61-854d-8c58b23e2a39" width="30%">


## Inspiration

In the evolving world of AI technology, we recognized an opportunity to enhance everyday experiences. One area that felt close to home was our post-workout interactions with GPS watches. The monotony of recurring, templated comments was evident. We envisioned an AI-driven platform that echoed the nuance of a personal trainer's feedback, making every workout feel even more personalized and rewarding.
What it does

There are two main options after you log in. Either upload your .gpx file manually through the upload button, or sync it with your Strava account and Rhythm will generate the comments for your most recent workouts.
How we built it

For the frontend we used React and material UI to create a user-friendly and appealing interface for our product. Firebase serves as the auth provider and Firestore as the database. On the main page all the comments displayed are fetched from the users collection of comments in firestore.

The backend is written in python with the Flask library. We created an endpoint to take a .gpx file and process the data, get a comment, and add it to the database. This ties together several API's and produces our end product, workout specific feedback and comments.


## Challenges we ran into

  Promt-engineering our GPT model to output in a style and format that satisfies how we want it to be.
  Figuring out how to seamlessly integrate Terra API to our pipeline in order to get better results

## Accomplishments that we're proud of

Beyond building a holistic product, we've crafted a versatile tool with potential integrations across an array of sports diary providers – from industry giants like Apple, Garmin, and Polar to niche platforms. The feedback generated can be a valuable addition to any fitness platform, making workouts more insightful and engaging.


## What's next for Rhythm

  More data. We want to train our model on more data to improve the quality of the comments.
  More integrations. We want to integrate with more fitness platforms to make our product more accessible.
  More features. We want to add more features to our product to make it more useful for our users.
  More users. We want to get more users to use our product and get feedback from them to improve our product.




## Team
<img src="https://github.com/erikbohne/hackmit-23/assets/40596752/5811ed24-21ef-4df6-a57f-a50b4b7f6361" width="70%">
