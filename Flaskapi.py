from flask import Flask



app = Flask(__name__)  


@app.route("/")


def home():


    return """


    <!doctype html>


<html lang="en">


<head>


  <meta charset="utf-8" />


  <meta name="viewport" content="width=device-width,initial-scale=1" />


  <title>Digital Resume — Ayush kumar  </title>


  <style>


    :root{


      --accent: #6c63ff;


      --bg: #f7f8fc;


      --card: #ffffff;


      --muted:#6b7280;


      --glass: rgba(255,255,255,0.6);


      --radius: 14px;


      color-scheme: light;


    }


    *{box-sizing:border-box}


    body{font-family:Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial; margin:0; background:linear-gradient(180deg,var(--bg),#eef2ff 80%); padding:32px; color:#111827}


    .container{max-width:1000px;margin:0 auto;display:grid;grid-template-columns:300px 1fr;gap:24px}


    .card{background:var(--card);border-radius:var(--radius);padding:20px;box-shadow:0 6px 18px rgba(15,23,42,0.06)}





    /* Sidebar */


    .profile{display:flex;flex-direction:column;align-items:center;text-align:center}


    .avatar{width:120px;height:120px;border-radius:20px;overflow:hidden;margin-bottom:12px;display:inline-grid;place-items:center;background:linear-gradient(135deg,var(--accent),#9b8cff)}


    .avatar svg{width:70%;height:70%;opacity:0.95}


    h1{margin:8px 0 4px;font-size:20px}


    p.role{margin:0;color:var(--muted);font-weight:600}


    .contact{margin-top:16px;width:100%;text-align:left}


    .contact a{display:flex;gap:8px;padding:8px 10px;border-radius:10px;text-decoration:none;color:inherit;align-items:center}


    .contact a:hover{background:#f3f4f6}


    .skill-badge{display:inline-block;background:#f3f4ff;padding:6px 10px;border-radius:999px;margin:6px 6px 0 0;font-size:13px;color:var(--accent)}





    /* Main */


    .headline{display:flex;justify-content:space-between;align-items:flex-start;gap:12px}


    .summary{margin-top:6px;color:var(--muted);line-height:1.5}


    .section{margin-top:18px}


    .section h3{margin:0 0 10px 0;font-size:16px}


    .job{display:flex;justify-content:space-between;gap:12px}


    .job .left{flex:1}


    .job time{color:var(--muted);font-size:13px}


    .list{margin:8px 0 0 0;padding-left:16px}


    .skills-grid{display:flex;flex-wrap:wrap}





    /* utilities */


    .muted{color:var(--muted)}


    .small{font-size:13px}


    .btn{display:inline-flex;gap:8px;align-items:center;padding:8px 12px;border-radius:10px;background:var(--accent);color:white;text-decoration:none;font-weight:600}


    .actions{display:flex;gap:8px}





    /* Responsive */


    @media (max-width:880px){


      .container{grid-template-columns:1fr; padding:0 12px}


      .avatar{width:96px;height:96px}


      .headline{flex-direction:column;align-items:flex-start}


    }


  </style>


</head>


<body>


  <div class="container">


    <!-- SIDEBAR -->


    <aside class="card profile">


      <div class="avatar" aria-hidden>


        <!-- simple icon placeholder -->


        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="24" height="24" rx="6" fill="white"/><path d="M12 12c1.657 0 3-1.567 3-3.5S13.657 5 12 5s-3 1.567-3 3.5S10.343 12 12 12zM6 19c0-2.667 2.686-4 6-4s6 1.333 6 4" stroke="rgba(0,0,0,0.08)" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>


      </div>


      <h1 id="name">Ayuhs kumar</h1>


      <p class="role">Software Developer • Jaipur</p>





      <div class="contact">


        <a href="mailto:you@example.com" title="Email">✉️ Ayushkumar@gmail.com</a>


        <a href="#" title="Phone">📞 +91 8210615625 </a>


        <a href="#" title="Website">🔗  ayushkumar.com</a>


        <a href="#" title="LinkedIn">🔗 linkedin.com/in/ayuhskumar</a>


      </div>





      <div class="section small">


        <h3>Key Skills</h3>


        <div class="skills-grid">


          <span class="skill-badge">HTML</span>


          <span class="skill-badge">CSS</span>


          <span class="skill-badge">JavaScript</span>


          <span class="skill-badge">React</span>


          <span class="skill-badge">Python</span>


        </div>


      </div>





      <div class="section small">


        <h3>Languages</h3>


        <p class="muted">English (Fluent)<br>Hindi (Native)</p>


      </div>





      <div class="section small">


        <h3>Education</h3>


        <p class="muted">B.Sc. / B.Tech — Vivekanand Global University, Jaipur<br><span class="small">2024 — Present</span></p>


      </div>


    </aside>





    <!-- MAIN -->


    <main class="card">


      <div class="headline">


        <div>


          <h2 style="margin:0">Professional Summary</h2>


          <p class="summary">Concise 2–3 line summary about you — who you are, what you do, and what value you bring. Focus on achievements and tools you use.</p>


        </div>


        <div class="actions">


          <button class="btn" onclick="window.print()">Download / Print</button>


        </div>


      </div>





      <section class="section">


        <h3>Experience</h3>





        <article class="job">


          <div class="left">


            <strong>Intern / Frontend Developer</strong>


            <div class="small muted">Company Name — Brief description of company or team</div>


            <ul class="list">


              <li>Built responsive UI components and improved performance by X%.</li>


              <li>Collaborated with designers and back-end teams to ship features.</li>


            </ul>


          </div>


          <div class="right small muted">


            <time>Jun 2024 — Present</time>


          </div>


        </article>





        <hr style="margin:12px 0;border:none;border-top:1px solid #eef2ff" />





        <article class="job">


          <div class="left">


            <strong>College Project — Cloud AI Website</strong>


            <div class="small muted">Personal / Academic Project</div>


            <ul class="list">


              <li>Designed a cloud services marketplace integrating AI-based recommendations.</li>


              <li>Implemented animations, responsive layout, and a demo chatbot using simple JS.</li>


            </ul>


          </div>


          <div class="right small muted">


            <time>Apr 2025 — Jun 2025</time>


          </div>


        </article>


      </section>





      <section class="section">


        <h3>Projects & Achievements</h3>


        <ul class="list">


          <li><strong>AI Sign Language Translator</strong> — Prototype web app that uses webcam input + ML model to translate signs.</li>


          <li><strong>Cloud Cost Optimizer</strong> — Script that analyzes usage and suggests cheaper plans.</li>


        </ul>


      </section>





      <section class="section">


        <h3>Skills</h3>


        <div class="skills-grid">


          <span class="skill-badge">Responsive Design</span>


          <span class="skill-badge">REST APIs</span>


          <span class="skill-badge">Git</span>


          <span class="skill-badge">Docker (Basics)</span>


          <span class="skill-badge">Data Structures</span>


        </div>


      </section>





      <section class="section">


        <h3>Education</h3>


        <p class="muted"><strong>University / College Name</strong><br>Bachelor of Technology — Major<br><span class="small">2023 — Present • GPA: —</span></p>


      </section>





      <section class="section">


        <h3>Extras</h3>


        <p class="small muted">Interests: Open-source, UI/UX, Machine Learning • Available for internships and freelance.</p>


      </section>





      <footer style="margin-top:20px;text-align:center" class="small muted">Tip: Edit the HTML to replace placeholders with your real info. Use the browser Print dialog to save as PDF.</footer>


    </main>


  </div>





  <script>


    // small script: fill demo name from localStorage if available


    (function(){


      const nameEl = document.getElementById('name');


      const stored = localStorage.getItem('resume_name');


      if(stored) nameEl.textContent = stored;


    })();


  </script>


</body>


</html>





    """


    


@app.route("/about")  


def about():


    return """


    <h1>i am aboutpage</h1>


    <h2>I am running in Flask</h2>


    """


if __name__=='__main__':  


    app.run()
