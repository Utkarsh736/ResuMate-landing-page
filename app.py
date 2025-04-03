from fasthtml.common import *

app = FastHTML()
rt = app.route

@rt('/')
async def get():
    return Titled('ResuMate',
        H2('Your AI-Powered Job Search Companion'),
        P('ResuMate leverages advanced AI technology to streamline your job search process. From crafting the perfect resume to acing your interviews, ResuMate is here to help you every step of the way.'),
        H3('Key Features'),
        Ul(
            Li('AI-driven resume optimization: Get personalized suggestions to make your resume stand out.'),
            Li('Personalized job recommendations: Find job listings tailored to your skills and preferences.'),
            Li('Interview preparation tools: Practice with AI-generated interview questions and feedback.'),
            Li('Career path guidance: Explore potential career trajectories based on your background and goals.')
        ),
        Div(
            H3('Stay Updated'),
            Form(
                Input(type='email', name='email', placeholder='Enter your email'),
                Button('Subscribe'),
                hx_post='/subscribe', target='#subscription-message', hx_swap='innerHTML'
            ),
            Div(id='subscription-message')
        ),
        A('Start Your Journey', href='/signup', cls='button')
    )

@rt('/subscribe', methods=['post'])
async def post(email: str):
    return Div('Thank you for subscribing!', role='alert', cls='success')

serve()