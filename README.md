# Project 2 - Insured

[The Checklistar live demo](https://jannis-kiriasis.github.io/the-checklistar/index.html)\
[The Checklistar repository](https://github.com/jannis-kiriasis/the-checklistar)

## Table of contents
-   [Introduction](#introduction)
-	[User Experience (UX)](#user-experience-ux---user-stories)
-	[Features](#features)
-	[Where user stories meet features](#where-user-stories-meet-features)
-	[Wireframes](#wireframes)
-   [Features left to implement](#features-left-to-implement)
-	[Designs](#design)
-   [Accessibility](#accessibility)
-   [SEO](#seo)
-	[Technologies and tools used](#technologies-and-tools-used)
-	[Testing](#testing)
-	[Issues fixed](#issues-fixed)
-	[Deployment](#deployment)
-	[Credits](#credits)
-   [Acknowledgements](#acknowledgements)
-   [Disclaimer](#disclaimer)

## Introduction

The Checklistar is a workflow management application designed to bring projects from A to Z.

Documents and projects more often then not, need to be reviewed and approved by a number of departments before they can 'go live'.

The larger the company and the longer this process normally takes. 

Let's say for example that we want to create a new advertising campaign about our brand new product. The marketing team will come up with the campaign but what about the other teams?

The product team probably needs to review the campaign to confirm that the feature advertised are correct.

The legal and compliance departments need to ensure that the campaign adhere to internal and external regulations.

The campaign may also need the review of an executive.

And obviously everyone has comments and edits.

The Checklistar takes away the pain of following up with every team, dig into email threads and record evidence of approvals (yes there is also the risk management team).

Does it sound familiar to you?

You are not alone.

A quick search with Google Keywords Planner can reveal how many monthly search there are to 'workflow management system' and related queries.

![queries about workflow management system](.media/README-files/workflow-management-system-keywords.png)

This is what you can do with The Checklistar:
1. Start a project, set and follow the stages it needs to go through.
2. Set the 'approvers', the people or the teams in your organization who need to review the project or document.
3. Receive a feedback from the approvers in form of comments, to keep the messages around one project / document in the same place.

### Who is The Checklistar for?
The checklistar is for those companies that need a desktop app to track progresses on multiple cross team projects or documents approval.

### What The Checklistar offer:
- A simple form to setup a project and approvers who need to review it.
- A unified view to see all the projects open.
- A view to see all the projects the logged in user have started.
- A view to see all the projects the logged in user need to approve.
- A form to leave comments under each project.
- The possibility to edit and delete projects.

![Insured responsive design](./media/README-files/i-am-responsive.png)
## User Experience (UX) – The needs
Now that we are familiar with The Checklistar target audience and offering, we are looking at the needs the app users may have. 

Having worked in corporate environments for different years, I was exposed to this type of processes where a project or document needed to be reviewed by different departments before it could be realised to the public. 

The first step I took was to listen to the needs of all the players involved in the process. I have identified 3 main stakeholders:
### The project manager (PM)
The project owner is the person who owns the project and is responsible to bring it to a conclusion. 

The project owner has different requirements since the beginning depending on the type of project that needs to be completed. 

To summaries, a project or document that needs to ‘go through the checklist’ (from here the name The Checklistar) always has:

- A title
- A description
- An attachment
- A due date
- The departments that need to approve it
- An aimed approval due date for each department to make sure the process doesn’t stop somewhere

Not every project goes smoothly through the checklist every time. The PM faces different struggles:

1. Some approvers forget to follow up and return the project approved on time. They are always busy, they (we) always get thousands of emails every day and the email with the project approval request gets forgotten under a pile of other urgent emails. The PM needs to remind the approvers constantly.

3. Some approvers come back with suggestions or changes requests. The project / document needs to be reviewed. The approver and the project owner start to exchange many emails back and forth. Someone else may be called in to approve the project too.

4. The PM also needs to collect evidence of every approval. All the approvals are recorded in case of an audit from third parties. The risk controllers regularly test a few projects to make sure that the company is limiting the risks as much as possible. The PM problem is that those approvals aren’t saved in a database, but in their mailbox. So they needs to go and find all the emails threads (from point 2) and keep a record of all the approval received. 

5. Deadlines are missed because of point 1,2,3. The project owner is considered the responsible because it’s ‘the owner’.

### The project approver (PA)
The project approver is the person that needs to review and approve a project. Every project may have more than one approver. Usually, the approvals need to be given in a specific order.

The PA also faces different problems:

1. The PA receives many requests of approvals per week. Some of them take longer than others to review. The PA is usually one designated person in a department. It’s difficult to keep track of all the approval requests if the only place they are found is their mailbox.
2. The PA needs to be always aware of the approval deadlines. Because it is difficult to keep up with all the incoming requests, it is imperative for the approver to be aware of all the deadlines. Some of the documents / projects are time sensitive, others may be regulatory changes. 
### The risk controller (RC)
The risk controller is someone that oversees the process from outside. The RC isn’t actively involved, however they periodically ‘test’ the process. They have to make sure that all the projects / documents completed went through the checklist rigorously and the approvals needed have been recorded.

Even if not actively involved, the RC also faces some problem:

1. While performing the tests, the RC needs to review all of the approval’s recordings. They need to examinate the evidence provided. Those evidence may be different from project to project. Every PM also collects them differently. The RC issue with this is that it’s time consuming and not immediate the answer. The RC may have to knock at the PM door to ask explanations about the evidence collected because not clear enough.
1. The RC also needs to evaluate the quality of the evidence and decide whether it is satisfactory for the risk control. This means that the RC needs to influence the way the checklist is compiled and the way the evidence is recorded. Again this process takes time as it isn’t standardised.

The first step was to outline all the problems the 3 main stakeholders have. Those problems where then translated into needs, in other words, the stakeholders ‘wants’ from the approval management system.

The app needs to be able to solve all of them. The following step I took was to transform those needs into Epics and then User stories.

At this point defining the epics was intuitive enough: I created 3 main epics, each of them addressing the issues of one of the stakeholders.
## Epics and User Stories

Following, you can find the epics an the user stories break down used to plan the development of the app.
### Epic 1 – The project manager

The PM requires a workflow to get some projects / documents approved. The PM needs to be able to submit certain information with the project/document. The PM needs to designate some approvers within the organization to review and approve the project. The PM needs to keep track of all the interactions with the PAs and collect approvals within certain deadlines. The approval evidence needs to be recorded for risk management reasons.


### E1 - User story 1 – Create a project
As a PM, I want to be able to create a project so that I don’t need to submit the project via email.

**Acceptance criteria:**
1. The project needs to include project id, title, description, attachment, due date and an unlimited number of approvers.

### E1 - User story 2 – Set the project workflow
As a project manager, I want to be able to assign unlimited approvers to a project so that I can get all the approvals needed for completion.

**Acceptance criteria:**
1. Set unlimited approvers when I’m creating the project
2. The approvers must be associated to a department and have a deadline

### E1 - User story 3 – Create main dashboard
As a project manager, I want to be able to see at what stage a process is and how many steps are missing so that I can make sure we are in line with deadlines.

**Acceptance criteria:**
1. Create a dashboard page with all the projects open and the approvals required for each project
2. The approvals must be ordered by due date
3. It should be immediate to notice what approvals have been given and what approvals are missing

### E1 - User story 4 – Edit a project
As a project manager, I want to be able to update a project anytime, so that if the requirements change, I can update the workflow.

**Acceptance criteria:**
1. Project title, description, due date approvers and approval due dates must be editable.
2. Only the project owner can edit a project.

### E1 - User story 5 – Delete a workflow
As a project manager, I want to be able to delete a project, so that if a project is cancelled, I can also delete it from the platform.

**Acceptance criteria:**
1. Include the option to cancel a project and related approvers.
2. Only the project owner can delete a project.

### E1 - User story 6 – See all the projects open
As a project manager, I want to be able to see all the projects I’ve started and their approvers, so that I can quickly see where I need to focus.

**Acceptance criteria:**
1. Create a page where the PM can see only the projects the logged-in PM has started
2. Make instantly evident what projects are completed and what aren’t
3. The projects should be ordered by created date


### E1 - User story 7 - Add a comment (Create)  
As a project manager, I can add a comment to a specific project, so that I can update other people or discuss a specific issue without sending emails.

**Acceptance criteria:**
1. Projects should be comment-able 
2. Comments should be in a thread and ordered by the newest


### E1 - User story 8 - Notify PM
As a PM, I want to be notified when a comment is added to the project, or an approval is given so that I can decide how to proceed next

**Acceptance criteria:**
1. Send me a notification when a project is approved
2. Send me a notification when a project is commented

### E1 - User story 9 - Registration and sign in project owner
As a project owner, I can register and log in to the software, so that I will be the only one able to create, edit, complete and cancel my projects.

**Acceptance criteria:**
1. Users need to be able to sign up to use the app.
2. PM must be authenticated to create, edit, cancel or complete a project.


## Epic 2 – The approvers / stages
The approvers need to be able to find of all the projects they need to approve easily. They’ll have a list of works they need to review so that nothing goes lost and they can make sure deadlines are respected. The approver needs to be able to comment and approve projects.

### E2 - User story 1 - See projects pending approval (Read) 
As an approver, I want to quickly see what projects are pending my approval so that I can concentrate and to get the work done.

**Acceptance criteria:**
1. All the approvers’ projects need to be in a page and the deadline should be visible.
2. The projects needing approval by the logged in approver need to be identified easily.

### E2 - User story 2 - See project by due date
As an approver, I want to see when all the projects pending my approval are due, so that I can prioritise my work.

**Acceptance criteria**
1. The due date will be visible in the dashboard, my approvals and my projects views for each project.
2. The My approvals view will be ordered by the due date.

### E2 - User story 3 - Approvers feedback
As an approver, I want to be able to add a comment to the project, so that I can record my feedback and don’t get lost in email threads. 

**Acceptance criteria**
1. The approver needs to be able to comment the project

### E2 - User story 4 - approve a project
As an approver, I want to be able to approve a project so that it can be sent to the next approver.

**Acceptance criteria**
1. A feature needs to allow the approver to approve the project
2. Only the approver specified by the project manager can approve a project

### E2 – user story 5 - Notify approvers
As an approver I want to be notified when a project is assigned to me so that I can take an action.

**Acceptance criteria**
1. The approver needs to receive a notification when he has been assigned a project.

### E2 – user story 6 - Registration and sign approvers
As an approver, I can register and login to the software, so that I will be the only one able to approve a project for my department.

**Acceptance criteria**
1. Users need to be able to sign up to use the app.
2. Approvers must be authenticated to approve a project.

## E3 – The risk controllers
The tool will allow risk controllers to keep track of all the work done and make sure that it has been carried out respecting regulations to lower risk levels. The tool records all the projects/ works done and the evidence should be collectable easily.

### E3 - User story 1
As a risk controller, I can download a list of the projects approved, so that I can record risk assessments and evidence.

**Acceptance criteria**
1. The RC needs to find a list of all the projects approved.
2. The completed projects need to be accessible easily.
3. Completed projects and approvals need to be downloadable


Mapping out the user stories helped me easily identify the problems the application solves:

1. There is no need to save / download approval emails as they are all stored in a database
1. The RC can find all project completed easily and download all the approvals from the database
1. There is no need to exchange emails as the projects can be commented.
1. Everything related to a project is centralised. So comments, approvals, deadlines and other project details can be found in the same place.


## Features

In the following paragraphs, we are going to see what features appear on the website and where they meet the users' needs.

### 1. Main navigation
   The main navigation includes the following pages:
   1. Create a project
   1. Dashboard – contains all the projects opened by anyone 
   1. My projects – the projects the logged in user have started
   1. My approvals – the approvals the logged in user need to give
   1. Notification centre – as list of things that happened related to the logged in user

The navigation allows users to filter the projects to easily find the projects they need to approve; they have opened and the option to create a project. 

Non logged in users can only see sign up and sign in in the navigation.

### 2. The projects
   The project includes the project details that the PM outlined. It also includes the approvers that need to approve it and their approval due dates.

The content seen is personalised for the signed in user. On the ‘My approvals’ page:

- If the logged in user have already approved the project, it will have a green background (otherwise light blue)

On the ‘my projects’ page:

- If the logged in user have already completed a project, it will have a green background (otherwise light blue)

Project collapsed

Project expanded

### 3. The project details

By clicking on view details on any project, it will open a project details page. There everyone can see more details about a project as well as its comments and the buttons to edit, approve, delete and complete. It also includes the form to submit a comment on the project.

Only the PM can see edit, delete and complete. Only the approvers can see the approve button and only their correspondent button.

Defensive design has been implemented to cancel, approve, complete and delete a project.

On page feedbacks have been implemented when a project is approved, completed, deleted or updated.

### 4. My projects
The my projects view filters the projects by projects opened from the logged in user. The projects are also divided between completed and not completed. The projects completed have a light green background whereas the projects not completed have a light blue background.

### 5. My approvals

The my approvals view filters the projects by projects that the logged in person needs to approve. The projects are also divided by approved and not approved. The projects approved have a light green background and the projects not approved have a light blue background.

### 6. Notification centre

The notification centre includes a list of notifications personalised for the logged in user. The user is notified when:

- a comment is added to a project where the user is an approver or a project owner
- a project is assigned to an approver
- a project has been approved

### 7. Create and edit a project forms

As the title says, this form allows the user to create or edit a form. Every field is editable. Approvers can be added and removed during creation or when editing a project and the records are automatically added or removed from the database.

On page feedbacks have been implemented when a project is created and updated.

### 8. Login

A form to authenticate the user to the app. Non authenticated users can see the projects but not interact with them (they can’t comment, approve, edit, open project etc. They can only ‘read’).

On page feedbacks have been implemented when a user logs in and signs up.


### 9. Signup

The signup form allows users to sign up and use the tool. At sign up they need to enter their department so that if they are selected as approvers, their department will show up in the approvers list of each project.

### 10. The admin panel

The admin panel allows a superuser to see all the records saved in the database including:

- projects
- project approvals
- users and user profiles
- Notifications
- comments

From the admin panel, projects and project approvals can be downloaded as a csv file to be handed to the RC and fulfil their requirements.

### 11. Feedbacks and popups

The applications let the user know every time they user perform an action whether is has been completed or not.

### 12. 404 and 500 error pages

The 404 and 500 error pages handle errors nicely explaining to the user what is happening and offering a way to exit the error.!

[Custom 404 page](Aspose.Words.4c96bf5c-2f8f-4cf7-bccf-572631e96517.001.png)

## Where user stories meet features

In the following table, I’m going to match features with user stories and the issues the app solves. All the user stories, features and needs outlined in the paragraphs above have a number that correspond to the number you see in the table below.

| User stories | Features |
|--------------|----------|
| E1 US1       | 7        |
| E1 US2       | 7        |
| E1 US3       | 2, 3     |
| E1 US4       | 7        |
| E1 US5       | 3        |
| E1 US6       | 4        |
| E1 US7       | 3        |
| E1 US8       | 6        |
| E2 US1       | 5        |
| E2 US2       | 5, 3     |
| E2 US3       | 3        |
| E2 US4       | 3        |
| E2 US5       | 6        |
| E3 US1       | 10       |


## Wireframes

The first draft of the website was completed by creating wireframes using Balsamic.

Below you can find the initial wireframes created. The main goal when I created 
the wireframes was to fulfill the user story requirements. Later on during development
I've upgraded the styling getting to the final version that you see live.

**Create a project**
![Create project page wireframe](./media/README-files/create-project.png)

**Dashboard**
![Dashboard wireframe](./media/README-files/dashboard.png)

**View details**
![View details wireframe](./media/README-files/view-project.png)

## Features left to implement 

- Create checklist templates. A set or predefined approvers. Every templates have different predefined approves. Improves UX.
- Implement email notification. When a notification is created, an email can also be created.
- Option to upload more than 1 document. Possibly a versioning system.
- Approvals to be give in a specific order, so disable the approver button untill the approver's turn comes.
- Signup with a social media account or Google.

## Design

In the following paragraph, I'm going to explain the colours, typography and imagery choices.

### Colours

I've used a similar color palette to a project I previosly realised (pp2) so the reasoning behind the colors choice is very similar.

The main colour used is a shade of blue (Liberty). Blue is a calm and serene colour. It is often associated with stability and reliability. I've increased a bit the contrast ratio with light backgrounds to achieve accessibility best scores.

All the main buttons are in a shade of green, Verdigris. It's different enough to differentiate from the main Liberty color. I've also used a share of red (Fuzzy Wuzzy) for the 'delete' button and the 'remove approver' button.

I've also used a tan color for the 'edit', 'complete' and 'approve'. Those aren't stardard actions (for which I've used Verdigris) and they aren't 'delete' actions so Fuzzy Wuzzy red wasn't a good chioce for those. 

Lighter shades of Verdigris and Liberty have been created to highlight complete / non completed and approved / not approved projects in the templates 'dashboard', 'my approvals', 'my projects'.


![Color Palette](./media/README-files/colors.png)

All the text colour combinations have been tested for accessibility and they all achieve WCAG AAA.
- [Colour contrast test: white on blue](https://webaim.org/resources/contrastchecker/?fcolor=FFFFFF&bcolor=3B4D97)   
- [Colour contrast test: black on light blue](https://webaim.org/resources/contrastchecker/?fcolor=000000&bcolor=E9ECF7)   
- [Colour contrast test: black on green](https://webaim.org/resources/contrastchecker/?fcolor=000000&bcolor=48A9A6) 
- [Colour contrast test: white on red](https://webaim.org/resources/contrastchecker/?fcolor=FFFFFF&bcolor=A42D2D)   
- [Colour contrast test: black on tan](https://webaim.org/resources/contrastchecker/?fcolor=000000&bcolor=D4B483)   
- [Colour contrast test: blue on light blue](https://webaim.org/resources/contrastchecker/?fcolor=E9ECF7&bcolor=3B4D97)   
- [Colour contrast test: black on tan](https://webaim.org/resources/contrastchecker/?fcolor=000000&bcolor=D4B483)   
- [Colour contrast test: dark green on white](https://webaim.org/resources/contrastchecker/?fcolor=296161&bcolor=FFFFFF)   

Tested with [Contrast checker](https://webaim.org/resources/contrastchecker/).

### Typography

The typography was chosen for my liking, again I've used it in previous projects PP2). Open Sans is a very popular font if not the most popular.

I used [Open Sans](https://fonts.google.com/specimen/Open+Sans) for all body elements.  

The fallback font used is Helvetica for all body elements.

### Imagery

The only image used in thi project is the favicon.


## Accessibility

As mentioned above, all the colour combinations used for text passed a contrast ratio test. During the testing phase, Verdigris didn't pass the test and so it was darkened creating the Dark Verdigris color achiving the WCAG AAA score for accessibility.

I've also used alt tags to describe images and aria labels to describe links.  
The pages have been structured using semantic HTML markup.  

The Lighthouse accessibility test also reports an accessibility score of 100/100. 

A Lighthouse report is available in a few paragraphs below in the testing section.

## SEO

While the most important SEO tags (meta tags and open graphs) have been used in the base.html template head, this app in for internal use, so in isn't made to be found on searh engines. 
SEO is irrevelant for this project.

## Technologies and tools used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://it.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Materialize](https://materializecss.com/)
- Version control: [Git](https://git-scm.com/)
- Public repository: [GitHub](https://github.com/)
- Google Font: [Open Sans](https://fonts.google.com/specimen/Open+Sans)
- Wireframes: [Balsamiq](https://balsamiq.com/)
- Lighthouse: [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
- Colours accessibility: [Webiam](https://webaim.org/resources/contrastchecker/)
- Uniform alert on all browsers: [SweetAlert](https://sweetalert2.github.io/)
- Colors darkener: [Color darkener](https://mdigi.tools/darken-color/)
- Color lightener: [Color lightener](https://mdigi.tools/lighten-color/)

## Testing

I've carried out the following tests:

1. [HTML validation](#html-validation)
2. [CSS validation](#css-validation)
3. [JavaScript validation](#js-validation)
9. [Automated python testing](#automanted-teting)
4. [Manual testing](#manual-testing)
5. [Browsers compatibility](#browser-compatibility)
6. [Responsiveness testing](#responsiveness-testing)
7. [Lighthouse testing](#lighthouse-testing)
8. [User stories testing](#user-stories-testing)


### HTML validation

All the pages passed the HTML validation with no errors or warnings.
- [index.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjannis-kiriasis.github.io%2Finsured%2Findex.html)  
![index.html html test](./README-files/questionnaire-html.png)
- [life-insurance-calculator.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjannis-kiriasis.github.io%2Finsured%2Flife-insurance-calculator.html)  
![life-insurance-calculator.html test](./README-files/calculator-html.png)
- [application-form.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjannis-kiriasis.github.io%2Finsured%2Fapplication-form.html)  
![application-form.html test](./README-files/application-html.png)

### CSS validation

Style.css passed the CSS validation with no errors.
- [css validation](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fjannis-kiriasis.github.io%2Finsured%2Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  
![CSS validation](./README-files/css-test.png)

There are only 2 warnings related to `-webkit-appearance: none;` and `-moz-appearance: none;` used to style the form submit button. This was used to prevent iPhone / iPad default style. The submit button would otherwise not be styled as declared in the CSS without the webkit extension.

### JS validation 
The JavaScript files have been passed through [Jshint](https://jshint.com/): I have added a few semicolumns and removed unused variables. There are no issues with the code.

There are also no errors in the Console (Google Developer Tools).

The Lighthouse best practices test also reports a score of 100/100. 

A Lighthouse report is available a few paragraphs below in the testing section.

### Automated testing



### Manual testing

I've tested that the different functionalities of the website work as intended.

| Test Label                                                              | Test Action                                                                                                                                        | Expected Outcome                                                                                                                                                                                                                   | Test Outcome |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Nav / mobile nav - Logo click                                           | Click on the logo in the navigation.                                                                                                               | It redirects to the homepage (“/”).                                                                                                                                                                                                | PASS         |
| Nav – sign up                                                           | Click on sign up in the navigation.                                                                                                                | It redirects to the sign up page “/accounts/signup/”.                                                                                                                                                                              | PASS         |
| Sign up – form validation                                               | On “/accounts/signup/” enter an incorrect form value or not enter a value (exclude the optional fields). Click sign up.                            | Sign up will fail and failing error will appear next to the field failed.                                                                                                                                                          | PASS         |
| Sign up - redirect                                                      | On “/accounts/signup/” complete the form and click on sign up.                                                                                     | You will be redirected to the homepage (“/”).                                                                                                                                                                                      | PASS         |
| Sign in - feedback                                                      | On “/accounts/signup/” complete the form and click on sign up.                                                                                     | After the redirect a green feedback message will appear on the bottom left.                                                                                                                                                        | PASS         |
| Nav / mobile nav - login                                                | Click on log in in the navigation.                                                                                                                 | It redirects to the login page “/accounts/login/”.                                                                                                                                                                                 | PASS         |
| Sign in – form validation                                               | On “/accounts/login/” enter an incorrect form value or not enter a value. Click sign in.                                                           | Sign in will fail and failing error will appear next to the field failed.                                                                                                                                                          | PASS         |
| Sign in - redirect                                                      | On “/accounts/login/” complete the form and click on sign in.                                                                                      | You will be redirected to the homepage (“/”).                                                                                                                                                                                      | PASS         |
| Sign in - feedback                                                      | On “/accounts/login/” complete the form and click on sign in.                                                                                      | After the redirect a green feedback message will appear on the bottom left.                                                                                                                                                        | PASS         |
| Nav / mobile nav – create a project                                     | Click on ‘Create a project’ in the nav.                                                                                                            | You’ll be redirected to “/create-project”.                                                                                                                                                                                         | PASS         |
| Create a project – form validation                                      | In “/create-project” test all inputs but ‘document’ and the approvers fields are required. Click on ‘create project’.                              | Submit will fail if you haven’t entered a required input.                                                                                                                                                                          | PASS         |
| Create a project – form validation approvers                            | In “/create-project” enter either the approver name or approval due date and click ‘create project’.                                               | Submit will fail. Both fields are required if one of the 2 is entered.                                                                                                                                                             | PASS         |
| Create a project – Add approvers                                        | In “/create-project” use the + and – buttons to add or remove as many approvers as needed.                                                         | Clicking on + will add a slot for an extra approver. Clicking on – will remove the last slot.                                                                                                                                      | PASS         |
| Create a project – form submit                                          | In “/create-project” complete the form correctly and fully. Click ‘submit project’.                                                                | After the click, you will be redirected to the homepage. Access the admin panel to find records of the project and approvers created in the database.                                                                              | PASS         |
| Create a project - feedback                                             | In “/create-project” complete the form correctly and fully. Click ‘submit project’.                                                                | After the submission a green feedback message will appear on the bottom left of the screen.                                                                                                                                        | PASS         |
| Create a project - notification                                         | In “/create-project” complete the form correctly and fully. Click ‘submit project’.                                                                | A notification will appear to the approvers selected in the navigation and in /notifications.                                                                                                                                      | PASS         |
| Create a project – title test                                           | In “/create-project” create 2 projects with the same title.                                                                                        |                                                                                                                                                                                                                                    | FAIL         |
| Nav / mobile nav - notification                                         | In the nav click on Notifications.                                                                                                                 | A list of notifications will appear if any.                                                                                                                                                                                        | PASS         |
| Notification                                                            | In “/notifications” click on a notification and then navigate back to “/notifications”.                                                            | The notification you have clicked on disappeared from the list because you read it already.                                                                                                                                        | PASS         |
| Nav / mobile nav – all projects                                         | In the nav click on All projects.                                                                                                                  | You are redirected to (“/”).                                                                                                                                                                                                       | PASS         |
| Nav / mobile nav – My projects                                          | In the nav click on My projects                                                                                                                    | You are redirected to (“/my-projects”).                                                                                                                                                                                            | PASS         |
| Nav / mobile nav – My approvals                                         | In the nav click on My approvals                                                                                                                   | You are redirected to (“/my-approvals.”).                                                                                                                                                                                          | PASS         |
| Nav / mobile nav – Logout                                               | In the nav click on Logout                                                                                                                         | You are asked if you are sure you want to logout.                                                                                                                                                                                  | PASS         |
| Logout                                                                  | In the nav click on Logout and confirm the logout on the second screen.                                                                            | You are logged out. You can’t see the navigation options and you can click on any buttons on the /project-details pages. You are redirected to the page “/”. A Green feedback box on the bottom left will say you have logged out. | PASS         |
| All projects – project approvers                                        | In (“/”). Click on ‘View approvers’ on any project you want.                                                                                       | The project expands and you can see all approvers and their de dates.                                                                                                                                                              | PASS         |
| All projects – view details                                             | In (“/”). Click on ‘View details’ on any project you want.                                                                                         | You are redirected to the project details page.                                                                                                                                                                                    | PASS         |
| All projects / My projects / My approvals – completed or approved color | Complete or approve a project.                                                                                                                     | In “/” or “/my-approvals” or “/my-projects” the project background color turns light green if you are signed in and you are the PM (my projects) or an approver (my-approvals)                                                     | PASS         |
| Project details                                                         | Look at any project you have create on all the pages where a project collapsed or not collapsed appears.                                           | You can always see the project id, title, owner due date, attachment (if any), completion status, approvers (if any), approvers department and approvers due date.                                                                 | PASS         |
| Project details – PM buttons                                            | Log in and click on ‘view details’ for a project where you are not the owner.                                                                      | You can’t click on edit project, delete project or complete project.                                                                                                                                                               | PASS         |
| Project details – PA buttons                                            | Log in and click on ‘view details’ for a project where you are not a project approver.                                                             | You can’t approve the project.                                                                                                                                                                                                     | PASS         |
| Project details – complete and delete 1                                 | Log in and view the details of a project where you are the owner. Click on delete project and complete project.                                    | Defensive design will ask you to confirm your choice.                                                                                                                                                                              | PASS         |
| Project details – complete and delete 2                                 | Log in and view the details of a project where you are the owner. Click on delete project and complete project. Approve also the defensive design. | You are redirected to the ‘my-projects’ page. A green feedback message on the bottom left will indicate the completion of your action.                                                                                             | PASS         |
| Project details - edit                                                  | On any project details page, click on Edit project.                                                                                                | You’ll be redirected to a prepopulated form where you can change the project information.                                                                                                                                          | PASS         |
| Project details – edit 2                                                | Change any field you want and click on ‘create a project’                                                                                          | If you have removed a required field, you’ll get an error. If you have added or removed an approver, the database is updated.                                                                                                      | PASS         |
| Project details – edit 3                                                | Update a project you own.                                                                                                                          | A feedback message on the bottom left will say you have updated the project after the form submission.                                                                                                                             | PASS         |
| Project details – comment form                                          | On any project you want, go to the project details page, fill and submit a comment form.                                                           | The comment submitted will appear below the comment form in chronological order from the newest to the oldest.                                                                                                                     | PASS         |
| My approvals page                                                       | Go to my approvals page                                                                                                                            | Projects are order by due date. You see only projects where you are an approver. Approved projects have a green background.                                                                                                        | PASS         |
| My projects page                                                        | Go to my projects page                                                                                                                             | Projects are order by last created. You see only projects where you are the owner. Completed projects have a green background.                                                                                                     | PASS         |
| Approve a project                                                       | Click on ‘view details’ on a project where you aren’t an approver.                                                                                 | You can’t approve.                                                                                                                                                                                                                 | PASS         |
| Approve a project 2                                                     | Click on ‘view details’ on a project where you are an approver. Click on ‘approve project’                                                         | Defensive design will ask you to confirm the approval.                                                                                                                                                                             | PASS         |
| Approve a project 3                                                     | Click on ‘view details’ on a project where you are an approver. Click on ‘approve project’. Pass the defensive design.                             | A feedback message on the bottom left will say you have approved the project. You are redirected to the /my-approvals page. The background of the project you have approved, will turn light green.                                | PASS         |

### Browser compatibility

All the functionality tests have been carried out and achieved a PASS on the latest versions of the following browsers:
- Google Chrome
- Safari
- Firefox
- Microsoft Edge

### Responsiveness testing

All the functionality tests have been carried out and achieved a PASS on the following screen resolutions:
- 365x667 (iPhone SE)
- 540x720 (Surface Duo)
- 1280x800 (Nest Hub Max)
- 2560x1600 (Macbook Pro M1)

The website has also been tested for responsiveness on [ami.responsivedesign.is](http://ami.responsivedesign.is/) with the following results:
- [index.html](https://ui.dev/amiresponsive?url=https://jannis-kiriasis.github.io/insured/index.html)
- [life-insurance-calculator.html](https://ui.dev/amiresponsive?url=https://jannis-kiriasis.github.io/insured/life-insurance-calculator.html)
- [application-form.html](https://jannis-kiriasis.github.io/insured/application-form.html)

### Lighthouse testing
Overall, the lighthouse report is very positive. 

![Lighthouse report](./README-files/lighthouse-insured.png) 
[Lighthouse report](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Fjannis-kiriasis.github.io%2Finsured%2Findex.html&strategy=mobile&category=performance&category=accessibility&category=best-practices&category=seo&category=pwa&utm_source=lh-chrome-ext)

Note that the performance score varies also depending on the internet connection and device used for testing.

### User stories testing

I've tested whether the user needs have been satisfied with the features created.

| **User stories**                                                                                          | **Features** | **Results** |
|-----------------------------------------------------------------------------------------------------------|--------------|-------------|
| As a user, I want to easily understand the main purpose of the site                                       | 2, 3, 6      | PASS        |
| As a user, I want to have a better idea of what cover I need                                              | 7            | PASS        |
| As a user, I want to get a better understanding of what I need to consider when deciding on a life policy | 6, 7, 8      | PASS        |
| As a user, I want to see how long the questionnaire takes to complete                                     | 4            | PASS        |
| As a user, I want to see at what stage of the questionnaire I am and the number of questions left         | 4            | PASS        |
| As a user, I want to get a personalised result based on my personal needs                                 | 7            | PASS        |
| As a user, I want to be able to take the questionnaire again                                              | 7, 10        | PASS        |
| As a user, I want to be able to find out how much cover I need                                            | 8            | PASS        |
| As a user, I want to be able to apply for a cover easily                                                  | 9            | PASS        |
| As a user, I want to know if my application had a positive outcome                                        | 10           | PASS        |
| As a user, I want to know be able to find my way if I get lost                                            | 3, 11        | PASS        |

## Issues fixed

1. Create many to many relations and templates [Codemy](https://www.youtube.com/watch?v=H3joYTIRqKk&ab_channel=Codemy.com)
2. Automatically create slug from project title [kodnito](https://www.kodnito.com/posts/slugify-urls-django/)
3. Making 2 queries in one view (I thought I had to create 2 views in one template)[Stackoverflow](https://stackoverflow.com/questions/62704325/django-display-multiple-views-in-one-template)
4. How to submit a form and a formset together [Stackoverflow](https://stackoverflow.com/questions/62704325/django-display-multiple-views-in-one-template)
5. Creating dynamic formset with JavaScript [BrennanTymrak](https://www.brennantymrak.com/articles/django-dynamic-formsets-javascript)
6. Filter a parent model based on child model [Stackoverflow](https://stackoverflow.com/questions/28059987/how-can-filter-parent-based-on-children-in-django)
7. How to add a date picker in django forms [Stackoverflow](https://stackoverflow.com/questions/36293061/how-to-include-datepicker-in-django-modelform)
8. Customise the default User model returned field (which is username)[Stackoverflow](https://stackoverflow.com/questions/34214320/django-customize-the-user-models-return-field)
9. If a project with an existing title is submitted, a 500 error page comes up. Solution: used clean method to handle unique title errors.

## Deployment

I've deployed the website on GitHub Pages. The website was developed on Gitpod and pushed to its GitHub repository using git command lines in the terminal. Every time a commit pushed to the website's repository updates the HTML and CSS files, GitHub Pages automatically updates the live demo.
To deploy the website:
1. from the GitHub repository, click on 'settings'
2. find and click on 'pages' on the setting sidebar menu
3. select the branch to be used. In this case 'main'
4. Refresh the page and in a few minutes, the following message will appear if the website was deployed correctly
![website published](./README-files/published-github-pages.png)

To clone the website:
1. Go to the GitHub repository [Insured](https://github.com/jannis-kiriasis/insured)
2. Open the dropdown 'Code'
3. Copy the given url (https://github.com/jannis-kiriasis/insured.git)
4. Open 'Git Bash' on your favourite code editor and select the location where you want to save the cloned directory
5. Type `git clone https://github.com/jannis-kiriasis/insured.git` and press enter to create a local copy

## Credits
### Graphics

- [Calculator icons created by Vitaly Gorbachev - Flaticon](https://www.flaticon.com/free-icons/calculator)
- [Questionnaire icons created by netscript - Flaticon](https://www.flaticon.com/free-icons/questionnaire)
- [Submit icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/submit)
- [Arrow icons created by th studio - Flaticon](https://www.flaticon.com/free-icons/arrow)
- [Arrow icons created by Handicon - Flaticon](https://www.flaticon.com/free-icons/arrow) 

## Acknowledgements

I'm an SEO specialist working for an insurance company in Dublin. So I have some experience with Google tools and marketing life insurance policies to people.

Brian Macharia, my mentor, helped me test the website functionalities and provide excellent recommendations.

I followed this video from [Code with Stein](https://www.youtube.com/watch?v=C8pYT1R8yo4&ab_channel=CodeWithStein) to create the notifications.

I followed this article from [Brennan Tymrak](https://www.brennantymrak.com/articles/django-dynamic-formsets-javascript) to create the dymanic formset with JavaScript to crete and edit a project.

I've used the Unittest on this project from [Elaine Broche](https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes/tree/main/hikebooker) to structure my automated testing. 

To create the README.md file I've used a previously created by me README.md [Insured README.md](https://github.com/jannis-kiriasis/insured/blob/main/README.md) and updated it as needed.

