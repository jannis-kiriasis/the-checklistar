# Project 2 - Insured

[The Checklistar live demo](https://jannis-kiriasis.github.io/insured/index.html)\
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

![queries about workflow management system](./README-files/workflow-management-system-keywords.png)

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

![Insured responsive design](./README-files/i-am-responsive.png)

## User Experience (UX) - user stories
Now that we are familiar with The Checklistar target audience and offering, we are looking at the needs the app users may have. Following, you can find the epics an the user stories break down used to plan the development of the app.

### Users goals

| **User stories**                                                                                          |
|-----------------------------------------------------------------------------------------------------------|
| As a user, I want to easily understand the main purpose of the site                                       |
| As a user, I want to have a better idea of what cover I need                                              |
| As a user, I want to get a better understanding of what I need to consider when deciding on a life policy |
| As a user, I want to see how long the questionnaire takes to complete                                     |
| As a user, I want to see at what stage of the questionnaire I am and the number of questions left         |
| As a user, I want to get a personalised result based on my personal needs                                 |
| As a user, I want to be able to take the questionnaire again                                              |
| As a user, I want to be able to find out how much cover I need                                            |
| As a user, I want to be able to apply for a cover easily                                                  |
| As a user, I want to know if my application had a positive outcome                                        |
| As a user, I want to know be able to find my way if I get lost                                            |

## Features

In the following paragraphs, we are going to see what features appear on the website and where they meet the users' needs.

### Global features

This is a list of features that appear on every page.

1.	**Logo**  
    The logo appears on every page. As an industry standard, the logo links back to the homepage.

    ![Logo](./README-files/insured-logo.png)

2.	**Main heading**  
    The main heading appears on every page of the questionnaire, calculator and application form.
    In the questionnaire, the main heading is the placeholder for the questions. Its content changes using DOM manipulation rules at every button click.

    ![Heading](./README-files/main-heading.png)

3.	**Sstages**  
    I've used graphics to represent the 3 pages included on the website: The questionnaire, the calculator and the application form. It lets users know at what stage of the whole process they are. 
    
    The current page icon becomes Verdigris when the page is active.

    ![Navigation](./README-files/navigation.png)

### Questionnaire features - index.html

4.	**Progress bar**  
    The progress bar helps users see at what stage of the questionnaire they are. The full questionnaire includes an intro, 5 questions and the results page. 
    The current progress circle is blue. The past questions / pages are green. The progress bar updates at every button click with DOM manipulation, so when users start the questionnaire or answer a question.

    ![Progress bar](./README-files/progress-bar.png)

    **Mobile progress bar**  
    The mobile progress bar shows the current page only when users are on the intro page or results page. On the actual questions, the progress update shows the current question number on the total (x / 5).

    ![Mobile progress bar](./README-files/mobile-progress-bar.png)

5.	**Intro page**  
    The intro page explains to users what Insured is all about. It also collects the user name which is stored in session storage and used later on. The user name is required and it's validated with other JS rules. 

    If users click on 'start' and the user name hasn't been added or it doesn't pass validation, an alert message will show up and the input fields border becomes red.

    ![Intro](./README-files/intro-page.png)

6.	**Question pages**  
    When users click start on the intro page and pass the username validation test, the first question is served and the progress bar updates. Yes and no buttons also appear on the screen. This is all handled with DOM manipulation and updated as the user clicks on yes / no to go to the next question.

    User answers are stored in variables.

    ![Question pages](./README-files/question-pages.png)

7.	**Results page**  
    Based on the answers provided, the results page tells users what life cover they may need. It uses logic to determine what content to show. If users answer yes to at least 1 question, the 'calculate your life insurance need' button will be shown. It brings users to the next step: calculate the cover amount they need. If all the user's answers have a negative outcome, only the button to restart is shown.

    ![Results page](./README-files/results.png)

### Life cover calculator features - life-insurance-calculator.html

8.	**Calculator**  
    A simple calculator to help users figure out how much life insurance they need. There are only 2 input fields: salary and years of cover needed. The calculation is a simple multiplication. Input fields are validated with HTML and JS rules.

    If the input fields aren't blank and differ from 0, an 'apply now for this cover' button is shown together with a 'recalculate' button.

    Users' inputs are saved in session storage.

    ![Calculator](./README-files/calculator.png)

### Application form features - application-form.html

9.	**Application form**  
    The contact form is prepopulated with the data previously asked to users. Users only need to add their contact details and click apply. New input fields validation rules are used on all fields. 

    ![Application form](./README-files/application-form.png)

10. **Confirmation message**
    An application submitted message appears on the screen when the form is submitted correctly. This is done using DOM manipulation. In the confirmation message, there is also a summary of the information submitted and a button to restart from the questionnaire.

    An email with the data submitted is also sent to the user and to Insured.

### Others
11. **Custom 404 page**  
    A custom 404 page asks visitors what page they were looking for.

    ![Custom 404 page](./README-files/404-page.png)

## Where user stories meet features

In the following paragraph, I’m going to match features with user needs (user stories). The features are numbered and the same feature numbers appear in the table below.

| **User stories**                                                                                          | **Features** |
|-----------------------------------------------------------------------------------------------------------|--------------|
| As a user, I want to easily understand the main purpose of the site                                       | 2, 3, 6      |
| As a user, I want to have a better idea of what cover I need                                              | 7            |
| As a user, I want to get a better understanding of what I need to consider when deciding on a life policy | 6, 7, 8      |
| As a user, I want to see how long the questionnaire takes to complete                                     | 4            |
| As a user, I want to see at what stage of the questionnaire I am and the number of questions left         | 4            |
| As a user, I want to get a personalised result based on my personal needs                                 | 7            |
| As a user, I want to be able to take the questionnaire again                                              | 7, 10        |
| As a user, I want to be able to find out how much cover I need                                            | 8            |
| As a user, I want to be able to apply for a cover easily                                                  | 9            |
| As a user, I want to know if my application had a positive outcome                                        | 10           |
| As a user, I want to know be able to find my way if I get lost                                            | 3, 11        |

## Wireframes

The first draft of the website was completed by creating wireframes using Balsamic. 

- **Questionnaire**   
![Intro page wireframe](./README-files/intro-page-wf.png)
![Questions wireframe](./README-files/questions-wf.png)
![Results wireframe](./README-files/results-page-wf.png)

- **Calculator & Application form**  
I had the idea of adding a calculator and an application form while WIP so wireframes aren't available.

## Features left to implement 

- Little info boxes can be added next to each input field to clarify why that information is needed.
- Additional fields can be added to the calculator to make it more advanced. An 'extra fields' dropdown could reveal more input fields and so give users the option to use the short calculator or the advanced calculator.
- More questions can be added to the questionnaire: there are life insurance policies that haven't been covered such as the serious illness cover. More questions can be asked to the users to give an even more specific result.
- Calculators for mortgage protection and income protection can also be created.
- Preselected cover type input fields can be added to the application form. The field will be preselected to the cover type users need based on their questionnaire results.

## Design

In the following paragraph, I'm going to explain the colours, typography and imagery choices.

### Colours

The main colour used is a shade of blue (Liberty). Blue is a calm and serene colour. It is often associated with stability and reliability. Most of the insurance companies I can think of have at least one shade of blue in their colour palette (Allianz, Aviva, Axa, Zurich to name a few) and so Insured had to have a blue too. I've increased a bit the contrast ratio with light backgrounds to achieve accessibility best scores.

As I chose Liberty, I needed an opposite colour to create contrast with important elements on the page, such as the buttons. So, I picked a shade of red, Fuzzy Wuzzy and increased its contrast ratio with light colours to pass accessibility tests.

As secondary colours, I've used a shade of green (Verdigris) to highlight the past questions in the progress bar, and a tan colour used for smaller decorative purposes. I've also added  Timberwolf in case I needed a light grey but I haven't used it. May become useful for future development. 

![Color Palette](./README-files/insured-color-palette.png)

All the text colour combinations have been tested for accessibility and they all achieve WCAG AAA.
- [Colour contrast test: white on red](https://webaim.org/resources/contrastchecker/?fcolor=FFFFFF&bcolor=A42D2D) - Used on buttons.  
- [Colour contrast test: black on light blue](https://webaim.org/resources/contrastchecker/?fcolor=000000&bcolor=F3F4FA) - Used on the main text area.  
- [Colour contrast test: blue on light blue](https://webaim.org/resources/contrastchecker/?fcolor=3B4D97&bcolor=F3F4FA) - Used on headings.  

Tested with [Contrast checker](https://webaim.org/resources/contrastchecker/).

### Typography

The typography was chosen for my liking. Open Sans is a very popular font if not the most popular.

I used [Open Sans](https://fonts.google.com/specimen/Open+Sans) for all body elements.  

The fallback font used is Helvetica for all body elements.

### Imagery

I've used graphics for the logo, favicon and the navigation process. The navigation graphics come from [Flaticon](https://www.flaticon.com/).

I've used SVG images where possible that are lighter than jpg and since it's a vector format, graphics always look sharp. It works well with logos and 'flat' graphics.

## Accessibility

As mentioned above, all the colour combinations used for text passed a contrast ratio test. During the testing phase, the white fonts on the red backgrounds (only used to style buttons) resulted low in contrast ratio. The red colour was adjusted to pass and achieve an accessibility score of WCAG AAA.

I've also used alt tags to describe images and aria labels to describe links.  
The pages have been structured using semantic HTML markup.  

The Lighthouse accessibility test also reports an accessibility score of 100/100. 

A Lighthouse report is available in a few paragraphs below in the testing section.

## SEO

Keywords have been used in the headings of the questionnaire start page and life insurance calculator page. Each page addresses a specific search intent:
- On the questionnaire page, the need of knowing whether a life insurance cover is needed
- the calculator page, the need for a life cover calculator
- The application form, the need of getting a cover painlessly

The title tags also include target keywords and the length displays in full on Google Search. Tested with this [title tag length checker](https://www.highervisibility.com/seo/tools/serp-snippet-optimizer/).

I've included the most common metadata (description, keywords, index) and a self-referring `rel=canonical` link on each page.

I've included Open Graph tags to control the pages' appearance when shared on social media as posts.

The Lighthouse SEO test also reports a score of 100/100. 

A Lighthouse report is available a few paragraphs below in the testing section.

## Technologies and tools used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://it.wikipedia.org/wiki/JavaScript)
- Version control: [Git](https://git-scm.com/)
- Public repository: [GitHub](https://github.com/)
- Resize and edit images: [Pixlr.com](https://pixlr.com/)
- Transform png to SVG: [Convertio.co](https://convertio.co/it/png-svg/)
- Graphics: [Flaticon](https://www.flaticon.com/)
- Google Font: [Open Sans](https://fonts.google.com/specimen/Open+Sans)
- Wireframes: [Balsamiq](https://balsamiq.com/)
- Lighthouse: [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
- Colours contrast checker: [Contrast checker](https://color-contrast-checker.deque.com/)
- Colours accessibility: [Webiam](https://webaim.org/resources/contrastchecker/)
- Send emails with JS: [emailJS](https://www.emailjs.com/)
- Uniform alert on all browsers: [SweetAlert](https://sweetalert2.github.io/)

## Testing

I've carried out the following tests:

1. [HTML validation](#html-validation)
2. [CSS validation](#css-validation)
3. [JavaScript validation](#js-validation)
4. [Functionality testing](#functionality-testing)
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

### Functionality testing

I've tested that the different functionalities of the website work as intended.

|                     Test Label                     |                                                              Test Action                                                              |                                                                                                                                                                Expected Outcome                                                                                                                                                                |  Test Outcome  |
|:--------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------:|
| Header                        | Click on all header internal links to verify they work (all pages).                                                                   | No links return a 404 error.                                                                                                                                                                                                                                                                                                                   | PASS all pages |
| Header links                        | Click on all header internal links to verify they link to the right pages (all pages).                                                | All links should link to the pages described in their anchor images.                                                                                                                                                                                                                                                                            | PASS all pages |
| On ‘start’ click                                   | Click on Start to verify that the questionnaire doesn’t start if the user name isn’t valid.                                                        | The questionnaire will start only if the username is 1 word, contains no numbers or special characters, is between 3 and 25 characters long.                                                                                                                                                                                                           | PASS           |
| On ‘start’ click                                   | Click on Start and if username validation is passed, the first question is shown                                                  | After username validation, the first question with yes / no buttons is shown.                                                                                                                                                                                                                                                                         | PASS           |
| On ‘yes no’ click                                  | Click on Yes / no to verify that user answers are saved.                                                                              | Type userAnswers in the console (in Developer Tools) and it will show the clicks saved                                                                                                                                                                                                                                                                                                 | PASS           |
| On ‘yes no’ click                                  | On yes no clicks, question changes, progress bar updates.                                                                             | On the buttons click a new question appears, the past question progress placeholder becomes Verdigris and the current question placeholder Liberty.                                                                                                                                                                                                             | PASS           |
| On ‘yes no’ click                                  | On the last yes no click, results are shown.                                                                                              | Based on the answers provided, different content is triggered. The user name appears in the first line.                                                                                                                                                                                                                                             | PASS           |
| Calculator input fields validation                 | Click on ‘calculate’ without entering any value.                                                                                      | An alert will say that salary and years fields are mandatory and the input border becomes red.                                                                                                                                                                                                                                                     | PASS           |
| Calculator input fields validation                 | Click on ‘calculate’ after entering salary and years.                                                                                 | A multiplication result is shown together with ‘apply now for this cover’ and ‘recalculate’ buttons.                                                                                                                                                                                                                                           | PASS           |
| ‘Recalculate’ clicks                               | Enter a new salary and / or years and click recalculate.                                                                              | The new multiplication result is shown.                                                                                                                                                                                                                                                                                                        | PASS           |
| Input fields storage                               | After clicking on ‘Apply now for this cover’ open sessions storage in Developer Tools.                                                | The input field values will be stored in session storage.                                                                                                                                                                                                                                                                                      | PASS           |
| Application form opening                           | When ./application-form.html opens, if anything is stored in session storage, the form fields will be prepopulated.                   | Form fields will be prepopulated if any value is stored in session storage.                                                                                                                                                                                                                                                                    | PASS           |
| Application form fields validation                 | On ‘apply’ click, some logic will validate all input fields. Try to leave a field blank one by one and check if an alert box appears. | On ‘apply’ click: -       All fields are mandatory -       Username validation is equal to the questionnaire username validation -       Salary and years validation is equal to the calculator input fields validation -       Phone number must be between 7 and 9 digits. -       Email is validated with html role and ‘email’ input type. | PASS           |
| On ‘apply’ click                                   | Click on 'apply', if validation is passed, a message will be shown.                                                                     | DOM manipulation will show a thank you message, a recap of the data provided and a button to restart the questionnaire.                                                                                                                                                                                                                        | PASS           |
| On ‘restart with new’ name click on thank you page | Click on 'Restart with new name' and you’ll go back to the beginning of the questionnaire.                                              | On button click, go back to questionnaire and storageSession is cleared.                                                                                                                                                                                                                                                                       | PASS           |
| On page change                                     | When opening a new page, the related icon below the logo will turn Verdigris.                                                         | On the current page, the related icon turns Verdigris.                                                                                                                                                                                                                                                                                                         | PASS           |
| 404 links                                          | Click on a non-existing URL and verify it lands on the custom 404 page.                                                               | A non-existing page links to the custom 404.html                                                                                                                                                                                                                                                                                               | PASS           |
|                                                    |                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                |                |
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

1. Cannot set properties of undefined (setting 'onclick'): I was using a function that I actually didn't need. I removed the function and the issue was gone.
2. Cannot read properties of null (reading 'classList'): I was trying to add a class property to an element that didn't exist (past questions). In my `progressUpdate()` function a past question exists only if runningQuestion is in `runningQuestion[1]`, while in `runningQuestion[0]` past questions don't exists since `runningQuestion[0]` is the first question. So with an if stamement I made the code generating the error, running only if `runningQuestion !== 0`. This worked.
3. Override iPhone / iPad default styling of submit button. The button isn't styled as declared in the CSS. Solution: add to the class .button `-webkit-appearance: none;`. [Stackoverflow](https://stackoverflow.com/questions/5438567/css-submit-button-weird-rendering-on-ipad-iphone).
4. On mobile yes / no buttons were retaining the :hover styling after being clicked. I made the hover styling exist only for devices where hover is real with a media query. [Stackoverflow](https://stackoverflow.com/questions/23885255/how-to-remove-ignore-hover-css-style-on-touch-devices).


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

I've followed [this video](https://www.youtube.com/watch?v=49pYIMygIcU&t=2066s) by Code Explained to create the logic to loop through the questions and create the progress bar (`progressUpdate()`, `nextQuestion()`, `leftQuestions()` and related event listeners and varibles). I've edited the code to fit this website.

I've used [this guide](https://www.javascripttutorial.net/javascript-dom/javascript-form-validation/) published on javascripttutorial.net to create part of the username input validation logic. The code was edited to fit this website.

I've used [this thread](https://stackoverflow.com/questions/17616624/detect-if-string-contains-any-spaces) to detect if the username input value contains any white spaces.

To create the README.md file I've used a previously created by me README.md [digibooking README.md](https://github.com/jannis-kiriasis/digibooking/blob/main/README.md) and updated it as needed.

## Disclaimer

I'm not a financial advisor. This website doesn't constitute financial advice and it has been created as part of a post graduate degree project. 

Your data aren't retained and will be deleted as the session expires. 

By clicking apply, you aren't actually applying for a life insurance policy. 

More factors need to be taken into consideration when deciding if to get a life insurance policy and calculating the amount. Don't rely on this website for your life insurance but contact a financial advisor.
