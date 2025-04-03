from fasthtml.common import *

app = FastHTML()
rt = app.route

# Define custom styles
style = Style('''
    :root {
        --pico-primary: #007bff;         /* Primary blue color */
        --pico-primary-hover: #0056b3;   /* Darker blue for hover */
    }
    .section {
        margin-bottom: 2rem;             /* Spacing between sections */
    }
    .cta-button {
        font-size: 1.2rem;               /* Larger button text */
        padding: 0.75rem 1.5rem;         /* Increased padding */
    }
    .success {
        color: green;                    /* Green text for success */
        background-color: lightgreen;    /* Light green background */
        padding: 0.5rem;                 /* Padding for visibility */
        border-radius: 4px;              /* Rounded corners */
    }
''')

@rt('/')
async def get():
    return Titled('ResuMate',
        # Hero Section
        Section(
            H2('Your AI-Powered Job Search Companion'),
            P('ResuMate leverages advanced AI technology to streamline your job search process. From crafting the perfect resume to acing your interviews, ResuMate is here to help you every step of the way.'),
            cls='section'
        ),
        # Features Section
        Section(
            H3('Key Features'),
            Ul(
                Li('AI-driven resume optimization: Get personalized suggestions to make your resume stand out.'),
                Li('Personalized job recommendations: Find job listings tailored to your skills and preferences.'),
                Li('Interview preparation tools: Practice with AI-generated interview questions and feedback.'),
                Li('Career path guidance: Explore potential career trajectories based on your background and goals.')
            ),
            cls='section'
        ),
        # Subscription Section
        Section(
            Article(
                H3('Stay Updated'),
                Form(
                    Input(type='email', name='email', placeholder='Enter your email'),
                    Button('Subscribe'),
                    hx_post='/subscribe', target='#subscription-message', hx_swap='innerHTML'
                ),
                Div(id='subscription-message')
            ),
            cls='section'
        ),
        # Call-to-Action
        Div(
            A('Start Your Journey', href='/signup', cls='button cta-button'),
            style='text-align: center;'  # Center the button
        ),
        head=style  # Add custom styles to the head
    )

@rt('/subscribe', methods=['post'])
async def post(email: str):
    return Div('Thank you for subscribing!', role='alert', cls='success')

serve()