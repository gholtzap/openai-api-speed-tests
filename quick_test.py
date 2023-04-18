import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
model_id = 'text-davinci-001'

def generate_text(prompt, model=model_id):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()



if __name__ == '__main__':
    prompt = "Stanford University, officially Leland Stanford Junior University,[13][14] is a private research university in Stanford, California. The campus occupies 8,180 acres (3,310 hectares), among the largest in the United States, and enrolls over 17,000 students.[15] Stanford is widely considered to be one of the most prestigious universities in the world.[a] Stanford was founded in 1885 by Leland and Jane Stanford in memory of their only child, Leland Stanford Jr., who had died of typhoid fever at age 15 the previous year.[2] Leland Stanford was a U.S. senator and former governor of California who made his fortune as a railroad tycoon. The university admitted its first students on October 1, 1891,[2][3] as a coeducational and non-denominational institution. Stanford University struggled financially after the death of Leland Stanford in 1893 and again after much of the campus was damaged by the 1906 San Francisco earthquake.[16] Following World War II, provost of Stanford Frederick Terman inspired and supported faculty and graduates' entrepreneurialism to build a self-sufficient local industry, which would later be known as Silicon Valley.[17] The university is organized around seven schools on the same campus: three schools consisting of 40 academic departments at the undergraduate level as well as four professional schools that focus on graduate programs in law, medicine, education, and business. The university also houses the public policy think tank, the Hoover Institution. Students compete in 36 varsity sports, and the university is one of two private institutions in the Division I FBS Pac-12 Conference. As of May 26, 2022, Stanford has won 131 NCAA team championships,[18] more than any other university, and was awarded the NACDA Directors' Cup for 25 consecutive years, beginning in 1994–1995.[19] In addition, by 2021, Stanford students and alumni had won at least 296 Olympic medals including 150 gold and 79 silver medals.[20] As of April 2021, 85 Nobel laureates, 29 Turing Award laureates,[note 1] and 8 Fields Medalists have been affiliated with Stanford as students, alumni, faculty, or staff.[41] In addition, Stanford is particularly noted for its entrepreneurship and is one of the most successful universities in attracting funding for start-ups.[42][43][44][45][46] Stanford alumni have founded numerous companies, which combined produce more than $2.7 trillion in annual revenue and have created 5.4 million jobs as of 2011, roughly equivalent to the seventh largest economy in the world (as of 2020).[47][48][49] Stanford is the alma mater of U.S. President Herbert Hoover, 74 living billionaires, and 17 astronauts.[50] In academia, its alumni include the current presidents of Harvard, Yale, and MIT and the provosts of Harvard and Princeton. It is also one of the leading producers of Fulbright Scholars, Marshall Scholars, Rhodes Scholars, and members of the United States Congress.[51] History"
    test_prompt = f"Generate 10 multiple choices questions with answer keys text: {prompt}. Make sure the answer is either A, B, C, or D. Don't put too many answers as the same letter choice."

    print("\n")
    generated_text = generate_text(test_prompt)
    print(f"Prompt: {test_prompt}\n\nGenerated text: {generated_text}")
